import os
import re

BASE = r"c:/Users/yavis/Downloads/transportation-cargo-logistics-website-template-2025-11-06-11-13-28-utc/LogiXpress/LogiXpress HTML"

SERVICES = [
    {
        "file": "service-trucking.html",
        "title": "Trucking Services",
        "bg": "images/background/4.webp",
        "img": "images/misc/s3.webp",
        "desc": "Gavhane Syndicate Transport provides reliable trucking services across Maharashtra with a fleet of trucks suited for all cargo types. From small consignments to large industrial shipments, our experienced drivers and well-maintained vehicles ensure your goods reach their destination safely and on schedule.",
        "tagline": "Reliable trucking across Maharashtra with experienced drivers and a well-maintained fleet.",
        "features": [
            ("Multi-Tonnage Fleet", "Our trucks range from light to heavy-duty, handling cargo from small parcels to full truckloads across Maharashtra."),
            ("Experienced Drivers", "Our drivers are trained, licensed, and experienced in navigating Maharashtra's industrial zones, highways, and port routes."),
            ("On-Time Delivery", "We prioritize scheduling and route optimization to ensure every consignment reaches its destination on time."),
            ("Industries Served", "We serve Steel, Cement, Chemicals, Textiles, Pharmaceuticals, Automotive, and more across Maharashtra."),
            ("Full Documentation", "We handle all transport documentation including lorry receipts, e-way bills, and delivery challans."),
            ("GPS-Tracked Fleet", "Our vehicles are equipped with GPS tracking for real-time visibility of your consignment at all times."),
        ],
    },
    {
        "file": "service-container-20ft.html",
        "title": "20ft Container Transport",
        "bg": "images/background/4.webp",
        "img": "images/misc/s3.webp",
        "desc": "We specialize in 20ft container transport from JNPT (Nhava Sheva), Mumbai Port, and major industrial zones across Maharashtra. Our fleet includes purpose-built container trailers with experienced operators who understand port logistics, customs procedures, and safe container handling.",
        "tagline": "Expert 20ft container movement from port to plant across Maharashtra.",
        "features": [
            ("Port to Plant Delivery", "Seamless 20ft container movement from JNPT, Nhava Sheva, and Mumbai Port directly to your factory or warehouse."),
            ("Customs Coordination", "We work closely with clearing agents to ensure smooth customs clearance and immediate pickup post-release."),
            ("Experienced Operators", "Our container trailer operators are trained in safe loading, lashing, and port gate procedures."),
            ("Timely Pickup", "We ensure prompt container pickup within port-allowed free days to avoid costly detention charges."),
            ("Pan-Maharashtra Delivery", "We deliver 20ft containers to all major industrial areas including Pune, Nashik, Aurangabad, Chakan, Talegaon, and more."),
            ("Complete Documentation", "End-to-end handling of DO, gate passes, delivery orders, and all transport documentation."),
        ],
    },
    {
        "file": "service-container-40ft.html",
        "title": "40ft Container Transport",
        "bg": "images/background/4.webp",
        "img": "images/misc/s3.webp",
        "desc": "Gavhane Syndicate Transport handles 40ft container transport with specialized trailers and permits for oversized loads. Our expertise in large container logistics ensures your heavy and bulky shipments are moved safely, legally, and efficiently from port to destination anywhere in Maharashtra.",
        "tagline": "Safe and efficient 40ft container movement with specialized trailers and permits.",
        "features": [
            ("Heavy-Duty Trailers", "Our 40ft container trailers are purpose-built for heavy loads and maintained to the highest safety standards."),
            ("Over-Dimensional Permits", "We obtain all necessary permits for oversized container transport on Maharashtra state and national highways."),
            ("Port Expertise", "Deep knowledge of JNPT, Nhava Sheva, and Mumbai Port procedures ensures fast and compliant container pickup."),
            ("Wide Network Coverage", "We cover all of Maharashtra including remote industrial estates, MIDC zones, and SEZs."),
            ("Lashing & Securing", "Cargo is properly lashed and secured inside containers using approved methods to prevent in-transit damage."),
            ("Dedicated Coordinator", "A dedicated transport coordinator manages each 40ft container movement keeping you informed at every step."),
        ],
    },
    {
        "file": "service-side-open-truck.html",
        "title": "Side Open Truck Services",
        "bg": "images/background/4.webp",
        "img": "images/misc/s3.webp",
        "desc": "Our side open trucks are ideal for loading and unloading cargo from the side, making them perfect for factories, warehouses, and tight loading bays. These versatile vehicles handle wide, flat, and irregularly shaped cargo that standard enclosed trucks cannot accommodate.",
        "tagline": "Flexible side-loading trucks for wide, flat, and irregular cargo across Maharashtra.",
        "features": [
            ("Side-Loading Design", "Side open trucks allow forklift and crane loading/unloading from either side, saving time and reducing handling damage."),
            ("Wide Cargo Compatibility", "Ideal for steel coils, machinery, sheets, pipes, and other wide or flat cargo that doesn't fit in standard trucks."),
            ("Factory-Friendly", "Perfect for industrial clients with side-entry loading docks and restricted overhead space."),
            ("Multiple Sizes", "Available in various tonnages to match your cargo weight and volume requirements."),
            ("Experienced Operators", "Our drivers are trained in safe loading and securing of wide and heavy cargo types."),
            ("Pan-Maharashtra Service", "Side open truck services available across all major industrial zones in Maharashtra."),
        ],
    },
    {
        "file": "service-odc.html",
        "title": "ODC Consignment",
        "bg": "images/background/4.webp",
        "img": "images/misc/s3.webp",
        "desc": "Over-Dimensional Cargo (ODC) consignment is our specialty. We handle the movement of large, heavy, and oversized industrial equipment across Maharashtra using specialized trailers, route surveys, escort vehicles, and all required government permits. Trusted by leading manufacturers for moving turbines, transformers, and heavy machinery.",
        "tagline": "Specialized ODC transport with permits, escorts, and route surveys for oversized loads.",
        "features": [
            ("Specialized ODC Trailers", "We operate low-bed, semi-low-bed, and extendable trailers designed for the largest and heaviest industrial loads."),
            ("Route Survey & Planning", "Our team conducts thorough route surveys to identify bridges, underpasses, and road conditions before every ODC movement."),
            ("Government Permits", "We handle all ODC permits from the Maharashtra PWD, RTO, and National Highway Authority for legal movement."),
            ("Escort Vehicles", "Police and private escort vehicles provided as required for safe passage of oversized loads on public roads."),
            ("Heavy Industry Expertise", "Experience moving turbines, transformers, pressure vessels, boilers, and large industrial machinery."),
            ("End-to-End Management", "From survey to delivery, we manage every aspect of your ODC consignment movement."),
        ],
    },
    {
        "file": "service-labour-supply.html",
        "title": "Labour Supply & Contractors",
        "bg": "images/background/4.webp",
        "img": "images/misc/s3.webp",
        "desc": "Gavhane Syndicate Transport provides skilled and unskilled labour for loading, unloading, material handling, and industrial operations. Our workforce is experienced, reliable, and available for both short-term and long-term assignments at factories, warehouses, ports, and construction sites across Maharashtra.",
        "tagline": "Reliable skilled and unskilled labour for loading, unloading, and industrial operations.",
        "features": [
            ("Loading & Unloading", "Trained workers for safe and efficient loading and unloading of containers, trucks, and warehouses."),
            ("Material Handling", "Experienced labour for in-plant material movement, stacking, sorting, and inventory management."),
            ("Port & CFS Labour", "Specialized workforce experienced in port operations, Container Freight Stations, and JNPT procedures."),
            ("Long-Term Contracts", "We offer long-term labour supply contracts with consistent teams for ongoing industrial operations."),
            ("Safety Compliance", "All our labour is trained in workplace safety, PPE usage, and follows industry safety standards."),
            ("Flexible Deployment", "Labour available for day shifts, night shifts, and weekend assignments to match your operational schedule."),
        ],
    },
    {
        "file": "service-tempo.html",
        "title": "Tempo Transport Services",
        "bg": "images/background/4.webp",
        "img": "images/misc/s3.webp",
        "desc": "Our tempo transport services provide fast and flexible small-to-medium cargo movement across Navi Mumbai, Mumbai, Pune, and throughout Maharashtra. Ideal for smaller consignments, partial loads, and time-sensitive deliveries where a full truck is not required.",
        "tagline": "Fast and flexible tempo services for small consignments across Navi Mumbai and Maharashtra.",
        "features": [
            ("Small Consignment Specialists", "Tempos handle loads that don't require a full truck, offering cost-effective transport for smaller shipments."),
            ("Fast Turnaround", "Lighter vehicles navigate city traffic faster, ensuring quicker pickup and delivery for urgent consignments."),
            ("Navi Mumbai Coverage", "Extensive coverage across Navi Mumbai including Turbhe, Vashi, Panvel, Nerul, Belapur MIDC zones."),
            ("Multiple Sizes", "Mini trucks, Tata Ace, Bolero pickups, and medium tempos available to match your exact cargo size."),
            ("Daily Scheduled Runs", "Regular daily routes between major industrial areas for reliable scheduled deliveries."),
            ("Door-to-Door Service", "Pick up from your door and deliver to the recipient's location without additional handling."),
        ],
    },
    {
        "file": "service-close-body-truck.html",
        "title": "Close Body Truck Services",
        "bg": "images/background/4.webp",
        "img": "images/misc/s3.webp",
        "desc": "Our close body trucks provide fully enclosed, weather-protected transport for cargo that requires protection from dust, rain, and environmental exposure. Ideal for textiles, pharmaceuticals, electronics, packaged goods, and any cargo sensitive to weather or contamination.",
        "tagline": "Fully enclosed trucks for weather-sensitive and contamination-prone cargo across Maharashtra.",
        "features": [
            ("Fully Enclosed Body", "Close body trucks protect cargo from rain, dust, sunlight, and environmental exposure during transit."),
            ("Weather-Sensitive Cargo", "Ideal for textiles, pharmaceuticals, FMCG, electronics, and any goods that must arrive clean and dry."),
            ("Contamination Prevention", "Enclosed design prevents cargo contamination from road dust, diesel fumes, and external elements."),
            ("Multiple Tonnages", "Available from 1 tonne to 20+ tonne capacity to suit cargo volumes of all sizes."),
            ("Secure Loading", "Goods are loaded, secured, and sealed inside the enclosed body for tamper-evident delivery."),
            ("Pan-Maharashtra Network", "Close body trucks deployed across Maharashtra including all major MIDC zones, cities, and highways."),
        ],
    },
]

