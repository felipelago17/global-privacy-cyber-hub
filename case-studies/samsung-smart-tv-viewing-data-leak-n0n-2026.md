# Case study — Samsung smart TV viewing and political ad data leaked by the n0n ransomware group (alleged, 2026)

`Samsung Electronics · Ransomware leak · Smart TV ACR data · Political advertising data · AI training data · Allegation, unverified · Single source`

Status as of 24 Nov 2026. Everything here is an allegation by a ransomware group, investigated by Cybernews, and Samsung had not commented when the article was published. This page rests on a tool-generated summary of the Cybernews article and on search excerpts from Cybernews, Technext24, Lowyat.net, UpGuard, TechRadar and others. I have not read the article directly, seen the leaked files, or found a Samsung statement. The article's publication date is not stated in the summary, and the leak is tied to the group's activity in mid-September 2026.

## Summary

Cybernews reports that the ransomware group n0n allegedly stole about 220MB of Samsung Electronics data and posted it to its dark web leak site after a deadline passed. The article says the claim is unverified and that the files "appear to confirm" that Samsung smart TVs collect usage data and send it to Samsung's data centres. Technext24 relays the same story.

## What was reportedly in the leak

| Dataset | Reported content |
|---|---|
| Smart TV viewing data | About 150,000 viewing events from 2024, with timestamps, viewing durations, device information, cities, ZIP codes and TV service provider names. The data does not show what individual users watched |
| Political advertising data | About 42,600 records of political ads aired from Sept to Oct 2026, including political affiliations, advertised issues, sponsors, estimated costs and timestamps, plus one political ad video |
| AI advertising training data | About 99,100 records from 2021, mostly embedding vectors |
| Internal documents | A Sept 2026 data-use agreement including an employee's full name and email address, and an access questionnaire for what appears to be Samsung's Content Data Warehouse, revealing details about an employee and infrastructure |

The article does not say how many users were affected; the 150,000 figure counts viewing events, not people. It also does not give recommendations.

## Discovery and Samsung's position

Cybernews researchers investigated the exposed data. Separately, SOCRadar found that n0n's Python file server, linked to a location in Sweden, was exposed on the open internet. Samsung had not commented, and Cybernews said it had asked and would update the piece.

## Context the article raises (not part of this incident)

- Samsung was sued in Texas over allegedly collecting personal data unlawfully through Automated Content Recognition (ACR). An UpGuard excerpt says a settlement with Texas officials was announced on 1 Mar 2026 and that the allegation was collection of viewing data without express, informed consent; I have not read the settlement.
- Proton warned users about smart TV privacy, and a researcher claims Samsung TVs collect audio, screenshots and viewing activity for targeted ads (Lowyat, 26 Oct 2026). The article also says viewing data is reportedly shared with more than 400 partners for targeted advertising. These are claims.
- A 2025 breach of about 270,000 customer support tickets at Samsung Germany, which Hudson Rock linked to credentials stolen in 2021 and never rotated (per the article).
- A separate Samsung incident: TechCrunch and others reported smart TV apps containing code that shared owners' internet connections through a proxy network, after which Samsung banned them. The excerpts do not show the date clearly, and it is a different issue.

## Why a privacy and cyber hub should care

- **Behavioural data from consumer devices.** Even without content-level detail, location, ZIP code, time and provider data can be personal data in many regimes, and linking it to household identifiers raises re-identification risk. Whether these records are personal data depends on identifiers I could not see.
- **Ad-tech and political data.** Political affiliation and issue-targeting data fall into special-category or sensitive-data concepts in several regimes, if tied to individuals. The article says the records concern ads aired, not named individuals, so I draw no conclusion.
- **Training data and embeddings.** Leaked embedding vectors raise the question of whether vectors derived from personal data remain personal data, a live issue for AI governance. See the [irreversibility trap case](irreversibility-trap-fine-tuning.md).
- **Credential hygiene.** The article's Samsung Germany reference is a reminder that unrotated credentials can fuel breaches years later, as in other cases in this hub.
- **Ransomware claims.** Leak-site claims are often unverified and sometimes exaggerated, so a response plan needs a way to test them quickly. Compare the [Shukran loyalty data breach case](shukran-loyalty-data-breach-landmark-2026.md).

## Gaps and cautions

- Allegation only; Samsung has not confirmed the breach, and the authenticity and origin of the files are unverified.
- Single-source on the incident itself; the numbers are the article's.
- No date for the article in my summary, and the origin of the data (which Samsung system or partner) is not stated.
- Not legal or security advice.
