$(document).ready(function () {

    $('#send_message').click(function (e) {
        e.preventDefault();

        var error = false;
        var name    = $('#name').val();
        var email   = $('#email').val();
        var phone   = $('#phone').val();
        var message = $('#message').val();

        // Clear error state on re-click
        $('#name, #email, #phone, #message').click(function () {
            $(this).removeClass('error_input');
        });

        // Field validation
        if (name.length === 0) {
            error = true;
            $('#name').addClass('error_input');
        } else {
            $('#name').removeClass('error_input');
        }

        if (email.length === 0 || email.indexOf('@') === -1) {
            error = true;
            $('#email').addClass('error_input');
        } else {
            $('#email').removeClass('error_input');
        }

        if (phone.length === 0) {
            error = true;
            $('#phone').addClass('error_input');
        } else {
            $('#phone').removeClass('error_input');
        }

        if (message.length === 0) {
            error = true;
            $('#message').addClass('error_input');
        } else {
            $('#message').removeClass('error_input');
        }

        if (error === false) {
            var $btn = $('#send_message');
            $btn.prop('disabled', true).val('Sending...');

            $.post('contact.php', $('#contact_form').serialize(), function (result) {
                if (result === 'sent') {
                    // Hide the form and show the success message
                    $('#contact_form').fadeOut(300, function () {
                        $('#success_message').fadeIn(500);
                    });
                } else {
                    // Show error, re-enable button
                    $('#error_message').fadeIn(500);
                    $btn.prop('disabled', false).val('Send Message');
                }
            }).fail(function () {
                $('#error_message').fadeIn(500);
                $btn.prop('disabled', false).val('Send Message');
            });
        }
    });

});
