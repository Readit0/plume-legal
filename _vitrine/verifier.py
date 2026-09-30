"""Vérifie les fichiers de textes de la vitrine : python verifier.py [codes…]"""
import json, os, re, sys

ICI = os.path.dirname(os.path.abspath(__file__))
ARB = r"C:\Users\T470s\Desktop\PLUME\lib\l10n"
fr = json.load(open(os.path.join(ICI, "textes", "fr.json"), encoding="utf-8"))
MOTS_FR = re.compile(r"\b(tes|avec|dans|pour|leur|être|c'est|n'est|appli|réécri\w*)\b", re.I)


def arb(code):
    for nom in (code, code.split("-")[0]):
        p = os.path.join(ARB, f"app_{nom}.arb")
        if os.path.exists(p):
            return json.load(open(p, encoding="utf-8"))
    return {}


def verifier(code):
    p = os.path.join(ICI, "textes", f"{code}.json")
    if not os.path.exists(p):
        return [f"{code}: fichier absent"]
    try:
        d = json.load(open(p, encoding="utf-8"))
    except Exception as e:
        return [f"{code}: JSON invalide ({e})"]
    err = []
    manque = set(fr) - set(d)
    trop = set(d) - set(fr)
    if manque: err.append(f"{code}: clés manquantes {sorted(manque)}")
    if trop: err.append(f"{code}: clés en trop {sorted(trop)}")
    for k, v in d.items():
        if not isinstance(v, str) or not v.strip():
            err.append(f"{code}.{k}: vide")
            continue
        if fr.get(k, "").count("*") != v.count("*"):
            err.append(f"{code}.{k}: marques * attendues {fr[k].count('*')}, trouvées {v.count('*')}")
        if "<" in v or ">" in v:
            err.append(f"{code}.{k}: balise HTML interdite")
        if code not in ("fr", "fr-CA") and k not in ("demo_contact",) and MOTS_FR.search(v) and code not in ("ht",):
            err.append(f"{code}.{k}: du français semble rester : {v[:60]}")
    a = arb(code)
    for cle in ("styleFriendly", "styleProfessional"):
        nom = a.get(cle)
        if nom and "regles_texte" in d and nom not in d["regles_texte"]:
            err.append(f"{code}.regles_texte: le nom de persona de l'app « {nom} » ({cle}) n'y figure pas")
    return err


codes = sys.argv[1:] or [f[:-5] for f in sorted(os.listdir(os.path.join(ICI, "textes"))) if f.endswith(".json")]
tout = []
for c in codes:
    tout += verifier(c)
print("\n".join(tout) if tout else f"OK ({len(codes)} langue(s))")
sys.exit(1 if tout else 0)
