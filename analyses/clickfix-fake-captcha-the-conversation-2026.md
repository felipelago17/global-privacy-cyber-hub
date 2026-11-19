# ClickFix: the fake CAPTCHA that makes you install the malware yourself (The Conversation, Nov 2026)

`ClickFix · Fake CAPTCHA · Social engineering · Infostealers · Security awareness · Source: The Conversation (academic explainer)`

Status as of 19 Nov 2026. This page is based on the full article text, which the user supplied as a paste because The Conversation blocks automated fetching. I did not check the article against the live page. The article's own figures (bot traffic share, the Australian Vidar Stealer finding) are cited by the authors and I have not traced them to the underlying reports.

## The source

Abu Barkat ullah (University of Canberra) and Mohiuddin Ahmed (Adelaide University), "This sneaky CAPTCHA scam tricks you into installing malware. Here's what you need to know", The Conversation: <https://theconversation.com/this-sneaky-captcha-scam-tricks-you-into-installing-malware-heres-what-you-need-to-know-296919>. The pasted copy is dated 19 Nov 2026 (GMT); syndicated listings showed 18 Nov, probably a time-zone difference between editions. Authorship comes from those listings, since the paste does not show bylines.

## What the article says

- **Background.** CAPTCHAs separate people from bots. The authors cite the Thales Bad Bot Report for bots making up over 53% of web traffic in 2025, up from 51% in 2024.
- **The scam.** ClickFix gets victims to run harmful instructions themselves, presented as part of a legitimate security check, instead of breaking through technical defences.
- **The sequence.**
  1. The victim lands on what looks like an ordinary site, often reached through a search result. The authors say it is likely a legitimate site that criminals have compromised.
  2. A familiar "confirm you are human" screen appears and the victim ticks the box.
  3. The page silently copies a command to the clipboard, then tells the victim to press a shortcut such as Windows+R and paste the command.
  4. On Windows this is the Run dialog; on Apple computers it is Terminal. Both are legitimate administrator tools, turned here into an installer for malware.
- **Real-world example.** The authors say Australia's national cyber security agency found a ClickFix campaign spreading Vidar Stealer, which takes passwords, browsing data and other sensitive information.
- **Consequences.** Stolen data can be used to access accounts, steal money or mount further attacks. The authors call the threat global.
- **Key point.** Clicking the fake CAPTCHA alone does not necessarily infect the machine. The harm happens when the user runs the pasted command.

## Defences the article recommends

- A genuine CAPTCHA never asks you to copy-paste text or run commands.
- Do not follow instructions you do not understand, and do not download unknown programs or change security settings because a site says so.
- Keep the computer, browser and security software updated, noting this cannot stop every new attack.
- Use strong unique passwords and multi-factor authentication.
- For banking and other sensitive services, use a bookmark or type the address, and remember that legitimate sites can be compromised.
- **If you ran a command:** stop, disconnect the device from the internet, and get technical help (on a work computer, the IT team). From another trusted device, change potentially exposed passwords and check important accounts for suspicious activity.

## Corroborating context (separate sources, excerpts only)

- A University of Michigan security alert on fake-CAPTCHA pages that lead visitors to run code that downloads malware, naming Lumma Stealer.
- A TechRadar report, citing BleepingComputer, on an earlier campaign where a fake CAPTCHA got users to override browser warnings about a downloaded executable.

I did not open these pages in full. The article itself names Vidar Stealer, not Lumma, so these are different campaigns or families.

## Why a privacy and cyber hub should care

- **User-run execution.** No software vulnerability is exploited, so patching alone does not stop it. Awareness training and endpoint policy matter. Restricting the Run dialog, PowerShell and Terminal for ordinary users is a common control, but that is my addition, not the article's.
- **Credential and personal-data theft.** Infostealers can lead to account takeover and later personal-data incidents, with possible breach-notification consequences.
- **Compromised legitimate sites.** The authors' point that the lure may sit on a hacked genuine site fits third-party script compromises such as the [Optimizely case](../case-studies/optimizely-third-party-script-compromise-178-sites-2026.md). The article does not make that link.
- Related awareness material: [training labs](../training-labs/README.md) and the [reference sites list](../training-labs/cyber-reference-sites-20.md).

## Gaps and cautions

- A public explainer by academics, not threat research. It gives no campaign telemetry and does not name the Australian agency's report or date.
- The Thales and Vidar Stealer claims are the authors' and are unverified here.
- Not legal or security advice.
