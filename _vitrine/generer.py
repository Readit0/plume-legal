"""Génère la vitrine de Plume dans toutes les langues : python generer.py

Sources :
  _vitrine/textes/<code>.json   les textes du site (fr = source, repli : en)
  app PLUME, lib/l10n/*.arb     noms et descriptions des personas, moteurs, règles — LES MÊMES MOTS QUE L'APP
  app PLUME, lib/l10n/app_languages.dart   le nom de chaque langue, écrit dans sa langue
Sortie : index.html (fr) et <code>/index.html.
"""
import html, json, os, re

ICI = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.dirname(ICI)
APP = r"C:\Users\T470s\Desktop\PLUME"
URL = "https://readit0.github.io/plume-legal/"
PLAY = "https://play.google.com/store/apps/details?id=com.plume.plume"
RTL = {"ar", "fa", "he", "ur"}
# La Lecture assistée n'est PAS active dans l'app (lib/core/feature_flags.dart :
# lectureAssistee = false). Elle ne se montre pas sur le site tant qu'elle ne
# l'est pas : passer à True le jour où elle s'active, puis relancer ce script.
AFFICHER_LECTURE = False
# Le nom d'une langue créée d'exemple, sur la capsule (avec son emblème).
LANGUE_EXEMPLE = "Nylo"
PHRASE_INVENTEE = "Ōvi tēla sā dūmin mōra kē ?"

CODES = ["fr"] + sorted(
    d for d in os.listdir(SITE)
    if os.path.isdir(os.path.join(SITE, d)) and os.path.exists(os.path.join(SITE, d, "politique-confidentialite.md"))
)

# ─── le nom de chaque langue, dans sa langue (lib/l10n/app_languages.dart) ───
src = open(os.path.join(APP, "lib", "l10n", "app_languages.dart"), encoding="utf-8").read()
NOMS = {}
for code, nom in re.findall(r"\('([a-zA-Z-]+)',\s*'([^']+)'\)", src):
    NOMS.setdefault(code, nom)
NOMS["fr"] = "Français"
for c in CODES:
    NOMS.setdefault(c, c)


def charger_arb(code):
    for nom in (code, code.split("-")[0]):
        p = os.path.join(APP, "lib", "l10n", f"app_{nom}.arb")
        if os.path.exists(p):
            return json.load(open(p, encoding="utf-8"))
    return {}


ARB_EN = charger_arb("en")
# langue → pays du drapeau (kLanguageFlagCountry de l'app) ; None = pas de drapeau, comme l'app
DRAPEAUX = json.load(open(os.path.join(ICI, "drapeaux.json"), encoding="utf-8"))
DRAPEAUX.setdefault("en", "us")


def nom_pastille(code):
    """Le libellé de la capsule : nom natif sans variante, 10 caractères au plus
    (TranslatorMode.libellePastille + PersonaStore.nomDeBaseLangue)."""
    nom = NOMS.get(code, code)
    i = nom.find(" (")
    return (nom if i <= 0 else nom[:i]).strip()[:10]


# Les répliques entre guillemets d'un texte de l'app, dans toutes les écritures.
GUILLEMETS = [("«", "»"), ("»", "«"), ("“", "”"), ("„", "“"), ("„", "”"), ('"', '"'), ("「", "」"),
              ("『", "』"), ("‘", "’"), ("‚", "‘"), ("״", "״"), ("‹", "›"), ("《", "》"), ("”", "”")]


def repliques(texte):
    """Les deux premières citations du texte, lues de GAUCHE À DROITE : chaque
    citation est consommée entière avant de chercher la suivante — sinon le mot
    ENTRE deux citations (« devient ») passerait pour une citation."""
    fermants = {}
    for a, b in GUILLEMETS:
        fermants.setdefault(a, []).append(b)
    out, i = [], 0
    while i < len(texte) and len(out) < 2:
        ch = texte[i]
        if ch in fermants:
            fins = [texte.find(b, i + 1) for b in fermants[ch]]
            fins = [j for j in fins if j > i + 1]
            if fins:
                j = min(fins)
                seg = texte[i + 1:j].strip()
                if 2 <= len(seg) <= 120:
                    out.append(seg)
                i = j + 1
                continue
        i += 1
    return out if len(out) == 2 else None
