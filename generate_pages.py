from pathlib import Path
ROOT = Path(__file__).resolve().parent

HEAD = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css">
<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css">
<script src="js/data.js"></script>
<script src="js/app.js" defer></script>
</head>
<body>
'''

HEADER = '''
<header class="site-header">
  <div class="header-inner wrap">
    <a class="logo" href="index.html" aria-label="OLX"><span class="logo-o">o</span><span class="logo-bar"></span><span class="logo-x">x</span></a>
    <a class="header-link" href="motors.html"><img src="images/car.png" alt=""><span>Motors</span></a>
    <a class="header-link" href="property.html"><img src="images/property.png" alt=""><span>Property</span></a>
    <div class="header-actions">
      <a class="icon-btn" href="chat.html" aria-label="Chat"><i class="fa-regular fa-comment"></i></a>
      <a class="icon-btn" href="favorites.html" aria-label="Favorites"><i class="fa-regular fa-heart"></i></a>
      <span data-login><a class="login-link" href="login.html">Login</a></span>
      <a class="sell-btn" href="sell.html"><span>+</span> SELL</a>
    </div>
  </div>
  <form class="search-bar wrap">
    <div class="location-field">
      <i class="fa-solid fa-location-dot"></i>
      <input name="location" value="Pakistan" placeholder="Location" aria-label="Location">
      <i class="fa-solid fa-chevron-down"></i>
    </div>
    <div class="query-field">
      <input type="search" name="q" placeholder="Find Cars, Mobile Phones and more..." aria-label="Search">
      <button class="search-btn" type="submit"><i class="fa-solid fa-magnifying-glass"></i> Search</button>
    </div>
  </form>
</header>
<nav class="cat-nav">
  <div class="cat-nav-inner wrap">
    <div class="all-cats">
      <a href="categories.html">All Categories <i class="fa-solid fa-chevron-down"></i></a>
      <div class="all-cats-menu">
        <a href="listings.html?cat=mobiles">Mobiles</a>
        <a href="listings.html?cat=cars">Vehicles</a>
        <a href="listings.html?cat=houses">Property for Sale</a>
        <a href="listings.html?cat=bikes">Bikes</a>
        <a href="listings.html?cat=electronics">Electronics</a>
        <a href="listings.html?cat=jobs">Jobs</a>
        <a href="listings.html?cat=plots">Land & Plots</a>
        <a href="listings.html?cat=tablets">Tablets</a>
      </div>
    </div>
    <a href="listings.html?cat=mobiles">Mobile Phones</a>
    <a href="listings.html?cat=cars">Cars</a>
    <a href="listings.html?cat=bikes">Motorcycles</a>
    <a href="listings.html?cat=houses">Houses</a>
    <a href="listings.html?cat=electronics">Video-Audios</a>
    <a href="listings.html?cat=tablets">Tablets</a>
    <a href="listings.html?cat=plots">Land & Plots</a>
  </div>
</nav>
'''

FOOTER = '''
<section class="app-banner">
  <div class="app-copy">
    <h2>Find amazing deals on the go.</h2>
    <p>Download OLX app now!</p>
  </div>
  <div class="phones-art"><img src="images/app-phones.png" alt="OLX app"></div>
  <div class="store-btns">
    <a href="https://apps.apple.com/">App Store</a>
    <a href="https://play.google.com/">Google Play</a>
    <a href="https://appgallery.huawei.com/">AppGallery</a>
  </div>
</section>
<footer class="site-footer">
  <div class="footer-cols wrap">
    <div><h4>Popular Categories</h4>
      <a href="listings.html?cat=cars">Cars</a>
      <a href="property.html">Flats for rent</a>
      <a href="listings.html?cat=mobiles">Mobile Phones</a>
      <a href="listings.html?cat=jobs">Jobs</a></div>
    <div><h4>Trending Searches</h4>
      <a href="listings.html?cat=bikes">Bikes</a>
      <a href="listings.html?q=watches">Watches</a>
      <a href="listings.html?q=books">Books</a>
      <a href="listings.html?q=dogs">Dogs</a></div>
    <div><h4>About Us</h4>
      <a href="blog.html">OLX Blog</a>
      <a href="contact.html">Contact Us</a>
      <a href="business.html">OLX for Businesses</a>
      <a href="about.html">About OLX</a></div>
    <div><h4>OLX</h4>
      <a href="help.html">Help</a>
      <a href="sitemap.html">Sitemap</a>
      <a href="terms.html">Terms of use</a>
      <a href="privacy.html">Privacy Policy</a>
      <a href="cookies.html">Cookie Policy</a>
      <a href="seller-terms.html">Seller Terms</a></div>
    <div><h4>Follow Us</h4>
      <div class="socials">
        <a href="#" aria-label="X"><i class="fa-brands fa-x-twitter"></i></a>
        <a href="#" aria-label="Facebook"><i class="fa-brands fa-facebook-f"></i></a>
        <a href="#" aria-label="YouTube"><i class="fa-brands fa-youtube"></i></a>
        <a href="#" aria-label="Instagram"><i class="fa-brands fa-instagram"></i></a>
      </div></div>
  </div>
  <div class="footer-bottom">Classifieds in Pakistan. © 2006–2026 OLX</div>
