"""Vérifie la mise à jour 2.1 des pages légales traduites : python verifier_legal.py [codes…]

Pour chaque langue, compare le fichier au dernier commit (git HEAD) :
  - version « 2.1 » dans l'en-tête, « 2.0 » n'y est plus ;
  - politique : +5 lignes de tableau « | ** », rien de supprimé hors des lignes que
    la version française modifie (en-tête, point 1, puce §2.2, phrase §10) ;
  - suppression : +1 puce (carnets de camouflage) et un paragraphe de 3 puces ;
  - fins de ligne CRLF conservées, pas de texte français collé dans une autre langue.
"""
import os, re, subprocess, sys

ICI = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.dirname(ICI)


def head(chemin):
    r = subprocess.run(["git", "-C", SITE, "show", f"HEAD:{chemin}"], capture_output=True)
    return r.stdout.decode("utf-8") if r.returncode == 0 else None


def verifier(code):
    err = []
    for nom in ("politique-confidentialite.md", "suppression-compte.md"):
        rel = f"{code}/{nom}"
        p = os.path.join(SITE, code, nom)
        avant = head(rel)
        apres = open(p, encoding="utf-8", newline="").read()
        if avant is None:
            err.append(f"{rel}: absent du dernier commit"); continue
        if "\r\n" in apres and "\n" in apres.replace("\r\n", ""):
            err.append(f"{rel}: fins de ligne mélangées (CRLF et LF)")
        tete = "\n".join(apres.replace("\r\n", "\n").split("\n")[:4])
        if "2.1" not in tete:
            err.append(f"{rel}: version 2.1 absente de l'en-tête")
        if re.search(r"\b2\.0\b", tete):
            err.append(f"{rel}: « 2.0 » encore dans l'en-tête")
        la, lb = avant.replace("\r\n", "\n").split("\n"), apres.replace("\r\n", "\n").split("\n")
        disparues = [l for l in la if l.strip() and l not in lb]
        if nom == "politique-confidentialite.md":
            d = sum(1 for l in lb if l.startswith("| **")) - sum(1 for l in la if l.startswith("| **"))
            if d != 5:
                err.append(f"{rel}: {d} ligne(s) de tableau ajoutée(s), 5 attendues")
            if len(disparues) > 5:
                err.append(f"{rel}: {len(disparues)} lignes d'origine modifiées/supprimées (≤ 5 attendues)")
        else:
            d = sum(1 for l in lb if l.startswith("- ")) - sum(1 for l in la if l.startswith("- "))
            if d != 4:
                err.append(f"{rel}: {d} puce(s) ajoutée(s), 4 attendues (1 carnet + 3 non effacés)")
            if len(disparues) > 5:
                err.append(f"{rel}: {len(disparues)} lignes d'origine modifiées/supprimées (≤ 5 attendues)")
        ajoutees = "\n".join(l for l in lb if l not in la)
        if code != "fr" and re.search(r"\b(carnet|mots en attente|jamais la phrase|empreinte pseudonyme)\b", ajoutees):
            err.append(f"{rel}: du français collé semble rester")
    return err


codes = sys.argv[1:] or sorted(d for d in os.listdir(SITE) if os.path.exists(os.path.join(SITE, d, "politique-confidentialite.md")))
tout = []
for c in codes:
    tout += verifier(c)
print("\n".join(tout) if tout else f"OK ({len(codes)} langue(s))")
sys.exit(1 if tout else 0)
