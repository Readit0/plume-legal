# Plume Privacy Policy

**Last updated: 31 July 2026** — Version 1.0

---

## Who is responsible for your data

**SASU RedLine Music**
SIREN 938 277 100 — SIRET `938 277 100 00013`
Abbaye 208-1, 208 Résidence Lavoisier, 18100 Vierzon, France
Contact: sogacmoi7@gmail.com

The application is published on Google Play under the developer name **openfunworld**.

This policy describes what the Plume application does in its current version. It was written by reading the application's code, not from a generic template.

---

## In one minute

Plume helps you write: it rewrites your text directly in the application where you are typing, and it can translate text shown on your screen.

Three things to remember:

1. **Plume keeps none of your texts on its servers.** Neither the texts you have rewritten, nor the text read from your screen. We keep no copy and no log of them.
2. **Depending on the engine you choose, your text either leaves your phone or does not.** Two engines (the Local Kit and the On-device AI) work entirely on the device. The third (the Cloud AI) sends the text to an artificial intelligence service **located outside the European Union**. You choose, and the Cloud AI is never activated without your explicit agreement.
3. **Plume needs powerful permissions** (reading the content displayed in other applications, capturing the screen). Below we explain precisely what they are used for and what they are not used for.

---

## 1. What Plume reads on your screen, and when

### 1.1 The accessibility service

To rewrite your text where you are writing it, Plume uses Android's accessibility service. This is a permission that you enable yourself, in your phone's settings, after an explanation screen that Plume shows you **before** asking you for it.

In practice:

- **When idle**, Plume only knows which application is open and when you place the cursor in an input field. That is what makes the floating capsule appear — and only in the applications you have configured yourself.
- **The content of the field is read only at the precise moment when you touch the capsule**, so that it can be rewritten and then replaced in place.
- **Password fields are excluded.** The application detects password-type fields (including numeric codes and web fields) and refuses to read them.
- This permission **does not allow any image capture** of your screen.
- Plume **never taps on your behalf** in another application: it replaces the text of a field, nothing else.

Two features that you enable yourself — **Assisted Reading in Text mode** and **translation of incoming messages** — read the displayed text continuously while they are running, and stop as soon as you switch them off.

If you decline the accessibility service, Plume remains usable: you can select a text and go through the "Plume" entry in the Android selection menu, or share a text to Plume.

### 1.2 Screen capture (Assisted Reading)

Assisted Reading overlays a translation on top of the displayed text — for example the speech bubbles of a comic. It needs to see the image of the screen.

- It is **disabled by default** and works only in the applications you have explicitly authorised, one by one.
- **Android asks for its own consent at the start of every session.** This is not a permission granted once and for all: each session requires a new agreement. Plume never seeks to reuse or bypass that agreement.
- Throughout the session, **a permanent notification and a system indicator remain visible**. Plume cannot capture your screen discreetly.
- The session **stops automatically when the screen is locked**, and immediately when you stop it yourself.
- Applications that protect their display (banking applications, password managers) are **blacked out by Android itself** before Plume receives anything at all. This is a system protection, real but partial: not all sensitive applications enable it. We therefore do not present it as an absolute guarantee.
- **Captured images are never saved or sent.** Each image is analysed in memory to extract the text from it, then discarded. No image ever leaves your phone, whatever engine is chosen.

---

## 2. What stays on your phone and what leaves it

This is the most important distinction in this policy, and you are the one who controls it.

### 2.1 The engines that send nothing out

- **The Local Kit** (offline text recognition and translation) runs entirely on the device.
- **The On-device AI** is an artificial intelligence model downloaded once and then stored on your phone (about 720 MB). It runs on your device.

With these two engines, **the text that is read or rewritten does not leave your phone.** There is no network call related to the content of your text.

### 2.2 The Cloud AI engine