</footer>
<div class="cookie" id="cookie">
  <span>We use cookies to keep this classroom clone working. See the <a href="cookies.html">Cookie Policy</a> and <a href="privacy.html">Privacy Policy</a>.</span>
  <button id="cookie-ok" type="button">Accept</button>
</div>
</body></html>
'''

def page(name, title, body, header=True, footer=True):
    html = HEAD.format(title=title)
    if header:
        html += HEADER
    html += body
    if footer:
        html += FOOTER
    else:
        html += '<div class="cookie" id="cookie"><span>We use cookies. <a href="cookies.html">Cookie Policy</a></span><button id="cookie-ok" type="button">Accept</button></div></body></html>'
    (ROOT / name).write_text(html, encoding="utf-8")
    print("wrote", name)

LEGAL_NOTE = '''<div class="note">This is a student assignment clone of the OLX Pakistan layout. These terms are original classroom wording covering the same topics as a classifieds site. They are not OLX’s official legal documents.</div>'''

pages = {}

pages["index.html"] = ("OLX - Buy and Sell for free anywhere in Pakistan", '''
<main>
  <section class="hero wrap"><img src="images/pic1.webp" alt="Featured banner"></section>
  <section class="categories wrap" id="home-cats"></section>
  <section class="listings wrap">
    <div class="section-head"><h2>Mobile Phones</h2><a href="listings.html?cat=mobiles">View More</a></div>
    <div class="cards" id="home-phones"></div>
  </section>
  <section class="listings wrap">
    <div class="section-head"><h2>Cars</h2><a href="listings.html?cat=cars">View More</a></div>
    <div class="cards" id="home-cars"></div>
  </section>
  <section class="listings wrap">
    <div class="section-head"><h2>Bikes & Motorcycles</h2><a href="listings.html?cat=bikes">View More</a></div>
    <div class="cards" id="home-bikes"></div>
  </section>
  <section class="listings wrap">
    <div class="section-head"><h2>Houses</h2><a href="listings.html?cat=houses">View More</a></div>
    <div class="cards" id="home-houses"></div>
  </section>
</main>
<script>
document.addEventListener("DOMContentLoaded", function(){
  document.getElementById("home-cats").innerHTML = OLX_CATS.map(c =>
    '<a class="cat-item" href="listings.html?cat='+c.id+'"><span class="cat-icon" style="background:#f2f4f5">'+c.icon+'</span><span>'+c.name+'</span></a>'
  ).join("");
  olxRender("#home-phones", OLX_ADS.filter(a=>a.category==="mobiles").slice(0,4));
  olxRender("#home-cars", OLX_ADS.filter(a=>a.category==="cars").slice(0,4));
  olxRender("#home-bikes", OLX_ADS.filter(a=>a.category==="bikes").slice(0,4));
  olxRender("#home-houses", OLX_ADS.filter(a=>a.category==="houses").slice(0,4));
});
</script>
''')

pages["listings.html"] = ("Ads | OLX Pakistan", '''
<main class="page wrap">
  <p class="crumbs"><a href="index.html">Home</a> / Ads</p>
  <div class="layout">
    <aside class="filters">
      <h3>Filters</h3>
      <form id="filter-form">
        <label>Sort</label>
        <select id="sort">
          <option value="new">Newly listed</option>
          <option value="low">Price: low to high</option>
          <option value="high">Price: high to low</option>
        </select>
        <label>Min price</label><input id="min" type="number" placeholder="0">
        <label>Max price</label><input id="max" type="number" placeholder="Any">
        <button class="filter-btn" type="submit">Apply</button>
      </form>
    </aside>
    <div>
      <div class="results-head"><h2 id="results-title">All ads</h2></div>
      <div class="cards" id="listing-grid"></div>
    </div>
  </div>
