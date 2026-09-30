// Plume — vitrine : la démonstration de la capsule et l'apparition au défilement.
(function () {
  var demo = document.querySelector("[data-demo]");
  if (demo) {
    var apres = demo.querySelector(".apres");
    var pastilles = demo.querySelectorAll("[data-persona]");
    var bouton = demo.querySelector(".reformuler");
    var textes = JSON.parse(demo.getAttribute("data-textes"));
    var courant = pastilles[0].getAttribute("data-persona");
    pastilles.forEach(function (p) {
      p.addEventListener("click", function () {
        pastilles.forEach(function (q) { q.setAttribute("aria-pressed", "false"); });
        p.setAttribute("aria-pressed", "true");
        courant = p.getAttribute("data-persona");
        if (demo.classList.contains("reecrit")) apres.textContent = textes[courant];
      });
    });
    bouton.addEventListener("click", function () {
      if (demo.classList.contains("reecrit")) {
        demo.classList.remove("reecrit");
        bouton.setAttribute("aria-pressed", "false");
      } else {
        apres.textContent = textes[courant];
        demo.classList.add("reecrit");
        bouton.setAttribute("aria-pressed", "true");
      }
    });
  }
  var blocs = document.querySelectorAll(".apparait");
  if (!("IntersectionObserver" in window)) {
    blocs.forEach(function (b) { b.classList.add("vu"); });
    return;
  }
  var obs = new IntersectionObserver(function (entrees) {
    entrees.forEach(function (e) {
      if (e.isIntersecting) { e.target.classList.add("vu"); obs.unobserve(e.target); }
    });
  }, { threshold: 0.12 });
  blocs.forEach(function (b) { obs.observe(b); });
})();
