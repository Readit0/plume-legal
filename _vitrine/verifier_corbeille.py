"""Vérifie la correction « corbeille du camouflage vidée après 30 jours » : python verifier_corbeille.py [codes…]

Pour chaque langue, compare au dernier commit (git HEAD) :
  - politique : EXACTEMENT 1 ligne d'origine modifiée, aucune ligne ajoutée ni retirée,
    nombre de lignes de tableau inchangé, la ligne modifiée est une ligne de tableau
    « | ** » qui contient « 30 » (le délai) ;
  - suppression-compte.md : INCHANGÉ ;
  - fins de ligne non mélangées, pas de français collé dans la ligne modifiée.
"""
import os, re, subprocess, sys

ICI = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.dirname(ICI)


def head(chemin):
    r = subprocess.run(["git", "-C", SITE, "show", f"HEAD:{chemin}"], capture_output=True)
    return r.stdout.decode("utf-8") if r.returncode == 0 else None


def verifier(code):
    err = []
    base = "" if code == "fr" else f"{code}/"
    rel = base + "politique-confidentialite.md"
    avant = head(rel)
    apres = open(os.path.join(SITE, rel), encoding="utf-8", newline="").read()
    if "\r\n" in apres and "\n" in apres.replace("\r\n", ""):
        err.append(f"{rel}: fins de ligne mélangées")
    la = avant.replace("\r\n", "\n").split("\n")
    lb = apres.replace("\r\n", "\n").split("\n")
    if len(la) != len(lb):
        err.append(f"{rel}: {len(lb) - len(la):+d} ligne(s) — attendu : même nombre")
    diff = [(a, b) for a, b in zip(la, lb) if a != b]
    if len(diff) != 1:
        err.append(f"{rel}: {len(diff)} ligne(s) modifiée(s), 1 attendue")
    else:
        a, b = diff[0]
        if not (a.startswith("| **") and b.startswith("| **")):
            err.append(f"{rel}: la ligne modifiée n'est pas une ligne de tableau")
        if not re.search(r"30|٣٠|۳۰|३०|৩০|三十|30", b):
            err.append(f"{rel}: le délai de 30 jours n'apparaît pas dans la ligne corrigée")
        if b.count("|") != a.count("|"):
            err.append(f"{rel}: nombre de colonnes changé ({a.count('|')} → {b.count('|')})")
        if code != "fr" and re.search(r"\b(peut être restauré|prochaine fois|vos carnets)\b", b):
            err.append(f"{rel}: du français collé semble rester")
    rel2 = base + "suppression-compte.md"
    if head(rel2) != open(os.path.join(SITE, rel2), encoding="utf-8", newline="").read():
        # comparaison tolérante aux fins de ligne
        a2 = (head(rel2) or "").replace("\r\n", "\n")
        b2 = open(os.path.join(SITE, rel2), encoding="utf-8", newline="").read().replace("\r\n", "\n")
        if a2 != b2:
            err.append(f"{rel2}: modifié alors qu'il ne devait pas l'être")
    return err


codes = sys.argv[1:] or (["fr"] + sorted(d for d in os.listdir(SITE) if os.path.exists(os.path.join(SITE, d, "politique-confidentialite.md"))))
tout = []
for c in codes:
    tout += verifier(c)
print("\n".join(tout) if tout else f"OK ({len(codes)} langue(s))")
sys.exit(1 if tout else 0)