</main>
''')

pages["ad.html"] = ("Ad details | OLX", '''
<main class="page wrap" id="ad-page">
  <p class="crumbs"><a href="index.html">Home</a> / Ad</p>
  <div class="ad-grid">
    <div>
      <div class="gallery">
        <img id="main-photo" class="main-photo" alt="Ad photo">
        <div class="thumbs" id="thumbs"></div>
      </div>
      <div class="desc">
        <h2>Description</h2>
        <p id="ad-desc"></p>
      </div>
    </div>
    <aside>
      <div class="seller-card">
        <p class="price-lg" id="ad-price"></p>
        <h1 id="ad-title"></h1>
        <p class="meta" id="ad-loc"></p>
        <div class="action-row">
          <a class="btn btn-dark" id="chat-btn" href="chat.html">Chat</a>
          <a class="btn btn-blue" href="login.html">Show phone</a>
        </div>
      </div>
      <div class="seller-card">
        <h3 id="ad-seller"></h3>
        <p class="meta" id="ad-member"></p>
        <a class="btn btn-outline" href="safety.html">Safety tips</a>
      </div>
      <div class="safe-card">
        <strong>Stay safe</strong>
        <p class="meta">Meet in public, never pay a deposit to a stranger, and read the <a href="safety.html">safety guide</a>.</p>
      </div>
    </aside>
  </div>
  <section class="listings" style="padding-top:28px">
    <div class="section-head"><h2>Related ads</h2></div>
    <div class="cards" id="related"></div>
  </section>
</main>
''')

pages["categories.html"] = ("All Categories | OLX", '''
<main class="page wrap">
  <h1>All Categories</h1>
  <section class="categories" id="all-cats-page"></section>
</main>
<script>
document.addEventListener("DOMContentLoaded", function(){
  document.getElementById("all-cats-page").innerHTML = OLX_CATS.map(c =>
    '<a class="cat-item" href="listings.html?cat='+c.id+'"><span class="cat-icon" style="background:#f2f4f5">'+c.icon+'</span><span>'+c.name+'</span></a>'
  ).join("");
});
</script>
''')

pages["motors.html"] = ("Motors | OLX", '''
<main>
  <section class="hero wrap"><img src="images/pic1.webp" alt="Motors"></section>
  <section class="listings wrap">
    <div class="section-head"><h2>Cars</h2><a href="listings.html?cat=cars">View More</a></div>
    <div class="cards" id="m-cars"></div>
  </section>
  <section class="listings wrap">
    <div class="section-head"><h2>Bikes</h2><a href="listings.html?cat=bikes">View More</a></div>
    <div class="cards" id="m-bikes"></div>
  </section>
</main>
<script>
document.addEventListener("DOMContentLoaded", function(){
  olxRender("#m-cars", OLX_ADS.filter(a=>a.category==="cars"));
  olxRender("#m-bikes", OLX_ADS.filter(a=>a.category==="bikes"));
});
</script>
''')

pages["property.html"] = ("Property | OLX", '''
<main>
  <section class="listings wrap" style="padding-top:28px">
    <div class="section-head"><h2>Houses</h2><a href="listings.html?cat=houses">View More</a></div>
    <div class="cards" id="p-houses"></div>
  </section>
  <section class="listings wrap">
    <div class="section-head"><h2>Land & Plots</h2><a href="listings.html?cat=plots">View More</a></div>
    <div class="cards" id="p-plots"></div>
  </section>
</main>
<script>
document.addEventListener("DOMContentLoaded", function(){
  olxRender("#p-houses", OLX_ADS.filter(a=>a.category==="houses"));
  olxRender("#p-plots", OLX_ADS.filter(a=>a.category==="plots"));
});
</script>
''')

pages["login.html"] = ("Login | OLX", '''
<main class="auth-wrap">
  <h1>Welcome to OLX</h1>
  <p class="sub">The trusted community of buyers and sellers.</p>
  <form id="login-form">
    <div class="field"><label>Phone number or email</label><input id="ident" required placeholder="03xx or email"></div>
    <label class="check"><input id="agree-terms" type="checkbox"> I agree to the <a href="terms.html">Terms of Use</a></label>
    <label class="check"><input id="agree-privacy" type="checkbox"> I agree to the <a href="privacy.html">Privacy Policy</a> and <a href="cookies.html">Cookie Policy</a></label>
    <p class="error"></p>
    <button class="btn btn-dark" type="submit" style="width:100%">Continue</button>
  </form>
  <p class="meta" style="margin-top:14px">New here? <a href="signup.html">Create an account</a></p>
