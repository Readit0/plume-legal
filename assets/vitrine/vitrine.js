// Plume — vitrine : la capsule (états de CapsuleOverlay.kt : repos → travail → succès),
// le choix de persona, les règles par app, la Lecture assistée, les moteurs.
(function () {
  "use strict";
  var reduit = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  // ─── La capsule ───
  var scene = document.querySelector("[data-scene]");
  if (scene) {
    var textes = JSON.parse(scene.getAttribute("data-textes"));
    var champ = scene.querySelector(".champ");
    var pilule = scene.querySelector(".pilule");
    var nom = pilule.querySelector(".nom");
    var avatar = pilule.querySelector("img");
    var choix = scene.querySelectorAll("[data-persona]");
    var courant = choix[0];
    var reecrit = false, occupe = false;
    var poser = function (t) {
      champ.classList.add("fondu");
      setTimeout(function () { champ.textContent = t; champ.classList.remove("fondu"); }, reduit ? 0 : 180);
    };
    var libelle = function () { nom.textContent = courant.getAttribute("data-nom"); };
    choix.forEach(function (b) {
      b.addEventListener("click", function () {
        choix.forEach(function (c) { c.setAttribute("aria-pressed", "false"); });
        b.setAttribute("aria-pressed", "true");
        courant = b;
        avatar.src = b.querySelector("img").src;
        libelle();
        if (reecrit) poser(textes[b.getAttribute("data-persona")]);
      });
    });
    pilule.addEventListener("click", function () {
      if (occupe) return;
      if (reecrit) { reecrit = false; poser(textes.brouillon); return; }
      occupe = true;
      pilule.classList.add("travail");
      setTimeout(function () {
        pilule.classList.remove("travail");
        poser(textes[courant.getAttribute("data-persona")]);
        reecrit = true;
        pilule.classList.add("succes");
        nom.textContent = textes.reecrit;
        setTimeout(function () { pilule.classList.remove("succes"); libelle(); occupe = false; }, 1300);
      }, reduit ? 0 : 950);
    });
  }

  // ─── Règles par application : les interrupteurs basculent ───
  document.querySelectorAll(".interrupteur").forEach(function (s) {
    s.addEventListener("click", function () {
      s.setAttribute("aria-checked", s.getAttribute("aria-checked") === "true" ? "false" : "true");
    });
  });

  // ─── Lecture assistée : la traduction se pose sur la planche ───
  var lecture = document.querySelector("[data-lecture]");
  if (lecture) {
    var planche = lecture.querySelector(".planche");
    lecture.querySelector(".pilule").addEventListener("click", function () {
      var actif = !planche.classList.contains("traduit");
      planche.classList.toggle("traduit", actif);
      lecture.classList.toggle("traduit-actif", actif);
      this.setAttribute("aria-pressed", actif ? "true" : "false");
    });
  }

  // ─── Les moteurs : un seul choisi à la fois ───
  var moteurs = document.querySelectorAll(".moteur");
  moteurs.forEach(function (m) {
    m.addEventListener("click", function () {
      moteurs.forEach(function (x) { x.setAttribute("aria-pressed", "false"); });
      m.setAttribute("aria-pressed", "true");
    });
  });

  // ─── Apparition au défilement ───
  var blocs = document.querySelectorAll(".apparait");
  if (!("IntersectionObserver" in window)) { blocs.forEach(function (b) { b.classList.add("vu"); }); return; }
  var obs = new IntersectionObserver(function (es) {
    es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add("vu"); obs.unobserve(e.target); } });
  }, { threshold: 0.1 });
  blocs.forEach(function (b) { obs.observe(b); });
})();