When you choose the Cloud AI, or when your device is not powerful enough for the On-device AI, the text concerned is transmitted to our servers, then to a third-party artificial intelligence service.

**We have to be clear about the actual journey:**

- The text passes through our infrastructure (Supabase), hosted in the **European Union** (Central Europe region, Frankfurt).
- It is then transmitted to **openrouter.ai**, a routing intermediary **located outside the European Union**, which has it processed by the **Mistral Small** model.
- **This is therefore a transfer of data outside the European Union.** We do not claim otherwise, and we make no promise of European hosting for this step.
- **Plume does not keep your text.** None of our server functions writes the content of your text: we record only a technical request identifier and your device identifier, in order to count your quota and detect abuse.
- **What these providers do on their side, we cannot guarantee.** We prefer to tell you so rather than promise you zero retention that we are not in a position to verify.

**The Cloud AI never activates on its own.** A dedicated consent screen explains these points to you before the first transmission, and nothing is sent until you have accepted. If the On-device AI fails, Plume does not silently switch to the cloud: it tells you and waits for your decision. You can withdraw this agreement at any time in the settings.

The text sent is capped: 1,200 characters for a rewrite, 4,000 characters for a screen analysis.

---

## 3. The data we keep

We use **no audience analytics tool, no third-party advertising tracker and no crash reporting tool**. The application contains no measurement SDK.

Here is everything that is stored on our servers:

| Data | Why | Retention |
|---|---|---|
| **Device identifier** (a random number generated by Plume, with no link to your identity or to any advertising identifier) | Link a device to an account, apply quotas, block abuse | Until your account is deleted |
| **Account e-mail address** (if you create an account by e-mail or via Google) | Authenticate you, link your subscription | Until your account is deleted |
| **Usage counters** (number of rewrites per day and per month — numbers, not texts) | Apply quotas | Until your account is deleted |
| **Purchase history** (Google Play transaction identifier, dates, subscription status) | Give you access to what you have paid for, manage renewals, meet our accounting obligations | Kept even after the account is deleted, but **detached from your identity** (see §6) |
| **Suggestions sent voluntarily** (if you send us a persona suggestion from the application) | Improve the catalogue. These suggestions are never published. | Until your account is deleted |
| **Technical abuse signals** (repeated overruns, integrity check failures — without any text) | Security, fraud prevention | Detached from your identity when the account is deleted |
| **Language and application version** | Serve the right content | Until your account is deleted |

**What we do not collect:** your name, your contacts, your location, your address book, your photos, your calendar, your application history. Plume requests none of these permissions.

**What stays only on your phone:** your custom personas and their avatars, your settings, your per-application rules, the Assisted Reading translation cache (cleared at the end of every session). None of this is sent to our servers.

---

## 4. Voice dictation

A microphone button lets you dictate instead of typing. Permission to access the microphone is requested **at the precise moment when you press that button**, never at start-up, and the microphone opens only at that instant. Plume never listens in the background.