</main>
''')

pages["signup.html"] = ("Create account | OLX", '''
<main class="auth-wrap">
  <h1>Create your account</h1>
  <p class="sub">Join the classifieds community. You must accept the agreements below.</p>
  <form id="signup-form">
    <div class="field"><label>Full name</label><input id="name" required></div>
    <div class="field"><label>Phone</label><input id="phone" required placeholder="03xx-xxxxxxx"></div>
    <div class="field"><label>Email</label><input type="email" required></div>
    <div class="field"><label>Password</label><input type="password" required minlength="6"></div>
    <label class="check"><input id="agree-terms" type="checkbox"> I have read and agree to the <a href="terms.html">Terms of Use</a></label>
    <label class="check"><input id="agree-privacy" type="checkbox"> I agree to the <a href="privacy.html">Privacy Policy</a></label>
    <label class="check"><input id="agree-rules" type="checkbox"> I agree to the <a href="rules.html">Posting Rules</a> and <a href="community.html">Community Guidelines</a></label>
    <p class="error"></p>
    <button class="btn btn-dark" type="submit" style="width:100%">Create account</button>
  </form>
</main>
''')

pages["sell.html"] = ("Post an ad | OLX", '''
<main class="page wrap form-wide">
  <div class="steps"><span class="on">1. Category</span><span class="on">2. Details</span><span class="on">3. Agreements</span></div>
  <h1>Post your ad</h1>
  <p class="sub">Free ads stay live for 30 days if they follow posting rules.</p>
  <form id="sell-form">
    <div class="field"><label>Category</label>
      <select required>
        <option value="">Choose</option>
        <option>Mobiles</option><option>Cars</option><option>Bikes</option>
        <option>Houses</option><option>Plots</option><option>Electronics</option>
        <option>Jobs</option><option>Services</option>
      </select></div>
    <div class="field"><label>Title</label><input required maxlength="70" placeholder="Keep it short and clear"></div>
    <div class="field"><label>Description</label><textarea rows="5" required maxlength="4096"></textarea></div>
    <div class="field"><label>Price (PKR)</label><input type="number" required min="1"></div>
    <div class="field"><label>Location in Pakistan</label><input required placeholder="City / area"></div>
    <div class="field"><label>Photo URL or file name</label><input placeholder="images/pic2.webp"></div>
    <h2 style="margin-top:18px">Required agreements</h2>
    <label class="check"><input id="agree-terms" type="checkbox"> I agree to the <a href="terms.html">Terms of Use</a> and <a href="seller-terms.html">Seller Platform Terms</a></label>
    <label class="check"><input id="agree-rules" type="checkbox"> I have read the <a href="rules.html">Posting Rules</a>, <a href="prohibited.html">Prohibited Items</a>, and <a href="ad-limits.html">Free Ad Limits</a></label>
    <label class="check"><input id="agree-legal" type="checkbox"> I confirm this offer is legal in Pakistan, uses a Pakistani location/phone, and is not a duplicate or competitor ad</label>
    <p class="error"></p>
    <div class="success" id="posted">Your ad was saved locally for this assignment. In a live site it would be reviewed against posting rules.</div>
    <button class="btn btn-dark" type="submit">Post now</button>
  </form>
</main>
''')

pages["account.html"] = ("My account | OLX", '''
<main class="page wrap">
  <div class="profile">
    <aside class="side-nav">
      <a class="active" href="account.html">Profile</a>
      <a href="my-ads.html">My ads</a>
      <a href="favorites.html">Favourites</a>
      <a href="chat.html">Chat</a>
      <a href="help.html">Help</a>
    </aside>
    <section>
      <h1>My account</h1>
      <p class="meta">Manage your profile, ads, and saved items.</p>
      <div class="seller-card" style="margin-top:16px">
        <h3>Profile</h3>
        <p>Name and phone are stored in this browser only.</p>
        <a class="btn btn-outline" href="login.html">Switch account</a>
      </div>
    </section>
  </div>