NAV_WITH_DROPDOWN = '''<ul id="mainmenu">
                                    <li><a class="menu-item" href="index.html">Home</a></li>
                                    <li><a class="menu-item" href="about.html">About Us</a></li>
                                    <li>
                                        <a class="menu-item" href="service-single.html">Services</a>
                                        <ul>
                                            <li><a href="service-trucking.html">Trucking</a></li>
                                            <li><a href="service-container-20ft.html">Container Transport (20ft)</a></li>
                                            <li><a href="service-container-40ft.html">Container Transport (40ft)</a></li>
                                            <li><a href="service-side-open-truck.html">Side Open Truck</a></li>
                                            <li><a href="service-odc.html">ODC Consignment</a></li>
                                            <li><a href="service-labour-supply.html">Labour Supply</a></li>
                                            <li><a href="service-tempo.html">Tempo Transport</a></li>
                                            <li><a href="service-close-body-truck.html">Close Body Truck</a></li>
                                        </ul>
                                    </li>
                                    <li><a class="menu-item" href="team.html">Our Team</a></li>
                                    <li><a class="menu-item" href="certifications.html">Certifications</a></li>
                                    <li><a class="menu-item" href="contact.html">Contact</a></li>
                                </ul>'''

OLD_NAV = '''<ul id="mainmenu">
                                    <li><a class="menu-item" href="index.html">Home</a></li>
                                    <li><a class="menu-item" href="about.html">About Us</a></li>
                                    <li><a class="menu-item" href="service-single.html">Services</a></li>
                                    <li><a class="menu-item" href="team.html">Our Team</a></li>
                                    <li><a class="menu-item" href="certifications.html">Certifications</a></li>
                                    <li><a class="menu-item" href="contact.html">Contact</a></li>
                                </ul>'''

