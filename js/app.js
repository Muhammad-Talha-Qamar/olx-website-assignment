(function () {
  function qs(sel, root) { return (root || document).querySelector(sel); }
  function qsa(sel, root) { return [...(root || document).querySelectorAll(sel)]; }
  function params() { return new URLSearchParams(location.search); }
  function favs() { return JSON.parse(localStorage.getItem("olx_favs") || "[]"); }
  function setFavs(v) { localStorage.setItem("olx_favs", JSON.stringify(v)); }
  function user() { return JSON.parse(localStorage.getItem("olx_user") || "null"); }

  window.olxCard = function (ad) {
    var saved = favs().includes(ad.id);
    return '<a class="card" href="ad.html?id=' + ad.id + '">' +
      '<img src="' + ad.img + '" alt="">' +
      '<div class="card-body">' +
      '<div class="card-top"><h3>' + ad.priceLabel + '</h3>' +
      '<button class="fav' + (saved ? ' saved' : '') + '" data-id="' + ad.id + '" aria-label="Save"><i class="fa-' + (saved ? 'solid' : 'regular') + ' fa-heart"></i></button></div>' +
      '<p class="title">' + ad.title + '</p>' +
      (ad.extra ? '<p class="meta">' + ad.extra + '</p>' : '') +
      '<p class="loc">' + ad.location + '</p>' +
      '<p class="time">' + ad.time + '</p></div></a>';
  };

  window.olxRender = function (target, list) {
    var el = qs(target);
    if (!el) return;
    el.innerHTML = list.length ? list.map(olxCard).join("") : '<p>No ads found.</p>';
  };

  document.addEventListener("click", function (e) {
    var btn = e.target.closest(".fav");
    if (!btn) return;
    e.preventDefault();
    e.stopPropagation();
    var id = btn.getAttribute("data-id");
    var list = favs();
    if (list.includes(id)) list = list.filter(function (x) { return x !== id; });
    else list.push(id);
    setFavs(list);
    btn.classList.toggle("saved", list.includes(id));
    var icon = btn.querySelector("i");
    if (icon) icon.className = list.includes(id) ? "fa-solid fa-heart" : "fa-regular fa-heart";
  });

  qsa("form.search-bar").forEach(function (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var q = (form.querySelector('input[name="q"]') || {}).value || "";
      var loc = (form.querySelector('[name="location"]') || {}).value || "Pakistan";
      location.href = "listings.html?q=" + encodeURIComponent(q) + "&location=" + encodeURIComponent(loc);
    });
  });

  var loginSlot = qs("[data-login]");
  if (loginSlot && user()) {
    loginSlot.innerHTML = '<a class="login-link" href="account.html">' + (user().name || "My account") + '</a>';
  }

  var cookie = qs("#cookie");
  if (cookie && !localStorage.getItem("olx_cookie")) cookie.classList.add("show");
  var ok = qs("#cookie-ok");
  if (ok) ok.addEventListener("click", function () {
    localStorage.setItem("olx_cookie", "1");
    cookie.classList.remove("show");
  });

  var p = params();
  if (qs("#listing-grid")) {
    var cat = p.get("cat") || "";
    var q = (p.get("q") || "").toLowerCase();
    var loc = (p.get("location") || "").toLowerCase();
    var list = OLX_ADS.filter(function (ad) {
      var okCat = !cat || ad.category === cat;
      var okQ = !q || (ad.title + ad.desc + ad.category).toLowerCase().includes(q);
      var okLoc = !loc || loc === "pakistan" || ad.location.toLowerCase().includes(loc);
      return okCat && okQ && okLoc;
    });
    var title = qs("#results-title");
    if (title) title.textContent = (cat ? cat : q ? q : "All ads") + " in " + (p.get("location") || "Pakistan");
    olxRender("#listing-grid", list);
    var ff = qs("#filter-form");
    if (ff) ff.addEventListener("submit", function (e) {
      e.preventDefault();
      var min = Number(qs("#min").value || 0);
      var max = Number(qs("#max").value || 1e12);
      var sort = qs("#sort").value;
      var filtered = list.filter(function (ad) { return ad.price >= min && ad.price <= max; });
      if (sort === "low") filtered.sort(function (a, b) { return a.price - b.price; });
      if (sort === "high") filtered.sort(function (a, b) { return b.price - a.price; });
      olxRender("#listing-grid", filtered);
    });
  }

  if (qs("#ad-page")) {
    var ad = OLX_ADS.find(function (x) { return x.id === p.get("id"); }) || OLX_ADS[0];
    qs("#ad-title").textContent = ad.title;
    qs("#ad-price").textContent = ad.priceLabel;
    qs("#ad-loc").textContent = ad.location + " · " + ad.time;
    qs("#ad-desc").textContent = ad.desc;
    qs("#ad-seller").textContent = ad.seller;
    qs("#ad-member").textContent = ad.member;
    var main = qs("#main-photo");
    main.src = ad.images[0];
    qs("#thumbs").innerHTML = ad.images.map(function (src, i) {
      return '<img class="' + (i === 0 ? "active" : "") + '" src="' + src + '">';
    }).join("");
    qsa("#thumbs img").forEach(function (img) {
      img.addEventListener("click", function () {
        qsa("#thumbs img").forEach(function (x) { x.classList.remove("active"); });
        img.classList.add("active");
        main.src = img.src;
      });
    });
    var related = OLX_ADS.filter(function (x) { return x.category === ad.category && x.id !== ad.id; }).slice(0, 4);
    olxRender("#related", related);
    qs("#chat-btn").href = "chat.html?with=" + encodeURIComponent(ad.seller);
  }

  if (qs("#fav-grid")) {
    olxRender("#fav-grid", OLX_ADS.filter(function (ad) { return favs().includes(ad.id); }));
  }

  var loginForm = qs("#login-form");
  if (loginForm) loginForm.addEventListener("submit", function (e) {
    e.preventDefault();
    var err = qs(".error");
    if (!qs("#agree-terms").checked || !qs("#agree-privacy").checked) {
      err.style.display = "block";
      err.textContent = "Please accept the Terms of Use and Privacy Policy to continue.";
      return;
    }
    localStorage.setItem("olx_user", JSON.stringify({ name: qs("#ident").value || "User", phone: qs("#ident").value }));
    location.href = "account.html";
  });

  var signupForm = qs("#signup-form");
  if (signupForm) signupForm.addEventListener("submit", function (e) {
    e.preventDefault();
    var err = qs(".error");
    if (!qs("#agree-terms").checked || !qs("#agree-privacy").checked || !qs("#agree-rules").checked) {
      err.style.display = "block";
      err.textContent = "All agreements must be accepted before creating an account.";
      return;
    }
    localStorage.setItem("olx_user", JSON.stringify({ name: qs("#name").value, phone: qs("#phone").value }));
    location.href = "account.html";
  });

  var sellForm = qs("#sell-form");
  if (sellForm) sellForm.addEventListener("submit", function (e) {
    e.preventDefault();
    var err = qs(".error");
    if (!qs("#agree-terms").checked || !qs("#agree-rules").checked || !qs("#agree-legal").checked) {
      err.style.display = "block";
      err.textContent = "You must accept posting rules, terms, and confirm the item is legal in Pakistan.";
      return;
    }
    qs("#posted").style.display = "block";
    sellForm.reset();
  });

  var contactForm = qs("#contact-form");
  if (contactForm) contactForm.addEventListener("submit", function (e) {
    e.preventDefault();
    qs("#posted").style.display = "block";
  });

  var chatSend = qs("#chat-send");
  if (chatSend) chatSend.addEventListener("click", function () {
    var input = qs("#chat-text");
    if (!input.value.trim()) return;
    var log = qs(".chat-log");
    var b = document.createElement("div");
    b.className = "bubble me";
    b.textContent = input.value;
    log.appendChild(b);
    input.value = "";
  });
})();