TXT_EN = json.load(open(os.path.join(ICI, "textes", "en.json"), encoding="utf-8"))

GRATUITES = [
    ("direct", "gratuit_base__direct", "styleDirect", "personaDescDirect"),
    ("pro", "gratuit_base__professionnel", "styleProfessional", "personaDescProfessionnel"),
    ("complice", "gratuit_base__complice", "styleFriendly", "personaDescComplice"),
    ("concis", "gratuit_base__concis", "styleConcise", "personaDescConcis"),
    ("romantique", "gratuit_base__romantique", "styleRomantic", "personaDescRomantique"),
]
EXPERTISE = [
    ("expertise_metier_s1__diplomate", "personaDiplomate", "personaDescDiplomate"),
    ("expertise_metier_s1__service_client", "personaServiceClient", "personaDescServiceClient"),
    ("expertise_metier_s1__artisan_devis", "personaArtisanDevis", "personaDescArtisanDevis"),
    ("expertise_metier_s1__n_gociateur_calme", "personaNegociateurCalme", "personaDescNegociateurCalme"),
    ("expertise_metier_s1__annonce_vente", "personaAnnonceVente", "personaDescAnnonceVente"),
]
CREATIVITE = [
    ("creativite_style_s1__litt_raire_soutenu", "personaLitteraireSoutenu", "personaDescLitteraireSoutenu"),
    ("creativite_style_s1__r_partie_esprit", "personaReparteeEsprit", "personaDescReparteeEsprit"),
    ("creativite_style_s1__chevaleresque", "personaChevaleresque", "personaDescChevaleresque"),
    ("creativite_style_s1__po_tique", "personaPoetique", "personaDescPoetique"),
    ("creativite_style_s1__t_n_breux_l_gant", "personaTenebreuxElegant", "personaDescTenebreuxElegant"),
    ("creativite_style_s1__minimaliste", "personaMinimaliste", "personaDescMinimaliste"),
    ("creativite_style_s1__interpr_tation", "personaInterpretation", "personaDescInterpretation"),
]

GLOBE = '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"/><ellipse cx="12" cy="12" rx="4.2" ry="9"/><path d="M3 12h18"/></svg>'
MICRO = '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="9" y="3" width="6" height="11" rx="3"/><path d="M6 11a6 6 0 0 0 12 0M12 17v4"/></svg>'
PLAY_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M5 3.5v17a1 1 0 0 0 1.5.86l14-8.5a1 1 0 0 0 0-1.72l-14-8.5A1 1 0 0 0 5 3.5Z"/></svg>'