FOOTER_SERVICES = '''                                    <ul>
                                        <li><a href="service-trucking.html">Trucking</a></li>
                                        <li><a href="service-container-20ft.html">Container Transport (20ft &amp; 40ft)</a></li>
                                        <li><a href="service-side-open-truck.html">Side Open Truck</a></li>
                                        <li><a href="service-odc.html">ODC Consignment</a></li>
                                        <li><a href="service-labour-supply.html">Labour Supply</a></li>
                                    </ul>'''

OLD_FOOTER_SERVICES = '''                                    <ul>
                                        <li><a href="service-single.html">Trucking</a></li>
                                        <li><a href="service-single.html">Container Transport (20ft &amp; 40ft)</a></li>
                                        <li><a href="service-single.html">Side Open Truck</a></li>
                                        <li><a href="service-single.html">ODC Consignment</a></li>
                                        <li><a href="service-single.html">Labour Supply</a></li>
                                    </ul>'''

OVERLAY_SERVICES_NEW = '''            <ul class="ul-check">
                <li><a href="service-trucking.html" style="color:inherit">Trucking</a></li>
                <li><a href="service-container-20ft.html" style="color:inherit">Container Transport (20ft)</a></li>
                <li><a href="service-container-40ft.html" style="color:inherit">Container Transport (40ft)</a></li>
                <li><a href="service-side-open-truck.html" style="color:inherit">Side Open Truck</a></li>
                <li><a href="service-odc.html" style="color:inherit">ODC Consignment</a></li>
                <li><a href="service-labour-supply.html" style="color:inherit">Labour Supply</a></li>
                <li><a href="service-tempo.html" style="color:inherit">Tempo Transport</a></li>
                <li><a href="service-close-body-truck.html" style="color:inherit">Close Body Truck</a></li>
            </ul>'''

