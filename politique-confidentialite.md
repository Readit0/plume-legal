# Politique de confidentialité de Plume

**Dernière mise à jour : 31 juillet 2026** — Version 1.0

> **MARQUEURS RESTANT À COMPLÉTER AVANT PUBLICATION**
> - `938 277 100 00013` : nous n'avons que le SIREN (9 chiffres). Le SIRET (14 chiffres) figure sur le Kbis.
> - `https://readit0.github.io/plume-legal` : adresse où ces pages seront hébergées. Elle doit être renseignée dans la fiche Play Store et dans les renvois internes de ce document.

---

## Qui est responsable de vos données

**SAS REDLINE MUSIC**
SIREN 938 277 100 — SIRET `938 277 100 00013`
A 208, 1208 rue Lavoisier, 18100 Vierzon, France
Contact : sogacmoi7@gmail.com

L'application est publiée sur Google Play sous le nom d'éditeur **openfunword**.

Cette politique décrit ce que fait l'application Plume dans sa version actuelle. Elle a été rédigée en lisant le code de l'application, pas à partir d'un modèle générique.

---

## En une minute

Plume vous aide à écrire : elle reformule votre texte directement dans l'application où vous êtes en train de taper, et elle peut traduire du texte affiché à l'écran.

Trois choses à retenir :