def page(code):
    txt = json.load(open(os.path.join(ICI, "textes", f"{code}.json"), encoding="utf-8")) \
        if os.path.exists(os.path.join(ICI, "textes", f"{code}.json")) else {}
    arb = charger_arb(code)
    pre = "" if code == "fr" else "../"
    img = pre + "assets/vitrine/"

    def T(k):  # texte du site, échappé ; *x* → accent dégradé
        v = html.escape(txt.get(k) or TXT_EN[k], quote=False)
        return re.sub(r"\*(.+?)\*", r'<span class="degrade">\1</span>', v)

    def A(k):  # texte de L'APP (arb), échappé
        return html.escape(arb.get(k) or ARB_EN.get(k) or k, quote=False)

    def attr(s):
        return html.escape(s, quote=True)

    brut = lambda k: txt.get(k) or TXT_EN[k]
    demo = {p: brut(f"demo_{'pro' if p == 'pro' else p}") for p, *_ in GRATUITES}
    demo["brouillon"] = brut("demo_brouillon")
    demo["reecrit"] = brut("demo_reecrit")

    choix = "".join(
        f'<button type="button" data-persona="{p}" data-nom="{attr(arb.get(n) or ARB_EN.get(n))}" aria-pressed="{"true" if i == 0 else "false"}">'
        f'<img src="{img}personas/{f}.webp" alt="" width="24" height="24">{A(n)}</button>'
        for i, (p, f, n, _) in enumerate(GRATUITES)
    )

    def cintre(f, n, d):
        return (f'<article class="persona"><img src="{img}personas/{f}.webp" alt="" width="56" height="56" loading="lazy">'
                f'<div><b>{A(n)}</b><p>{A(d)}</p></div></article>')

    offertes = "".join(cintre(f, n, d) for _, f, n, d in GRATUITES)
    expertise = "".join(cintre(f, n, d) for f, n, d in EXPERTISE)
    creativite = "".join(cintre(f, n, d) for f, n, d in CREATIVITE)

    langues = "".join(
        f'<li><a href="{pre}{"" if c == "fr" else c + "/"}" hreflang="{c}" lang="{c}"'
        f'{" aria-current=\"page\"" if c == code else ""}>{html.escape(NOMS[c])}</a></li>'
        for c in sorted(CODES, key=lambda c: NOMS[c].lower())
    )
    alternates = "".join(
        f'\n  <link rel="alternate" hreflang="{c}" href="{URL}{"" if c == "fr" else c + "/"}">' for c in CODES
    ) + f'\n  <link rel="alternate" hreflang="x-default" href="{URL}en/">'

    # La bande de langues de la capsule : drapeau + nom natif, comme l'app (HF-481).
    def moitie(c, cible=False):
        pays = DRAPEAUX.get(c)
        drap = f'<img src="{img}drapeaux/{pays}.webp" alt="" height="12">' if pays else ""
        return f'<span{" class=\"cible\"" if cible else ""}>{drap}{html.escape(nom_pastille(c))}</span>'

    autre = "fr" if code == "en" else "en"
    segment = f'<span class="segment">{moitie(code, True)}{moitie(autre)}</span>'
    segment_langue = (f'<span class="segment">{moitie(code)}<span class="cible"><img class="embleme" '
                      f'src="{img}embleme-langue.webp" alt="" height="14">{html.escape(LANGUE_EXEMPLE)}</span></span>')
    camo = repliques(arb.get("camoExpGesteTapCorps") or "") or repliques(ARB_EN.get("camoExpGesteTapCorps", ""))
    lecture_nav = f'\n        <a href="#lecture">{T("nav_lecture")}</a>' if AFFICHER_LECTURE else ""
    autorisations = T("autorisations_texte") if AFFICHER_LECTURE else T("autorisations_sans_lecture")
    # la planche : des répliques de manga en japonais (en coréen sur la page japonaise)
    orig1, orig2 = ("기다려! 나 두고 가지 마!", "같이 가자.") if code == "ja" else ("待って！置いていかないで！", "一緒に行こう。")
    initiale = html.escape((brut("demo_contact") or "?")[0].upper())
    canon = URL + ("" if code == "fr" else code + "/")

    sortie = f"""---
layout: null
---
{{% raw %}}<!DOCTYPE html>
<html lang="{code}" dir="{"rtl" if code in RTL else "ltr"}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(brut("meta_title"))}</title>
  <meta name="description" content="{attr(brut("meta_description"))}">
  <meta name="theme-color" content="#0E1116">
  <link rel="canonical" href="{canon}">{alternates}
  <meta property="og:title" content="{attr(brut("meta_title"))}">
  <meta property="og:description" content="{attr(brut("meta_description"))}">
  <meta property="og:image" content="{URL}assets/vitrine/partage.jpg">
  <meta property="og:url" content="{canon}">
  <meta property="og:type" content="website">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="icon" type="image/png" sizes="32x32" href="{img}favicon-32.png">
  <link rel="apple-touch-icon" href="{img}icone-192.png">
  <link rel="stylesheet" href="{img}polices/polices.css">
  <link rel="stylesheet" href="{img}vitrine.css">
</head>
<body>
  <a class="saut" href="#contenu">{T("skip")}</a>

  <header class="entete">
    <div class="conteneur">
      <a class="marque" href="./"><img src="{img}icone-192.png" alt="" width="32" height="32">Plume</a>
      <nav class="nav" aria-label="Plume">
        <a href="#geste">{T("nav_geste")}</a>
        <a href="#styles">{T("nav_styles")}</a>
        <a href="#camouflage">{A("capsuleCamouflageLabel")}</a>{lecture_nav}
        <a href="#confidentialite">{T("nav_confidentialite")}</a>
        <details class="langues">
          <summary aria-label="{attr(brut("langues_label"))}">{GLOBE}{html.escape(NOMS[code])}</summary>
          <ul>{langues}</ul>
        </details>
      </nav>
    </div>
  </header>

  <main id="contenu">
    <section class="heros">
      <div class="conteneur">
        <div>
          <span class="surtitre">{T("surtitre")}</span>
          <h1>{T("h1")}</h1>
          <p class="accroche">{T("accroche")}</p>
          <div class="actions">
            <a class="cta" href="{PLAY}">{PLAY_SVG}<span><small>{T("cta_petit")}</small>Google Play</span></a>
            <span class="secondaire">{T("gratuit_court")}</span>
          </div>
        </div>

        <div class="scene" data-scene data-textes="{attr(json.dumps(demo, ensure_ascii=False))}">
          <div class="telephone" role="group" aria-label="{attr(brut("demo_aria"))}">
            <div class="ecran">
              <div class="statut"><span>10:26</span><span>5G<i></i></span></div>
              <div class="fil"><span class="contact">{initiale}</span><div><b>{T("demo_contact")}</b><small>{T("demo_statut")}</small></div></div>
              <div class="messages"><div class="recu">{T("demo_recu")}</div></div>
              <div class="saisie">
                <div class="champ" aria-live="polite">{T("demo_brouillon")}</div>
                <span class="envoyer"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 20.5 21 12 3 3.5 3 10l12 2-12 2z"/></svg></span>
              </div>
              <div class="capsule">
                <div class="bande" aria-hidden="true">
                  <span class="puce-ctrl on">{GLOBE}</span>
                  <span class="puce-ctrl">{MICRO}</span>
                  {segment}
                </div>
                <button type="button" class="pilule" aria-label="{attr(brut("demo_consigne"))}">
                  <img src="{img}personas/gratuit_base__direct.webp" alt="" width="26" height="26">
                  <span class="nom">{A("styleDirect")}</span>
                  <span class="points" aria-hidden="true"><i></i><i></i><i></i></span>
                </button>
              </div>
            </div>
          </div>
          <div class="choix">{choix}</div>
          <p class="consigne">{T("demo_consigne")}</p>
        </div>
      </div>
    </section>

    <section class="bloc" id="geste">
      <div class="conteneur">
        <div class="titre-section apparait"><h2>{T("geste_titre")}</h2><p>{T("geste_intro")}</p></div>
        <div class="grille">
          <article class="carte apparait">
            <div class="vignette" aria-hidden="true"><span class="onde"></span><span class="onde"></span>
              <span class="mini"><img src="{img}personas/gratuit_base__professionnel.webp" alt="">{A("styleProfessional")}</span></div>
            <h3>{T("tap_titre")}</h3><p>{T("tap_texte")}</p>
          </article>
          <article class="carte apparait">
            <div class="vignette long" aria-hidden="true">
              <span class="mini"><img src="{img}personas/gratuit_base__complice.webp" alt="">{A("styleFriendly")}</span>
              <svg class="anneau" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/></svg>
              <div class="suggestion"><b>{T("long_suggestion")}</b><i></i><i></i></div></div>
            <h3>{T("long_titre")}</h3><p>{T("long_texte")}</p>
          </article>
          <article class="carte apparait">
            <div class="vignette" aria-hidden="true"><div class="pile"><span class="micro-rouge">{MICRO}</span>
              <span class="barres"><i></i><i></i><i></i><i></i><i></i></span></div></div>
            <h3>{T("micro_titre")}</h3><p>{T("micro_texte")}</p>
          </article>
        </div>
      </div>
    </section>

    <section class="bloc" id="styles">
      <div class="conteneur">
        <div class="titre-section apparait"><h2>{T("styles_titre")}</h2><p>{T("styles_intro")}</p></div>
        <div class="rayon apparait"><h3>{T("styles_offertes")}</h3><div class="cintres">{offertes}</div></div>
        <div class="rayon apparait"><h3>{A("packExpertiseMetier")} <span>{T("styles_abonnement")}</span></h3><div class="cintres">{expertise}</div></div>
        <div class="rayon apparait"><h3>{A("packCreativiteStyle")} <span>{T("styles_abonnement")}</span></h3><div class="cintres">{creativite}
          <article class="persona tienne"><span class="plus" aria-hidden="true">+</span><div><b>{T("styles_tienne_titre")}</b><p>{T("styles_tienne_texte")}</p></div></article></div></div>
      </div>
    </section>

    <section class="bloc" id="regles">
      <div class="conteneur deux">
        <div class="apparait">
          <div class="titre-section"><h2>{T("regles_titre")}</h2></div>
          <p>{T("regles_texte")}</p>
        </div>
        <div class="appareil apparait">
          <div class="barre-titre">{A("perAppTitle")}</div>
          <div class="entete-section"><span class="liseré"></span>
            <svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/></svg>
            <b>{A("perAppPersonaSection")}</b><span class="plus-rond" aria-hidden="true">+</span></div>
          <p class="sous-titre">{A("perAppPersonaBody")}</p>
          <div class="liste">
            <div class="regle"><span class="app" style="background:linear-gradient(135deg,#30A46C,#22D3EE)"><svg viewBox="0 0 24 24"><path d="M4 5h16v11H9l-5 4z"/></svg></span>
              <div class="txt"><b>{T("regles_app_1")}</b><small>{A("styleFriendly")}</small></div>
              <button type="button" class="interrupteur" role="switch" aria-checked="true" aria-label="{attr(brut("regles_app_1"))}"></button></div>
            <div class="regle"><span class="app" style="background:linear-gradient(135deg,#4C8DFF,#6C6BFF)"><svg viewBox="0 0 24 24"><rect x="3" y="7" width="18" height="13" rx="2"/><path d="M9 7V4h6v3"/></svg></span>
              <div class="txt"><b>{T("regles_app_2")}</b><small>{A("styleProfessional")}</small></div>
              <button type="button" class="interrupteur" role="switch" aria-checked="true" aria-label="{attr(brut("regles_app_2"))}"></button></div>
            <div class="regle"><span class="app" style="background:linear-gradient(135deg,#F59E0B,#EC4899)"><svg viewBox="0 0 24 24"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg></span>
              <div class="txt"><b>{T("regles_app_3")}</b><small>{A("styleConcise")}</small></div>
              <button type="button" class="interrupteur" role="switch" aria-checked="false" aria-label="{attr(brut("regles_app_3"))}"></button></div>
          </div>
          <p class="note-accent">{T("regles_note")}</p>
        </div>
      </div>
    </section>

    <section class="bloc" id="camouflage">
      <div class="conteneur deux">
        <div class="apparait">
          <div class="titre-section"><h2>{A("camoExpTitre")}</h2><p>{A("camoExpSousTitre")}</p></div>
          <div class="points-cles">
            <div><b>{A("camoExpGesteTapTitre")}</b><p>{A("camoExpGesteTapCorps")}</p></div>
            <div><b>{A("camoExpGesteLongTitre")}</b><p>{A("camoExpGesteLongCorps")}</p></div>
            <div><b>{A("camoLexiqueIntroTitre")}</b><p>{A("camoLexiqueIntroDesc")}</p></div>
          </div>
          <p class="avertissement"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 8v5M12 16.5v.5"/></svg><span>{A("camoExpAvertissement")}</span></p>
        </div>
        <div class="apparait">
          <div class="demo-mode camouflage" data-bascule data-a="{attr(camo[0]) if camo else ''}" data-b="{attr(camo[1]) if camo else ''}" data-reussi="{attr(arb.get("capsuleCamouflageLabel") or ARB_EN.get("capsuleCamouflageLabel"))}">
            <div class="fil-mini"><span class="contact">{initiale}</span><b>{T("demo_contact")}</b></div>
            <div class="bulle-envoyee" aria-live="polite">{html.escape(camo[0]) if camo else A("camoExpGesteTapCorps")}</div>
            <div class="capsule statique">
              <div class="bande" aria-hidden="true"><span class="puce-ctrl">{MICRO}</span></div>
              <button type="button" class="pilule violette" aria-label="{attr(arb.get("camoExpGesteTapTitre") or ARB_EN.get("camoExpGesteTapTitre"))}">
                <img src="{img}embleme-camouflage.webp" alt="" width="26" height="26">
                <span class="nom">{A("capsuleCamouflageLabel")}</span>
                <span class="points" aria-hidden="true"><i></i><i></i><i></i></span>
              </button>
            </div>
            <p class="consigne">{A("camoExpGesteTapTitre")}</p>
          </div>
        </div>
      </div>
    </section>

    <section class="bloc" id="langue">
      <div class="conteneur deux">
        <div class="apparait inverse">
          <div class="demo-mode langue" data-bascule data-a="{attr(PHRASE_INVENTEE)}" data-b="{attr(brut("demo_recu"))}" data-reussi="{attr(nom_pastille(code))}">
            <div class="fil-mini"><img class="contact embleme-contact" src="{img}embleme-langue.webp" alt=""><b>{html.escape(LANGUE_EXEMPLE)}</b></div>
            <div class="bulle-recue" aria-live="polite" dir="auto">{html.escape(PHRASE_INVENTEE)}</div>
            <div class="capsule statique">
              <div class="bande" aria-hidden="true"><span class="puce-ctrl on">{GLOBE}</span>{segment_langue}</div>
              <button type="button" class="pilule" aria-label="{attr(arb.get("camoExpGesteLongTitre") or ARB_EN.get("camoExpGesteLongTitre"))}">
                <img src="{img}personas/gratuit_base__direct.webp" alt="" width="26" height="26">
                <span class="nom">{A("styleDirect")}</span>
                <span class="points" aria-hidden="true"><i></i><i></i><i></i></span>
              </button>
            </div>
            <p class="consigne">{A("camoExpGesteLongTitre")}</p>
          </div>
        </div>
        <div class="apparait">
          <div class="titre-section"><h2>{A("langCreateDesc")}</h2><p>{A("langAttendDesc")}</p></div>
          <div class="points-cles">
            <div><b>{A("langImportTitle")}</b><p>{A("langImportDesc")}</p></div>
            <div><b>{A("langFicheRegles")}</b><p>{A("langFicheReglesIntro")}</p></div>
            <div><b>{A("langDefTitre")}</b><p>{A("langDefIntro")}</p></div>
          </div>
        </div>
      </div>
    </section>

<!--LECTURE-->
    <section class="bloc" id="lecture">
      <div class="conteneur deux">
        <div class="planche-cadre apparait inverse" data-lecture>
          <div class="bouton-lecture">
            <button type="button" class="pilule" aria-pressed="false"><span class="pastille-etat"></span><span class="nom">{T("lecture_bouton")} · Cloud AI</span></button>
            <span class="bascule-mode" aria-hidden="true"><span class="actif">IM</span><span>TXT</span></span>
          </div>
          <div class="planche" dir="ltr">
            <svg viewBox="0 0 400 300" aria-hidden="true">
              <defs><pattern id="trame" width="6" height="6" patternUnits="userSpaceOnUse"><circle cx="3" cy="3" r="1.1" fill="#1a1a1a" opacity=".22"/></pattern></defs>
              <rect width="400" height="300" fill="#F2EFE8"/>
              <g stroke="#1a1a1a" stroke-width="1" opacity=".18">{"".join(f'<line x1="400" y1="300" x2="{x}" y2="0"/>' for x in range(0, 420, 22))}</g>
              <rect x="0" y="190" width="400" height="110" fill="url(#trame)"/>
              <path d="M40 300 C40 230 70 200 110 200 C150 200 175 230 178 300Z" fill="#1a1a1a"/>
              <circle cx="110" cy="165" r="38" fill="#fff" stroke="#1a1a1a" stroke-width="4"/>
              <path d="M74 150 C80 118 140 112 148 150 C135 136 92 134 74 150Z" fill="#1a1a1a"/>
              <circle cx="98" cy="170" r="4" fill="#1a1a1a"/><circle cx="124" cy="170" r="4" fill="#1a1a1a"/>
              <path d="M250 300 C252 240 280 222 318 222 C352 222 372 246 372 300Z" fill="#fff" stroke="#1a1a1a" stroke-width="4"/>
              <circle cx="312" cy="190" r="32" fill="#fff" stroke="#1a1a1a" stroke-width="4"/>
              <path d="M280 178 C286 150 336 146 344 180 L344 196 C332 170 296 168 280 196Z" fill="#1a1a1a"/>
              <path d="M300 200 q12 8 24 0" stroke="#1a1a1a" stroke-width="3" fill="none"/>
              <ellipse cx="124" cy="62" rx="112" ry="44" fill="#fff" stroke="#1a1a1a" stroke-width="3"/>
              <path d="M110 104 l6 22 l14 -24z" fill="#fff" stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round"/>
              <text x="124" y="67" text-anchor="middle" font-size="14.5" font-weight="700" fill="#1a1a1a">{html.escape(orig1)}</text>
              <ellipse cx="300" cy="96" rx="80" ry="34" fill="#fff" stroke="#1a1a1a" stroke-width="3"/>
              <path d="M300 128 l4 22 l14 -24z" fill="#fff" stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round"/>
              <text x="300" y="101" text-anchor="middle" font-size="15" font-weight="700" fill="#1a1a1a">{html.escape(orig2)}</text>
            </svg>
            <div class="bulle-trad" style="left:6%;top:12%;width:50%;height:18%" dir="auto">{T("lecture_trad_1")}</div>
            <div class="bulle-trad" style="left:59%;top:24%;width:32%;height:16%" dir="auto">{T("lecture_trad_2")}</div>
          </div>
          <p class="consigne" style="margin-top:12px">{T("lecture_consigne")}</p>
        </div>
        <div class="apparait">
          <div class="titre-section"><h2>{T("lecture_titre")}</h2></div>
          <p>{T("lecture_texte")}</p>
          <p>{T("lecture_langues")}</p>
        </div>
      </div>
    </section>
<!--/LECTURE-->

    <section class="bloc" id="confidentialite">
      <div class="conteneur">
        <div class="titre-section apparait"><h2>{T("conf_titre")}</h2></div>
        <div class="grille">
          <button type="button" class="carte moteur apparait" aria-pressed="false">
            <span class="tete"><span class="ico" style="background:rgba(48,164,108,.14)"><svg viewBox="0 0 24 24" style="stroke:#30A46C"><path d="M13 2 4 14h7l-1 8 9-12h-7z"/></svg></span>
              <span><h3>{A("readingModeLocalTitle")}</h3><span class="etiquette" style="background:rgba(48,164,108,.15);color:#6FD3A0">{T("local_puce")}</span></span></span>
            <p>{T("local_texte")}</p>
          </button>
          <button type="button" class="carte moteur apparait" aria-pressed="true">
            <span class="tete"><span class="ico" style="background:rgba(76,141,255,.14)"><svg viewBox="0 0 24 24" style="stroke:#4C8DFF"><path d="M7 18a5 5 0 0 1-.5-9.97A7 7 0 0 1 20 10a4 4 0 0 1-1 8z"/></svg></span>
              <span><h3>{A("readingModeCloudTitle")}</h3><span class="etiquette" style="background:rgba(76,141,255,.15);color:#8DB6FF">{T("cloud_puce")}</span></span></span>
            <p>{T("cloud_texte")}</p>
          </button>
          <button type="button" class="carte moteur apparait" aria-pressed="false">
            <span class="tete"><span class="ico" style="background:rgba(108,107,255,.14)"><svg viewBox="0 0 24 24" style="stroke:#6C6BFF"><path d="m12 3 1.8 4.6L18 9l-4.2 1.4L12 15l-1.8-4.6L6 9l4.2-1.4z"/><path d="M19 15l.8 2 2 .8-2 .8-.8 2-.8-2-2-.8 2-.8z"/></svg></span>
              <span><h3>{A("readingModeGemmaTitle")}</h3><span class="etiquette" style="background:rgba(108,107,255,.18);color:#A9A8FF">{T("ia_puce")}</span></span></span>
            <p>{T("ia_texte")}</p>
          </button>
        </div>
        <div class="carte autorisations apparait">
          <span class="bouclier"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3 4 6v6c0 5 3.4 8.3 8 9 4.6-.7 8-4 8-9V6z"/><path d="m9 12 2 2 4-4"/></svg></span>
          <div><h3>{T("autorisations_titre")}</h3><p>{autorisations}</p></div>
        </div>
      </div>
    </section>

    <section class="final">
      <div class="conteneur">
        <div class="carte apparait">
          <img src="{img}icone-192.png" alt="" width="72" height="72">
          <h2>{T("final_titre")}</h2>
          <p>{T("final_texte")}</p>
          <a class="cta" href="{PLAY}">{PLAY_SVG}<span><small>{T("cta_petit")}</small>Google Play</span></a>
          <p style="margin:28px 0 0">{T("final_signature")}</p>
        </div>
      </div>
    </section>
  </main>

  <footer class="pied">
    <div class="conteneur">
      <div>© 2026 Plume · {T("pied_contact")} : <a href="mailto:sogacmoi7@gmail.com">sogacmoi7@gmail.com</a>
        <small class="marques" lang="en">Google Play and the Google Play logo are trademarks of Google LLC. Android is a trademark of Google LLC.</small></div>
      <nav aria-label="{attr(brut("legal_toutes"))}">
        <a href="politique-confidentialite">{T("legal_confidentialite")}</a>
        <a href="conditions-generales">{T("legal_cgu")}</a>
        <a href="suppression-compte">{T("legal_suppression")}</a>
        <a href="{pre}informations-legales">{T("legal_toutes")}</a>
      </nav>
    </div>
  </footer>
  <script src="{img}vitrine.js" defer></script>
</body>
</html>{{% endraw %}}
"""
    if not AFFICHER_LECTURE:
        sortie = re.sub(r"<!--LECTURE-->.*?<!--/LECTURE-->\n?", "", sortie, flags=re.S)
    return sortie.replace("<!--LECTURE-->\n", "").replace("<!--/LECTURE-->\n", "")


if __name__ == "__main__":
    import sys
    faits, replis = 0, []
    for code in (sys.argv[1:] or CODES):
        if not os.path.exists(os.path.join(ICI, "textes", f"{code}.json")):
            replis.append(code)
        out = os.path.join(SITE, "index.html") if code == "fr" else os.path.join(SITE, code, "index.html")
        open(out, "w", encoding="utf-8", newline="\n").write(page(code))
        faits += 1
    print(f"{faits} page(s) générée(s)" + (f" — textes en anglais faute de traduction : {' '.join(replis)}" if replis else ""))