OLD_OVERLAY_SERVICES = '''            <ul class="ul-check">
                <li>Trucking</li>
                <li>Container Transport (20ft &amp; 40ft)</li>
                <li>Side Open Truck</li>
                <li>ODC Consignment</li>
                <li>Labour Supply</li>
                <li>Import Container Handling</li>
            </ul>'''


def sidebar(active_file):
    items = [
        ("service-trucking.html", "Trucking"),
        ("service-container-20ft.html", "Container Transport (20ft)"),
        ("service-container-40ft.html", "Container Transport (40ft)"),
        ("service-side-open-truck.html", "Side Open Truck"),
        ("service-odc.html", "ODC Consignment"),
        ("service-labour-supply.html", "Labour Supply"),
        ("service-tempo.html", "Tempo Transport"),
        ("service-close-body-truck.html", "Close Body Truck"),
    ]
    html = ""
    for f, label in items:
        if f == active_file:
            html += f'                                <a href="{f}" class="bg-color text-light d-block p-3 px-4 rounded-10px mb-3 relative"><h5 class="mb-0">{label}</h5></a>\n'
        else:
            html += f'                                <a href="{f}" class="bg-light d-block p-3 px-4 rounded-10px mb-3"><h5 class="mb-0">{label}</h5></a>\n'
    return html.rstrip('\n')