1. **Plume ne conserve aucun de vos textes sur ses serveurs.** Ni vos textes reformulés, ni le texte lu à l'écran. Nous n'en gardons ni copie, ni journal.
2. **Selon le moteur que vous choisissez, votre texte quitte ou ne quitte pas votre téléphone.** Deux moteurs (le Kit local et l'IA locale) travaillent entièrement sur l'appareil. Le troisième (l'IA Cloud) envoie le texte à un service d'intelligence artificielle **situé hors de l'Union européenne**. Vous choisissez, et l'IA Cloud ne s'active jamais sans votre accord explicite.
3. **Plume a besoin d'autorisations puissantes** (lire le contenu affiché dans les autres applications, capturer l'écran). Nous expliquons ci-dessous précisément ce qu'elles servent et ce qu'elles ne servent pas.

---

## 1. Ce que Plume lit sur votre écran, et quand

### 1.1 Le service d'accessibilité

Pour réécrire votre texte à l'endroit où vous l'écrivez, Plume utilise le service d'accessibilité d'Android. C'est une autorisation que vous activez vous-même, dans les réglages du téléphone, après un écran d'explication que Plume vous montre **avant** de vous la demander.

Concrètement :

- **Au repos**, Plume sait seulement quelle application est ouverte et à quel moment vous placez le curseur dans un champ de saisie. C'est ce qui fait apparaître la capsule flottante — et uniquement dans les applications que vous avez vous-même configurées.
- **Le contenu du champ n'est lu qu'à l'instant précis où vous touchez la capsule**, pour être réécrit puis remplacé sur place.
- **Les champs de mot de passe sont exclus.** L'application détecte les champs de type mot de passe (y compris les codes numériques et les champs web) et refuse de les lire.
- Cette autorisation **ne permet aucune capture d'image** de votre écran.
- Plume **n'appuie jamais à votre place** dans une autre application : elle remplace le texte d'un champ, rien d'autre.

Deux fonctions que vous activez vous-même — la **Lecture Assistée en mode Texte** et la **traduction des messages reçus** — lisent le texte affiché en continu tant qu'elles tournent, et s'arrêtent dès que vous les coupez.

Si vous refusez le service d'accessibilité, Plume reste utilisable : vous pouvez sélectionner un texte et passer par le menu « Plume » de la sélection Android, ou partager un texte vers Plume.

### 1.2 La capture d'écran (Lecture Assistée)

La Lecture Assistée superpose une traduction par-dessus le texte affiché — par exemple les bulles d'une bande dessinée. Elle a besoin de voir l'image de l'écran.

- Elle est **désactivée par défaut** et ne fonctionne que dans les applications que vous avez explicitement autorisées, une par une.
- **Android vous demande son propre consentement à chaque démarrage de session.** Ce n'est pas une permission accordée une fois pour toutes : chaque session exige un nouvel accord. Plume ne cherche jamais à réutiliser ou contourner cet accord.
- Pendant toute la session, **une notification permanente et un indicateur système restent visibles**. Plume ne peut pas capturer votre écran discrètement.
- La session **s'arrête automatiquement au verrouillage de l'écran**, et immédiatement quand vous l'arrêtez vous-même.
- Les applications qui protègent leur affichage (applications bancaires, gestionnaires de mots de passe) sont **occultées par Android lui-même** avant que Plume ne reçoive quoi que ce soit. C'est une protection du système, réelle mais partielle : toutes les applications sensibles ne l'activent pas. Nous ne la présentons donc pas comme une garantie absolue.
- **Les images capturées ne sont jamais enregistrées ni envoyées.** Chaque image est analysée en mémoire pour en extraire le texte, puis abandonnée. Aucune image ne part de votre téléphone, jamais, quel que soit le moteur choisi.

---

## 2. Ce qui reste sur votre téléphone et ce qui part

C'est la distinction la plus importante de cette politique, et c'est vous qui la contrôlez.

### 2.1 Les moteurs qui ne font rien sortir

- **Le Kit local** (reconnaissance et traduction de texte hors ligne) fonctionne entièrement sur l'appareil.
- **L'IA locale** est un modèle d'intelligence artificielle téléchargé une fois puis stocké sur votre téléphone (environ 720 Mo). Il s'exécute sur votre appareil.

Avec ces deux moteurs, **le texte lu ou reformulé ne quitte pas votre téléphone.** Il n'y a aucun appel réseau lié au contenu de votre texte.

### 2.2 Le moteur IA Cloud

Quand vous choisissez l'IA Cloud, ou quand votre appareil n'est pas assez puissant pour l'IA locale, le texte concerné est transmis à nos serveurs, puis à un service d'intelligence artificielle tiers.

**Il faut être clair sur le trajet réel :**

- Le texte transite par notre infrastructure (Supabase), hébergée dans l'**Union européenne** (région Europe centrale, Francfort).
- Il est ensuite transmis à **openrouter.ai**, un intermédiaire de routage **situé hors de l'Union européenne**, qui le fait traiter par le modèle **Mistral Small**.
- **Il s'agit donc d'un transfert de données hors de l'Union européenne.** Nous ne prétendons pas le contraire, et nous n'affichons aucune promesse d'hébergement européen pour cette étape.
- **Plume ne conserve pas votre texte.** Aucune de nos fonctions serveur n'écrit le contenu de votre texte : nous n'enregistrons qu'un identifiant technique de requête et l'identifiant de votre appareil, pour compter votre quota et détecter les abus.
- **Ce que ces prestataires font de leur côté, nous ne pouvons pas le garantir.** Nous préférons vous le dire plutôt que de vous promettre une rétention nulle que nous ne sommes pas en mesure de vérifier.

**L'IA Cloud ne s'active jamais toute seule.** Un écran de consentement dédié vous explique ces points avant le premier envoi, et rien ne part tant que vous n'avez pas accepté. Si l'IA locale échoue, Plume ne bascule pas vers le cloud en silence : elle vous le signale et attend votre décision. Vous pouvez révoquer cet accord à tout moment dans les réglages.

Le texte envoyé est plafonné : 1 200 caractères pour une reformulation, 4 000 caractères pour une analyse d'écran.

---

## 3. Les données que nous conservons

Nous n'utilisons **aucun outil d'analyse d'audience, aucun traceur publicitaire tiers, aucun outil de rapport de plantage**. L'application ne contient pas de SDK de mesure.

Voici l'intégralité de ce qui est stocké sur nos serveurs :

| Donnée | Pourquoi | Durée |
|---|---|---|
| **Identifiant d'appareil** (un numéro aléatoire généré par Plume, sans lien avec votre identité ni avec un identifiant publicitaire) | Rattacher un appareil à un compte, appliquer les quotas, bloquer les abus | Jusqu'à la suppression de votre compte |
| **Adresse e-mail du compte** (si vous créez un compte par e-mail ou via Google) | Vous authentifier, rattacher votre abonnement | Jusqu'à la suppression de votre compte |
| **Compteurs d'usage** (nombre de reformulations par jour et par mois — des nombres, pas des textes) | Appliquer les quotas | Jusqu'à la suppression de votre compte |
| **Historique d'achat** (identifiant de transaction Google Play, dates, état de l'abonnement) | Vous donner accès à ce que vous avez payé, gérer les renouvellements, respecter nos obligations comptables | Conservé même après suppression du compte, mais **détaché de votre identité** (voir §6) |
| **Suggestions envoyées volontairement** (si vous nous écrivez une suggestion de persona depuis l'application) | Améliorer le catalogue. Ces suggestions ne sont jamais publiées. | Jusqu'à la suppression de votre compte |
| **Signaux techniques d'abus** (dépassements répétés, échec de contrôle d'intégrité — sans aucun texte) | Sécurité, lutte contre la fraude | Détachés de votre identité à la suppression du compte |
| **Langue et version de l'application** | Servir le bon contenu | Jusqu'à la suppression de votre compte |