</main>
''')

pages["my-ads.html"] = ("My ads | OLX", '''
<main class="page wrap">
  <h1>My ads</h1>
  <p class="meta">Posted ads appear here after you use Sell. Sample public ads are shown below.</p>
  <div class="cards" id="home-phones"></div>
</main>
<script>document.addEventListener("DOMContentLoaded", function(){ olxRender("#home-phones", OLX_ADS.slice(0,4)); });</script>
''')

pages["favorites.html"] = ("Favourites | OLX", '''
<main class="page wrap">
  <h1>Favourites</h1>
  <div class="cards" id="fav-grid"></div>
</main>
''')

pages["chat.html"] = ("Chat | OLX", '''
<main class="page wrap">
  <h1>Chat</h1>
  <div class="chat-layout">
    <div class="chat-list">
      <a class="active" href="#">Ali Khan · iPhone listing</a>
      <a href="#">Auto House · Civic</a>
      <a href="#">Property Plus · House</a>
    </div>
    <div class="chat-pane">
      <div class="chat-log">
        <div class="bubble">Is this still available?</div>
        <div class="bubble me">Yes, we can meet in a public place.</div>
      </div>
      <div class="chat-input">
        <input id="chat-text" placeholder="Type a message">
        <button class="btn btn-dark" id="chat-send" type="button">Send</button>
      </div>
    </div>
  </div>
  <p class="meta" style="margin-top:12px">Never share OTPs or make advance payments. See <a href="safety.html">safety tips</a>.</p>
</main>
''')

pages["help.html"] = ("Help Center | OLX", '''
<div class="help-hero">
  <h1>HOW CAN WE HELP YOU?</h1>
  <input placeholder="Search">
</div>
<main class="wrap">
  <div class="help-grid">
    <a class="help-card" href="about.html"><h3>Important Updates</h3><p>Classroom clone notes and how this assignment site is structured.</p></a>
    <a class="help-card" href="featured.html"><h3>Ad of the Week</h3><p>How featured placement and Ad of the Week style boosts work.</p></a>
    <a class="help-card" href="seller-terms.html"><h3>Seller Platform Terms</h3><p>Terms and conditions related to posting and seller tools.</p></a>
    <a class="help-card" href="safety.html"><h3>Safety</h3><p>Safety measures for buying and selling in person.</p></a>
    <a class="help-card" href="privacy.html"><h3>Legal & Privacy</h3><p>Privacy Policy, Cookie Policy, and Terms of Use.</p></a>
    <a class="help-card" href="featured.html"><h3>Featured Ads & Business Packages</h3><p>Paid visibility options for sellers and shops.</p></a>
    <a class="help-card" href="ad-limits.html"><h3>Free Ad Limits</h3><p>How many free ads you can post and how long they stay live.</p></a>
    <a class="help-card" href="featured.html"><h3>Boost to Top</h3><p>Move an ad higher in its category for a limited time.</p></a>
    <a class="help-card" href="account.html"><h3>My Account / Profile</h3><p>Create, edit, and protect your account.</p></a>
    <a class="help-card" href="rules.html"><h3>Posting and Managing Ads</h3><p>How to post, edit, hide a number, and why ads are rejected.</p></a>
    <a class="help-card" href="business.html"><h3>Payments & Invoices</h3><p>Billing for featured ads in this assignment demo.</p></a>
    <a class="help-card" href="chat.html"><h3>Chat</h3><p>Message other users from an ad page.</p></a>
    <a class="help-card" href="safety.html"><h3>How do I buy on OLX?</h3><p>Search, chat, meet, and inspect before you pay.</p></a>
    <a class="help-card" href="contact.html"><h3>About Us / Contact</h3><p>Contact details for this assignment site.</p></a>
    <a class="help-card" href="prohibited.html"><h3>Prohibited items</h3><p>What you cannot list on the platform.</p></a>
  </div>
