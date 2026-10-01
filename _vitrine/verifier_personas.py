"""Vérifie la correction « personas sauvegardés » (2e passe 2.1) : python verifier_personas.py [codes…]

Pour chaque langue, compare le fichier au dernier commit (git HEAD, qui porte déjà la 2.1) :
  - politique : +1 ligne de tableau « | ** » (personas), ≤ 2 lignes d'origine modifiées
    (avis 2.1 complété, phrase « uniquement sur votre téléphone ») ;
  - suppression : +1 puce (personas), ≤ 1 ligne d'origine modifiée (« Sur votre téléphone ») ;
  - en-tête toujours en 2.1, fins de ligne non mélangées, pas de français collé.
"""
import os, re, subprocess, sys

ICI = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.dirname(ICI)


def head(chemin):
    r = subprocess.run(["git", "-C", SITE, "show", f"HEAD:{chemin}"], capture_output=True)
    return r.stdout.decode("utf-8") if r.returncode == 0 else None


def verifier(code):
    err = []
    for nom, lignes_tab, puces, max_mod in (("politique-confidentialite.md", 1, 0, 2),
                                            ("suppression-compte.md", 0, 1, 1)):
        rel = f"{code}/{nom}" if code != "fr" else nom
        p = os.path.join(SITE, rel)
        avant = head(rel)
        apres = open(p, encoding="utf-8", newline="").read()
        if avant is None:
            err.append(f"{rel}: absent du dernier commit"); continue
        if "\r\n" in apres and "\n" in apres.replace("\r\n", ""):
            err.append(f"{rel}: fins de ligne mélangées (CRLF et LF)")
        tete = "\n".join(apres.replace("\r\n", "\n").split("\n")[:4])
        if "2.1" not in tete:
            err.append(f"{rel}: version 2.1 absente de l'en-tête")
        la, lb = avant.replace("\r\n", "\n").split("\n"), apres.replace("\r\n", "\n").split("\n")
        disparues = [l for l in la if l.strip() and l not in lb]
        dt = sum(1 for l in lb if l.startswith("| **")) - sum(1 for l in la if l.startswith("| **"))
        dp = sum(1 for l in lb if l.startswith("- ")) - sum(1 for l in la if l.startswith("- "))
        if dt != lignes_tab:
            err.append(f"{rel}: {dt} ligne(s) de tableau ajoutée(s), {lignes_tab} attendue(s)")
        if dp != puces:
            err.append(f"{rel}: {dp} puce(s) ajoutée(s), {puces} attendue(s)")
        if len(disparues) > max_mod:
            err.append(f"{rel}: {len(disparues)} lignes d'origine modifiées/supprimées (≤ {max_mod} attendues)")
        if not disparues:
            err.append(f"{rel}: aucune ligne d'origine corrigée (la phrase « sur votre téléphone » doit changer)")
        ajoutees = "\n".join(l for l in lb if l not in la)
        if code != "fr" and re.search(r"\b(personas personnalisés|sauvegardés sur nos serveurs|miniature|liste de personas)\b", ajoutees):
            err.append(f"{rel}: du français collé semble rester")
    return err


codes = sys.argv[1:] or (["fr"] + sorted(d for d in os.listdir(SITE) if os.path.exists(os.path.join(SITE, d, "politique-confidentialite.md"))))
tout = []
for c in codes:
    tout += verifier(c)
print("\n".join(tout) if tout else f"OK ({len(codes)} langue(s))")
sys.exit(1 if tout else 0)