**Ce que nous ne collectons pas :** votre nom, vos contacts, votre localisation, votre carnet d'adresses, vos photos, votre agenda, l'historique de vos applications. Plume ne demande aucune de ces autorisations.

**Ce qui reste uniquement sur votre téléphone :** vos personas personnalisés et leurs avatars, vos réglages, vos règles par application, le cache de traduction de la Lecture Assistée (effacé à la fin de chaque session). Rien de tout cela n'est envoyé à nos serveurs.

---

## 4. La dictée vocale

Un bouton microphone vous permet de dicter au lieu de taper. L'autorisation d'accès au micro est demandée **au moment précis où vous appuyez sur ce bouton**, jamais au démarrage, et le micro ne s'ouvre qu'à cet instant. Plume n'écoute jamais en arrière-plan.

**Plume ne reçoit, ne stocke et ne transmet aucun enregistrement audio.** La dictée est confiée au moteur de reconnaissance vocale intégré à votre téléphone (celui d'Android). Plume ne récupère que le texte transcrit.

**Point important et honnête :** ce moteur système appartient à votre téléphone, généralement à Google. Selon votre appareil, ses réglages et les modules de langue installés, **il peut transmettre l'audio aux serveurs de son éditeur** pour le transcrire. Ce traitement échappe à Plume et relève de la politique de confidentialité de l'éditeur de votre système. Nous ne pouvons donc pas affirmer que votre voix reste sur l'appareil — cela dépend de votre téléphone, pas de nous.

Si vous refusez l'autorisation du micro, la saisie au clavier reste évidemment disponible.

---

## 5. Publicité

Le service est gratuit dans une certaine limite d'utilisation par jour. Au-delà, vous pouvez **choisir** de regarder une publicité récompensée pour débloquer des utilisations supplémentaires. Ce n'est jamais imposé : si vous ne regardez pas de publicité, vous gardez simplement ce à quoi vous avez droit.

- Les publicités sont fournies par **Google AdMob**.
- Elles apparaissent **uniquement dans l'application Plume elle-même**, jamais dans la capsule flottante et jamais par-dessus une autre application.
- **Les abonnés ne voient aucune publicité.**
- Dans l'Espace économique européen, au Royaume-Uni et en Suisse, un formulaire de consentement fourni par une plateforme certifiée par Google vous est présenté **avant la première publicité**. Tant que votre choix n'est pas recueilli, aucune publicité n'est demandée. Si vous refusez, les publicités restent **non personnalisées** et **aucune fonctionnalité ne vous est retirée**. Vous pouvez revenir sur ce choix à tout moment depuis les réglages.
- Pour créditer votre récompense de façon fiable, votre identifiant d'appareil Plume est transmis à AdMob. Google peut par ailleurs collecter ses propres données conformément à sa politique de confidentialité.

*À la date de rédaction, la diffusion publicitaire est désactivée côté serveur. Cette section décrit le fonctionnement dès qu'elle sera activée.*

---

## 6. Abonnements et achats

Les abonnements et les packs sont vendus **via Google Play**. Nous ne voyons jamais vos coordonnées bancaires : elles sont traitées par Google, qui est le vendeur au sens de la facturation.

Nous recevons de Google un justificatif d'achat que notre serveur vérifie, et nous en conservons la trace (identifiant de transaction, dates, état). Cette trace est conservée pour des raisons comptables et pour empêcher qu'un même achat serve deux fois — mais elle est **détachée de votre identité** lorsque vous supprimez votre compte.

---

## 7. Vos droits

Vous disposez des droits d'accès, de rectification, d'effacement, de limitation, d'opposition et de portabilité prévus par le RGPD.

**Le plus simple, et le plus rapide : la suppression est intégrée à l'application.**
Réglages → Confidentialité → Supprimer mes données. Elle est **exécutée immédiatement**, pas mise en file d'attente. Le détail de ce qui est effacé et de ce qui est conservé figure dans notre page dédiée : `https://readit0.github.io/plume-legal/suppression-compte`.

Vous pouvez aussi supprimer votre compte **sans installer l'application**, en écrivant à sogacmoi7@gmail.com.

Pour toute autre demande, écrivez à **sogacmoi7@gmail.com**. Nous répondons sous un mois.

**Bases légales :** l'exécution du contrat (fournir le service que vous demandez, gérer votre abonnement), votre consentement (service d'accessibilité, capture d'écran, envoi vers l'IA Cloud, publicité personnalisée), notre intérêt légitime (sécurité, lutte contre la fraude) et nos obligations légales (comptabilité).