def features_html(features):
    rows = ""
    for title, desc in features:
        rows += f"""
                                <div class="col-lg-6 wow fadeInUp">
                                    <div class="relative">
                                        <i class="abs fs-40 p-4 bg-dark icon_check rounded-1 text-light"></i>
                                        <div class="ps-100 ms-4">
                                            <h4>{title}</h4>
                                            <p>{desc}</p>
                                        </div>
                                    </div>
                                </div>"""
    return rows


def make_page(svc):
    nav = NAV_WITH_DROPDOWN
    footer_svc = FOOTER_SERVICES
    overlay_svc = OVERLAY_SERVICES_NEW
    page = f"""<!DOCTYPE html>
<html lang="en">

<head>
    <title>Gavhane Syndicate Transport - Road Transport Contractors, Navi Mumbai</title>
    <link rel="icon" href="images/Logos/Favicon logo.png" type="image/gif" sizes="16x16">
    <meta content="text/html;charset=utf-8" http-equiv="Content-Type">
    <meta content="width=device-width, initial-scale=1.0" name="viewport" >
    <meta content="Gavhane Syndicate Transport - Road Transport Contractors, Navi Mumbai" name="description" >
    <meta content="" name="keywords">
    <meta content="" name="author">
    <!-- CSS Files
    ================================================== -->
    <link href="css/bootstrap.min.css" rel="stylesheet" type="text/css" id="bootstrap">
    <link href="css/plugins.css" rel="stylesheet" type="text/css" >
    <link href="css/swiper.css" rel="stylesheet" type="text/css" >
    <link href="css/style.css" rel="stylesheet" type="text/css" >
    <link href="css/coloring.css" rel="stylesheet" type="text/css" >
    <!-- color scheme -->
    <link id="colors" href="css/colors/scheme-01.css" rel="stylesheet" type="text/css" >

</head>

<body>
    <div id="wrapper">
        <a href="#" id="back-to-top"></a>

        <!-- page preloader begin -->
        <div id="de-loader"></div>
        <!-- page preloader close -->

        <!-- header begin -->
        <header class="header-static transparent mt-lg-4 pt-lg-2">
            <div class="container">
                <div class="row">
                    <div class="col-md-12">
                        <div class="de-flex sm-pt10">
                            <div class="de-flex-col">
                                <!-- logo begin -->
                                <div id="logo">
                                    <a href="index.html">
                                        <img class="logo-main" src="images/Logos/GST Logo (1).png" alt="" >
                                        <img class="logo-scroll" src="images/Logos/GST Logo (1).png" alt="" >
                                        <img class="logo-mobile" src="images/Logos/GST Logo (1).png" alt="" >
                                    </a>
                                </div>
                                <!-- logo end -->
                            </div>
                            <div class="de-flex-col header-col-mid">
                                <!-- mainemenu begin -->
                                {nav}
                                <!-- mainmenu end -->
                            </div>
                            <div class="de-flex-col">
                                <div class="menu_side_area">
                                    <a href="contact.html" class="btn-main btn-line fx-slide"><span>Contact Us</span></a>
                                    <span id="menu-btn"></span>
                                </div>

                                <div id="btn-extra">
                                    <span></span>
                                    <span></span>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </header>
        <!-- header close -->
        <!-- content begin -->
        <div class="no-bottom no-top" id="content">

            <div id="top"></div>

            <section id="subheader" class="text-light sm-mt-90 relative rounded-1 overflow-hidden m-3" data-bgimage="url({svc['bg']}) center">
                <div class="container relative z-2">
                    <div class="row gy-4 gx-5 align-items-center">
                        <div class="col-lg-12">
                            <h1 class="split">{svc['title']}</h1>
                            <ul class="crumb wow fadeInUp">
                                <li><a href="index.html">Home</a></li>
                                <li><a href="service-single.html">Services</a></li>
                                <li class="active">{svc['title']}</li>
                            </ul>
                        </div>
                    </div>
                </div>
                <div class="gradient-edge-bottom color op-7 h-80"></div>
                <div class="sw-overlay op-7"></div>
            </section>

            <section>
                <div class="container">
                    <div class="row g-4 gx-5">
                        <div class="col-lg-3">
                            <div class="me-lg-3">
{sidebar(svc['file'])}
                            </div>
                        </div>

                        <div class="col-lg-9">
                            <div class="row g-4 gx-5">

                                <div class="col-lg-6">
                                    <h2 class="split">{svc['title']}</h2>
                                    <p class="wow fadeInRight" data-wow-delay=".5s">{svc['desc']}</p>
                                </div>

                                <div class="col-lg-6">
                                    <div class="relative">
                                        <img src="{svc['img']}" class="img-fluid rounded-1 wow fadeInUp" alt="">
                                        <div class="bg-color text-light p-4 abs m-4 bottom-0 rounded-1 sm-hide">
                                            <div class="row g-4 align-items-center">
                                                <div class="col-lg-12">
                                                    <p class="no-bottom">{svc['tagline']}</p>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>

                            </div>

                            <div class="spacer-double"></div>
                            <h2>Key Features</h2>

                            <div class="row g-4">{features_html(svc['features'])}
                            </div>

                        </div>
                    </div>
                </div>
            </section>

            <section class="bg-color text-light pt-50 pb-50">
                <div class="container">
                    <div class="row g-4">
                        <div class="col-md-9">
                            <h3 class="mb-0 fs-32 split">Ready to Move Your Cargo Across Maharashtra?</h3>
                        </div>
                        <div class="col-lg-3 text-lg-end">
                            <a class="btn-main fx-slide btn-line wow fadeInRight" data-wow-delay=".2s" href="contact.html"><span>Contact Us</span></a>
                        </div>
                    </div>
                </div>
            </section>

        </div>
        <!-- content close -->

        <!-- footer begin -->
        <footer class="text-light section-dark">
            <div class="container">
                <div class="row g-4 justify-content-between">
                    <div class="col-md-6">
                        <img src="images/Logos/GST Logo (1).png" class="w-170px mb-2" alt="">
                        <div class="spacer-single"></div>
                        <div class="row g-4">
                            <div class="col-md-6">
                                <div class="widget">
                                    <h5>Services</h5>
{footer_svc}
                                </div>
                            </div>

                            <div class="col-md-6">
                                <div class="widget">
                                    <h5>Company</h5>
                                    <ul>
                                        <li><a href="index.html">Home</a></li>
                                        <li><a href="about.html">About Us</a></li>
                                        <li><a href="team.html">Our Team</a></li>
                                        <li><a href="certifications.html">Certifications</a></li>
                                        <li><a href="contact.html">Contact</a></li>
                                    </ul>
                                </div>
                            </div>
                        </div>


                        <div class="social-icons mb-sm-30 text-center">
                            <a href="#"><i class="fa-brands fa-facebook-f"></i></a>
                            <a href="#"><i class="fa-brands fa-x-twitter"></i></a>
                            <a href="#"><i class="fa-brands fa-instagram"></i></a>
                            <a href="#"><i class="fa-brands fa-youtube"></i></a>
                            <a href="#"><i class="fa-brands fa-whatsapp"></i></a>
                        </div>
                    </div>

                    <div class="col-md-6">
                        <div class="d-flex align-items-center justify-content-between">
                            <h2>Get in Touch</h2>
                            <img src="images/ui/up-right-arrow.webp" class="w-60px op-5" alt="">
                        </div>

                        <div class="widget">
                            <div class="op-5 fs-15">Email</div>
                            <h3>gavhane.transport@gmail.com</h3>

                            <div class="spacer-20"></div>

                            <div class="op-5 fs-15">Phone</div>
                            <h3>9967912409 / 9594777755</h3>

                            <div class="spacer-20"></div>

                            <div class="op-5 fs-15">Office Location</div>
                            <h3>B-618, City Mall, Mayuresh Trade Center, Plot No. 4, Sector-19A, Turbhe, Navi Mumbai - 400703</h3>

                            <div class="spacer-20"></div>

                        </div>
                    </div>
                </div>
            </div>
            <div class="subfooter">
                <div class="container">
                    <div class="row">
                        <div class="col-md-12 text-center">
                            Copyright 2025 Gavhane Syndicate Transport
                        </div>
                    </div>
                </div>
            </div>
        </footer>
        <!-- footer close -->
    </div>

    <!-- overlay content begin -->
    <div id="extra-wrap" class="text-light">
        <div id="btn-close">
            <span></span>
            <span></span>
        </div>

        <div id="extra-content">
            <img src="images/Logos/GST Logo (1).png" class="w-200px" alt="">

            <div class="spacer-30-line"></div>

            <h5>Our Services</h5>
{overlay_svc}

            <div class="spacer-30-line"></div>

            <h5>Contact Us</h5>
            <div><i class="icofont-phone me-2 op-5"></i>9967912409 / 9594777755</div>
            <div><i class="icofont-location-pin me-2 op-5"></i>B-618, City Mall, Mayuresh Trade Center, Plot No. 4, Sector-19A, Turbhe, Navi Mumbai - 400703 </div>
            <div><i class="icofont-envelope me-2 op-5"></i>gavhane.transport@gmail.com</div>

            <div class="spacer-30-line"></div>

            <h5>About Us</h5>
            <p>Gavhane Syndicate Transport is a road transport organization with 28 fleets, covering a wide network across Maharashtra. Specialists in 20ft &amp; 40ft container handling, ODC consignment, and labour supply.</p>

            <div class="social-icons">
                <a href="#"><i class="fa-brands fa-facebook-f"></i></a>
                <a href="#"><i class="fa-brands fa-x-twitter"></i></a>
                <a href="#"><i class="fa-brands fa-instagram"></i></a>
                <a href="#"><i class="fa-brands fa-youtube"></i></a>
                <a href="#"><i class="fa-brands fa-whatsapp"></i></a>
            </div>
        </div>
    </div>
    <!-- overlay content end -->

    <!-- Javascript Files
    ================================================== -->
    <script src="js/plugins.js"></script>
    <script src="js/designesia.js"></script>
    <script src="js/swiper.js"></script>
    <script src="js/custom-swiper-1.js"></script>

</body>

</html>"""
    return page