</main>
''')

def legal(title, inner):
    return f'<main class="page wrap legal"><h1>{title}</h1>{LEGAL_NOTE}{inner}</main>'

pages["terms.html"] = ("Terms of Use | OLX", legal("Terms of Use", '''
<p>Last updated: 21 September 2026.</p>
<p>By creating an account, posting content, or using this classifieds website, you enter a binding agreement with the operator of this assignment site (“we”, “the Service”). If you do not agree, do not use the Service.</p>
<h2>1. The Service</h2>
<p>The Service is an online notice board that lets people in Pakistan publish offers and contact each other. We are not a party to any sale, rental, job, or service contract between users. We do not inspect items, hold money in escrow, or guarantee that a listing is accurate.</p>
<h2>2. Eligibility</h2>
<p>You must be able to form a contract under Pakistan law. You may keep only one account per phone number. Accounts created from foreign IPs, or ads that advertise foreign numbers or delivery from outside Pakistan, are not allowed.</p>
<h2>3. Your content</h2>
<p>You are solely responsible for photos, titles, prices, and descriptions you upload. You confirm that you own or have permission to publish that content, that it does not infringe copyright or privacy, and that you grant us a licence to host, display, and moderate it so the Service can function.</p>
<h2>4. Posting rules</h2>
<p>Ads must follow the <a href="rules.html">Posting Rules</a> and <a href="prohibited.html">Prohibited Items</a> list. An ad that complies may stay live for 30 days. Repeating the same ad after deletion before that period ends is not allowed. We may refuse, edit, or remove content that breaks these terms, including competitor ads and multi-product dumps.</p>
<h2>5. Featured ads</h2>
<p>Paid placement such as Featured Ads or Boost to Top is optional, described in the <a href="featured.html">Featured Ads</a> page, and fees are non-refundable once delivery starts, except where required by law.</p>
<h2>6. Acceptable use</h2>
<p>Do not scrape the site, attack our systems, impersonate others, harvest personal data, or use the Service to commit fraud. We may suspend accounts that create a safety or legal risk.</p>
<h2>7. Liability</h2>
<p>The Service is provided as-is for a class assignment. We are not liable for deals that go wrong between users. You agree to meet in public, inspect goods, and follow the <a href="safety.html">Safety Tips</a>.</p>
<h2>8. Changes</h2>
<p>We may update these terms. Continued use after a notice on this page means you accept the new version.</p>
'''))

pages["privacy.html"] = ("Privacy Policy | OLX", legal("Privacy Policy", '''
<p>This policy explains what we collect in this classroom clone and why.</p>
<h2>Information we collect</h2>
<ul>
<li>Account details you type: name, phone, email, password (stored in your browser for this demo).</li>
<li>Listing details: title, price, location, photos, description.</li>
<li>Usage data: search terms, saved ads, cookie consent, and pages visited on this site.</li>
</ul>
<h2>How we use it</h2>
<p>To show ads near a location you choose, to keep you logged in, to send transactional notices (ad live, ad expired) that you cannot opt out of if the real product required them, and to measure which banners are viewed.</p>
<h2>Public information</h2>
<p>When you post an ad, other users may see your first name, city, and, if you reveal it, your phone number. Anything you share in chat can be copied by the other person.</p>
<h2>Sharing</h2>
<p>We do not sell personal data. A live product may share non-identifiable analytics with advertising partners as described in the <a href="cookies.html">Cookie Policy</a>.</p>
<h2>Your rights</h2>
<p>You may ask to access or delete demo data by clearing your browser storage or contacting the address on the <a href="contact.html">Contact</a> page.</p>
'''))

pages["cookies.html"] = ("Cookie Policy | OLX", legal("Cookie Policy", '''
<p>Cookies and similar storage keep you logged in, remember favourite ads, and store whether you accepted this banner.</p>
<ul>
<li><strong>Essential:</strong> login state, cookie consent, form progress.</li>
<li><strong>Preferences:</strong> location field, language.</li>
<li><strong>Analytics (typical live site):</strong> anonymous counts of visits.</li>
</ul>
<p>You can refuse non-essential cookies in your browser. Blocking essential cookies will stop login and posting from working.</p>
'''))

pages["seller-terms.html"] = ("Seller Platform Terms | OLX", legal("Terms and Conditions for Seller Platform", '''
<p>These terms apply if you use posting tools, seller dashboard, featured ads, or business packages.</p>
<h2>Seller duties</h2>
<p>You must describe the item honestly, set a real price, use your own photos, and complete or withdraw the ad when the item is sold. You must not use another person’s identity documents.</p>
<h2>Quality and review</h2>
<p>Ads may stay pending until they pass automated or manual checks. Reasons for rejection include invalid price, multiple products in one ad, prohibited items, and copyrighted images.</p>
<h2>Fees</h2>
<p>Free limits are in <a href="ad-limits.html">Free Ad Limits</a>. Extra visibility is paid and governed by <a href="featured.html">Featured Ads & Business Packages</a>.</p>
<h2>Suspension</h2>
<p>Repeated rule breaks can remove posting rights. You remain responsible for deals started while your ads were live.</p>
'''))

pages["rules.html"] = ("Posting Rules | OLX", legal("Rules of OLX / Posting guidelines", '''
<ul>
<li><strong>Local posting:</strong> Offers must be in Pakistan. Foreign IPs and foreign numbers are not permitted. One account, one phone number.</li>
<li><strong>Ad duration:</strong> A compliant ad stays active for 30 days. You may not repost the same ad after deletion until that window ends.</li>
<li><strong>Legal goods:</strong> Only items and services allowed under Pakistan law.</li>
<li><strong>One product per ad:</strong> Bundles that look like a shop dump may be rejected as “multiple products”.</li>
<li><strong>Price:</strong> Use a realistic PKR price. “0”, fake, or clickbait prices can be rejected.</li>
<li><strong>Photos:</strong> Up to 12 photos in a live product; this demo accepts one path. No stolen brand catalogues.</li>
<li><strong>Competitors:</strong> Ads promoting other classifieds platforms are not allowed.</li>
<li>How to post: choose a category, add title, description, price, location, photos, accept agreements, then Post now.</li>
</ul>
<p>Related: <a href="prohibited.html">Prohibited items</a> · <a href="ad-limits.html">Free ad limits</a> · <a href="sell.html">Post an ad</a></p>
'''))

pages["prohibited.html"] = ("Prohibited items | OLX", legal("Which items are not allowed", '''
<p>You may not list anything illegal in Pakistan or that creates a safety risk, including (examples for this assignment):</p>
<ul>
<li>Weapons, explosives, and related accessories</li>
<li>Drugs, stolen goods, counterfeit currency or documents</li>
<li>Prescription medicines and medical devices that require a licence</li>
<li>Counterfeit branded goods presented as genuine</li>
<li>Live wildlife protected by law</li>
<li>Adult sexual services or exploitative content</li>
<li>Ads that request advance fees for fake jobs</li>
</ul>
<p>If we believe an ad is unlawful, we may remove it and, where required, report it.</p>
'''))

pages["safety.html"] = ("Safety Tips | OLX", legal("Safety tips", '''
<h2>Tips for a safe transaction</h2>
<ul>
<li>Chat on the site first. Do not move to unknown payment apps because someone rushed you.</li>
<li>Meet in a public, well-lit place. Take a friend to vehicle and property visits.</li>
<li>Inspect the item and documents before paying. For cars, check registration and physical condition.</li>
<li>Never send a deposit, gift-card code, or OTP to someone you have not met.</li>
<li>Jobs that ask you to pay for a kit or “registration” are usually fraud.</li>
</ul>
<h2>How do I know if it’s a fraud?</h2>
<p>Warning signs include prices far below market, sellers who will not meet, requests to pay a courier in advance, and stories about being abroad.</p>
<h2>Report</h2>
<p>Use <a href="contact.html">Contact Us</a> to report an ad. Include the ad title and why it looks unsafe.</p>
'''))

pages["community.html"] = ("Community Guidelines | OLX", legal("Community guidelines", '''
<p>Be respectful in chat and ads. No hate speech, harassment, or discrimination. Do not post another person’s private data. Users who report problems in good faith help keep the community usable.</p>
'''))

pages["featured.html"] = ("Featured Ads | OLX", legal("Featured Ads, Boost to Top & Ad of the Week", '''
<p>Featured Ads place a listing in selected spots on the homepage or category pages for a paid period. Boost to Top moves an ad higher in search for a short window. Ad of the Week is a curated slot.</p>
<p>Fees in a live product are charged through a payment provider and are typically non-refundable after the boost starts. This assignment does not process real payments.</p>
'''))

pages["ad-limits.html"] = ("Free Ad Limits | OLX", legal("Free Ad Limits", '''
<p>Free users can keep a limited number of live ads at once (for this demo: unlimited locally, 30-day duration in the story of the product). Extra ads or extra cities may require a business package. After 30 days an ad expires and can be posted again if it still follows the rules.</p>
'''))

pages["about.html"] = ("About | OLX", legal("About this OLX assignment", '''
<p>This website copies the look of OLX Pakistan for a class project: header, search, categories, listings, ad details, sell flow, account, chat, help centre, and legal agreements.</p>
<p>It is not affiliated with OLX. Listings and phone numbers are sample data.</p>
'''))

pages["contact.html"] = ("Contact Us | OLX", '''
<main class="page wrap form-wide">
  <h1>Contact Us</h1>
  <p class="meta">For this assignment, messages stay in the browser.</p>
  <form id="contact-form">
    <div class="field"><label>Name</label><input required></div>
    <div class="field"><label>Email</label><input type="email" required></div>
    <div class="field"><label>Topic</label>
      <select><option>Report an ad</option><option>Account help</option><option>Safety</option><option>Legal</option></select>
    </div>
    <div class="field"><label>Message</label><textarea rows="5" required></textarea></div>
    <div class="success" id="posted">Thanks. Your message was recorded locally.</div>
    <button class="btn btn-dark" type="submit">Send</button>
  </form>