Vous pouvez introduire une réclamation auprès de la **CNIL** (www.cnil.fr).

---

## 8. Les mineurs

Plume est un outil d'aide à la rédaction, destiné à un public **de 13 ans et plus**. Nous ne collectons pas sciemment de données d'enfants de moins de 13 ans et l'application n'est pas conçue ni promue pour eux. Si vous êtes titulaire de l'autorité parentale et pensez que votre enfant nous a transmis des données, écrivez à sogacmoi7@gmail.com : nous supprimerons le compte.

Comme l'application permet de reformuler un texte libre et affiche de la publicité, elle n'est pas éligible aux programmes destinés aux familles de Google Play.

---

## 9. Sous-traitants et destinataires

| Prestataire | Rôle | Où |
|---|---|---|
| **Supabase** | Hébergement de la base de données, authentification, fonctions serveur | Union européenne (Francfort) |
| **OpenRouter** | Acheminement des requêtes vers le modèle d'IA | **Hors Union européenne** |
| **Mistral AI** (via OpenRouter) | Modèle qui traite le texte (Mistral Small) | Traitement via l'intermédiaire ci-dessus |
| **Google Play / Google Billing** | Paiement, abonnements | Google Ireland / États-Unis |
| **Google AdMob** | Publicité récompensée | Google Ireland / États-Unis |
| **Google (services système du téléphone)** | Reconnaissance vocale, modules de traduction hors ligne | Selon votre appareil |

**Nous ne vendons aucune donnée et n'en cédons aucune à des courtiers en données.**

**Transferts hors Union européenne :** le recours à OpenRouter, à Google Play et à AdMob implique un transfert de données hors de l'Union européenne. L'encadrement juridique de ces transferts (clauses contractuelles types, décision d'adéquation) **doit être vérifié et documenté par un professionnel avant publication** — voir la note en fin de document.

---

## 10. Sécurité

Les échanges entre l'application et nos serveurs sont chiffrés (HTTPS/TLS). L'accès aux données en base est restreint par des règles serveur : les fonctions sensibles ne sont pas accessibles depuis l'application. Aucun système n'est parfaitement sûr, mais aucun texte que vous reformulez n'est stocké chez nous — ce qui limite mécaniquement ce qu'une intrusion pourrait révéler.

---

## 11. Modifications

Toute modification de cette politique sera publiée à l'adresse `https://readit0.github.io/plume-legal` avec une nouvelle date. En cas de changement important sur la circulation de vos données, nous vous en informerons dans l'application.

---

## Conditions générales

Les conditions d'utilisation du service (quotas, abonnements, résiliation) figurent dans un document distinct : `https://readit0.github.io/plume-legal/conditions-generales`.

---

> ### À faire relire par un professionnel
>
> Ce document a été rédigé en mesurant le comportement réel de l'application, mais **il n'a pas été rédigé par un juriste**. Quatre points méritent en priorité un avis professionnel :
>
> 1. **Le transfert de données hors Union européenne** vers OpenRouter. C'est le point le plus sensible : il faut déterminer le mécanisme de transfert applicable, vérifier qu'un accord de traitement existe avec ce prestataire, et l'écrire ici. Tant que ce n'est pas fait, ce document décrit le transfert sans affirmer qu'il est encadré.
> 2. **Les bases légales** retenues au §7, en particulier la répartition entre consentement et intérêt légitime pour le service d'accessibilité.
> 3. **L'âge minimum** (13 ans) et sa cohérence avec le questionnaire de classification de contenu de Google Play.
> 4. **La mention relative à l'IA** au titre du règlement européen sur l'intelligence artificielle (obligation de transparence pour un système à risque limité).
