# ClickFix: the fake CAPTCHA that makes you install the malware yourself (The Conversation, Nov 2026)

`ClickFix · Fake CAPTCHA · Social engineering · Infostealers · Security awareness · Source: The Conversation (academic explainer)`

Status as of 19 Nov 2026. This page rests on search-result excerpts of one article, not the full text: The Conversation blocked automated fetching of the page, and I did not use a mirror or republished copy to get around that. Treat everything below as the excerpts' content and read the article before relying on any detail.

## The source

Abu Barkat ullah (University of Canberra) and Mohiuddin Ahmed (Adelaide University), "This sneaky CAPTCHA scam tricks you into installing malware. Here's what you need to know", The Conversation, dated 18 Nov 2026: <https://theconversation.com/this-sneaky-captcha-scam-tricks-you-into-installing-malware-heres-what-you-need-to-know-296919>. The authorship and date come from syndication listings of the article.

## What the excerpts say

- **The scam.** Criminals imitate familiar "prove you are human" checks. The named technique is **ClickFix**, which tricks people into running harmful instructions on their own computers.
- **How it plays out.** A verification screen appears while browsing and asks the user to tick a box. Instead of completing the check, the page shows further instructions, for example to paste a command into the Windows "Run" tool. These are legitimate tools for advanced users, which the attackers turn to installing malware.
- **Tell-tale sign.** A genuine CAPTCHA never asks a user to copy and paste commands.
- **Impact.** The malware can steal passwords, browsing information and other sensitive data. The article calls the threat global and says criminals may use stolen data to reach personal accounts, steal money or launch further attacks.

## Corroborating context (separate sources, excerpts only)

- A University of Michigan security alert describes fake-CAPTCHA pages that direct visitors to run code that downloads and executes malware, mentions Lumma Stealer, and gives a compromised news site as one place the fake check appeared.
- A TechRadar report, citing BleepingComputer, described an earlier campaign where a fake CAPTCHA coaxed users into overriding browser warnings about a downloaded executable.
- A Fox News piece describes the same pattern as copying a command to the clipboard and having the user run it, without a file download.

I did not open these pages in full.

## Why a privacy and cyber hub should care

- **Employee-initiated execution.** The user, not an exploit, runs the command, so patching does not stop it. That makes it a training and endpoint-policy issue (restricting the Run dialog, PowerShell and terminal use for ordinary users is a common control, though that is my addition, not from the article).
- **Credential and personal-data theft.** Infostealers take saved passwords and browser data, which can lead to account takeover and later personal-data incidents.
- **Any site can host it.** Compromised legitimate websites, and third-party script compromises such as the [Optimizely case](../case-studies/optimizely-third-party-script-compromise-178-sites-2026.md), can place a lure in front of real visitors; the article does not link these.
- For related awareness material, see the [training labs](../training-labs/README.md) and the [reference sites list](../training-labs/cyber-reference-sites-20.md).

## Gaps and cautions

- Excerpts only; the article's examples, figures and recommendations beyond the points above are not captured.
- An academic explainer for the public, not threat research; it gives no campaign data in the parts I saw.
- Not legal or security advice.