**Plume does not receive, store or transmit any audio recording.** Dictation is entrusted to the speech recognition engine built into your phone (Android's). Plume receives only the transcribed text.

**An important and honest point:** that system engine belongs to your phone, generally to Google. Depending on your device, its settings and the installed language modules, **it may transmit the audio to its publisher's servers** in order to transcribe it. That processing is beyond Plume's control and is governed by the privacy policy of the publisher of your operating system. We therefore cannot state that your voice stays on the device — that depends on your phone, not on us.

If you decline the microphone permission, keyboard input of course remains available.

---

## 5. Advertising

The service is free within a certain daily usage limit. Beyond that, you may **choose** to watch a rewarded ad to unlock additional uses. This is never imposed: if you do not watch an ad, you simply keep what you are entitled to.

- The ads are provided by **Google AdMob**.
- They appear **only within the Plume application itself**, never in the floating capsule and never on top of another application.
- **Subscribers see no advertising.**
- In the European Economic Area, the United Kingdom and Switzerland, a consent form provided by a platform certified by Google is presented to you **before the first ad**. Until your choice has been collected, no ad is requested. If you refuse, the ads remain **non-personalised** and **no feature is taken away from you**. You can change this choice at any time from the settings.
- In order to credit your reward reliably, your Plume device identifier is transmitted to AdMob. Google may also collect its own data in accordance with its privacy policy.

*At the time of writing, ad serving is disabled on the server side. This section describes how it will work once it is enabled.*

---

## 6. Subscriptions and purchases

Subscriptions and packs are sold **through Google Play**. We never see your bank details: they are handled by Google, which is the seller for billing purposes.

We receive a purchase receipt from Google which our server verifies, and we keep a record of it (transaction identifier, dates, status). This record is kept for accounting reasons and to prevent the same purchase from being used twice — but it is **detached from your identity** when you delete your account.

---

## 7. Your rights

You have the rights of access, rectification, erasure, restriction of processing, objection and data portability provided for by the GDPR.

**The simplest and fastest way: deletion is built into the application.**
Settings → Privacy → Delete my data. It is **carried out immediately**, not placed in a queue. The details of what is erased and what is kept are set out on our dedicated page: `https://readit0.github.io/plume-legal/suppression-compte`.

You can also delete your account **without installing the application**, by writing to sogacmoi7@gmail.com.

For any other request, write to **sogacmoi7@gmail.com**. We reply within one month.

**Legal bases:** performance of the contract (providing the service you request, managing your subscription), your consent (accessibility service, screen capture, transmission to the Cloud AI, personalised advertising), our legitimate interests (security, fraud prevention) and our legal obligations (accounting).

You may lodge a complaint with the **CNIL** (www.cnil.fr), the publisher's supervisory authority, or, **if you reside in the European Union**, with the supervisory authority of your country of residence — Article 77 of the GDPR leaves the choice to you.

---

## 8. Minors

Plume is a writing-assistance tool intended for an audience **aged 16 and over**. We do not knowingly collect data from children under 16, and the application is neither designed nor promoted for them. If you hold parental authority and believe that your child has sent us data, write to sogacmoi7@gmail.com: we will delete the account.

As the application allows free text to be rewritten and displays advertising, it is not eligible for Google Play's family programmes.

---

## 9. Processors and recipients

| Provider | Role | Where |
|---|---|---|
| **Supabase** | Database hosting, authentication, server functions | European Union (Frankfurt) |
| **OpenRouter** | Routing of requests to the AI model | **Outside the European Union** |
| **Mistral AI** (via OpenRouter) | Model that processes the text (Mistral Small) | Processing via the intermediary above |
| **Google Play / Google Billing** | Payment, subscriptions | Google Ireland / United States |
| **Google AdMob** | Rewarded advertising | Google Ireland / United States |
| **Google (phone system services)** | Speech recognition, offline translation modules | Depending on your device |

**We sell no data and transfer none to data brokers.**

**Transfers outside the European Union:** the use of OpenRouter, Google Play and AdMob involves a transfer of data outside the European Union.

---

## 10. Security

Exchanges between the application and our servers are encrypted (HTTPS/TLS). Access to the data in the database is restricted by server-side rules: sensitive functions are not accessible from the application. No system is perfectly secure, but none of the text you rewrite is stored with us — which mechanically limits what an intrusion could reveal.

---

## 11. Changes

Any change to this policy will be published at `https://readit0.github.io/plume-legal` with a new date. If there is a significant change in how your data circulates, we will inform you within the application.

---

## Terms and conditions

The terms of use of the service (quotas, subscriptions, cancellation) are set out in a separate document: `https://readit0.github.io/plume-legal/conditions-generales`.

---

---

This document is a translation of the French version, available at https://readit0.github.io/plume-legal/. It is provided for your information. In the event of any discrepancy, please contact us at sogacmoi7@gmail.com.