# Create all 8 service pages
for svc in SERVICES:
    path = os.path.join(BASE, svc["file"])
    with open(path, "w", encoding="utf-8") as f:
        f.write(make_page(svc))
    print(f"Created: {svc['file']}")

# Update navigation and footer in existing 6 pages
existing_pages = ["index.html", "about.html", "service-single.html", "team.html", "certifications.html", "contact.html"]

for page in existing_pages:
    path = os.path.join(BASE, page)
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    changed = False

    # Update navigation
    if OLD_NAV in content:
        content = content.replace(OLD_NAV, NAV_WITH_DROPDOWN)
        print(f"Updated nav in: {page}")
        changed = True
    else:
        print(f"WARNING: nav not found in {page}")

    # Update footer service links
    if OLD_FOOTER_SERVICES in content:
        content = content.replace(OLD_FOOTER_SERVICES, FOOTER_SERVICES)
        print(f"Updated footer services in: {page}")
        changed = True
    else:
        print(f"WARNING: footer services not found in {page}")

    # Update overlay services
    if OLD_OVERLAY_SERVICES in content:
        content = content.replace(OLD_OVERLAY_SERVICES, OVERLAY_SERVICES_NEW)
        print(f"Updated overlay services in: {page}")
        changed = True
    else:
        print(f"WARNING: overlay services not found in {page}")

    if changed:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

print("\nDone! All service pages created and existing pages updated.")
