<?php
/**
 * Contact Form Handler — Gavhane Syndicate Transport
 * Uses PHPMailer with Gmail SMTP for reliable email delivery.
 *
 * Setup:
 *   1. Run:  composer require phpmailer/phpmailer
 *   2. Fill in mailer-config.php with your Gmail App Password
 */

// Only accept POST requests
if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    exit('Method Not Allowed');
}

// Load PHPMailer (installed via Composer)
require_once __DIR__ . '/vendor/autoload.php';
require_once __DIR__ . '/mailer-config.php';

use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\SMTP;
use PHPMailer\PHPMailer\Exception;

// ── Input sanitization ────────────────────────────────────────────
$name    = isset($_POST['name'])    ? htmlspecialchars(trim($_POST['name']),    ENT_QUOTES, 'UTF-8') : '';
$email   = isset($_POST['email'])   ? trim($_POST['email'])                                          : '';
$phone   = isset($_POST['phone'])   ? htmlspecialchars(trim($_POST['phone']),   ENT_QUOTES, 'UTF-8') : '';
$message = isset($_POST['message']) ? htmlspecialchars(trim($_POST['message']), ENT_QUOTES, 'UTF-8') : '';

// ── Server-side validation ────────────────────────────────────────
if (empty($name) || empty($email) || empty($phone) || empty($message)) {
    echo 'failed';
    exit;
}

if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
    echo 'failed';
    exit;
}

$email = filter_var($email, FILTER_SANITIZE_EMAIL);

// ── Send via PHPMailer + Gmail SMTP ───────────────────────────────
$mail = new PHPMailer(true);

try {
    // SMTP settings
    $mail->isSMTP();
    $mail->Host       = SMTP_HOST;
    $mail->SMTPAuth   = true;
    $mail->Username   = SMTP_USERNAME;
    $mail->Password   = SMTP_PASSWORD;
    $mail->SMTPSecure = SMTP_SECURE;
    $mail->Port       = SMTP_PORT;
    $mail->CharSet    = 'UTF-8';

    // Recipients
    $mail->setFrom(MAIL_FROM, MAIL_FROM_NAME);
    $mail->addAddress(MAIL_TO, MAIL_FROM_NAME);
    $mail->addReplyTo($email, $name);   // Reply goes directly to the enquirer

    // Email content
    $mail->isHTML(true);
    $mail->Subject = MAIL_SUBJECT;

    $mail->Body = '
<!DOCTYPE html>
<html lang="en">
<body style="font-family:Arial,sans-serif;font-size:15px;color:#333;background:#f4f4f4;padding:20px;">
  <div style="max-width:560px;margin:0 auto;background:#fff;border-radius:8px;overflow:hidden;box-shadow:0 2px 8px rgba(0,0,0,.08);">
    <div style="background:#c0392b;padding:24px 32px;">
      <h2 style="margin:0;color:#fff;font-size:20px;">New Enquiry — Gavhane Syndicate Transport</h2>
    </div>
    <div style="padding:28px 32px;">
      <table style="width:100%;border-collapse:collapse;">
        <tr>
          <td style="padding:10px 0;border-bottom:1px solid #eee;width:120px;font-weight:bold;color:#555;">Name</td>
          <td style="padding:10px 0;border-bottom:1px solid #eee;">' . $name . '</td>
        </tr>
        <tr>
          <td style="padding:10px 0;border-bottom:1px solid #eee;font-weight:bold;color:#555;">Email</td>
          <td style="padding:10px 0;border-bottom:1px solid #eee;">' . $email . '</td>
        </tr>
        <tr>
          <td style="padding:10px 0;border-bottom:1px solid #eee;font-weight:bold;color:#555;">Phone</td>
          <td style="padding:10px 0;border-bottom:1px solid #eee;">' . $phone . '</td>
        </tr>
        <tr>
          <td style="padding:14px 0 4px;font-weight:bold;color:#555;vertical-align:top;">Message</td>
          <td style="padding:14px 0 4px;">' . nl2br($message) . '</td>
        </tr>
      </table>
    </div>
    <div style="background:#f9f9f9;padding:16px 32px;font-size:12px;color:#aaa;">
      Sent from the contact form at gavhanesyndicatetransport.com
    </div>
  </div>
</body>
</html>';

    // Plain-text fallback
    $mail->AltBody = "New Enquiry - Gavhane Syndicate Transport\n\n"
        . "Name:    {$name}\n"
        . "Email:   {$email}\n"
        . "Phone:   {$phone}\n"
        . "Message: {$message}\n";

    $mail->send();
    echo 'sent';

} catch (Exception $e) {
    // Log the error server-side; never expose details to the browser
    error_log('Mailer Error: ' . $mail->ErrorInfo);
    echo 'failed';
}