</main>
''')

pages["blog.html"] = ("OLX Blog", '''
<main class="page wrap">
  <h1>OLX Blog</h1>
  <a class="help-card" href="blog-post.html" style="display:block;margin-top:16px">
    <h3>How to write a listing that sells</h3>
    <p>Use a clear title, real photos, and a fair price — then keep chat replies fast.</p>
  </a>
  <a class="help-card" href="safety.html" style="display:block;margin-top:16px">
    <h3>Stay safe when you buy a used car</h3>
    <p>Documents, test drives, and meeting in public.</p>
  </a>
</main>
''')

pages["blog-post.html"] = ("How to write a listing | Blog", legal("How to write a listing that sells", '''
<p>Lead with the brand and model. Add the one detail buyers search for (storage, mileage, marla). Take photos in daylight. State what is included. Reply to chat the same day.</p>
'''))

pages["business.html"] = ("OLX for Businesses", legal("OLX for Businesses", '''
<p>Shops and dealers can use business packages for more live ads, featured placement, and a shop-style presence. Payments and invoices on a live product would appear in the seller dashboard. This demo has no real billing.</p>
<p>See also <a href="seller-terms.html">Seller Platform Terms</a>.</p>
'''))

pages["sitemap.html"] = ("Sitemap | OLX", '''
<main class="page wrap legal">
  <h1>Sitemap</h1>
  <h2>Marketplace</h2>
  <ul>
    <li><a href="index.html">Home</a></li>
    <li><a href="categories.html">All categories</a></li>
    <li><a href="motors.html">Motors</a></li>
    <li><a href="property.html">Property</a></li>
    <li><a href="listings.html">All ads</a></li>
    <li><a href="sell.html">Post an ad</a></li>
  </ul>
  <h2>Account</h2>
  <ul>
    <li><a href="login.html">Login</a></li>
    <li><a href="signup.html">Sign up</a></li>
    <li><a href="account.html">My account</a></li>
    <li><a href="my-ads.html">My ads</a></li>
    <li><a href="favorites.html">Favourites</a></li>
    <li><a href="chat.html">Chat</a></li>
  </ul>
  <h2>Help & agreements</h2>
  <ul>
    <li><a href="help.html">Help centre</a></li>
    <li><a href="terms.html">Terms of Use</a></li>
    <li><a href="privacy.html">Privacy Policy</a></li>
    <li><a href="cookies.html">Cookie Policy</a></li>
    <li><a href="seller-terms.html">Seller Platform Terms</a></li>
    <li><a href="rules.html">Posting rules</a></li>
    <li><a href="prohibited.html">Prohibited items</a></li>
    <li><a href="safety.html">Safety tips</a></li>
    <li><a href="community.html">Community guidelines</a></li>
    <li><a href="featured.html">Featured ads</a></li>
    <li><a href="ad-limits.html">Free ad limits</a></li>
    <li><a href="contact.html">Contact</a></li>
    <li><a href="about.html">About</a></li>
    <li><a href="blog.html">Blog</a></li>
    <li><a href="business.html">OLX for Businesses</a></li>
  </ul>
</main>
''')

for name, (title, body) in pages.items():
    page(name, title, body)

# keep root style.css pointing at new css for old links
(ROOT / "style.css").write_text('@import url("css/style.css");\n', encoding="utf-8")
print("done", len(pages), "pages")
