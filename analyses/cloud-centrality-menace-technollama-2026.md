# Attack of the clouds: the "centrality menace" revisited (TechnoLlama, Nov 2026)

`Cloud concentration · Operational resilience · Digital sovereignty · DORA · UK critical third parties · Commentary`

Status as of 14 Nov 2026. This page summarises one commentary post; it is not a statement of law.

## The piece

Andres Guadamuz, "Attack of the clouds: the centrality menace revisited", TechnoLlama (13 Nov 2026): <https://www.technollama.co.uk/attack-of-the-clouds-the-centrality-menace-revisited>. The post uses a Microsoft 365 outage that began on a Thursday afternoon in the UK to revisit an argument the author first made after a 2013 Cloudflare outage. The summary below is paraphrased from my reading of the post.

## The argument

Cloud services were meant to make the web more distributed, but many services now depend on a few central points, so one failure can hit many organisations at once. In 2013 the single point of failure was a DNS name server. For the 2026 outage the author suggests it was the system that decides which servers are healthy: automated failover moved traffic onto remaining servers that were then overloaded, and recovered servers failed again as soon as they received traffic, which he compares to a self-inflicted DDoS. That diagnosis is his own suggestion, not a confirmed root cause.

| Theme | Point made |
|---|---|
| Growing stakes | Earlier outages mostly hit websites. Now email, calendars, documents, meetings and identity depend on the cloud. The post lists disruption to UK GP surgeries, pharmacies, police forces, councils and universities, plus government and court systems elsewhere |
| Recent incidents | The 2024 CrowdStrike update failure, AWS and Cloudflare outages in 2025, and a January 2026 Microsoft 365 outage |
| Jurisdiction and sovereignty | Long-standing concern about dependence on US providers subject to US law, now framed by governments as digital sovereignty (the post cites the French government's move away from US video tools). European alternatives are limited and customers are locked into licences |
| Procurement | Each purchase is sensible, but together they create systemic risk |
| Regulation | DORA and the UK critical third parties regime treat financial firms' reliance on a few technology providers as systemic and give regulators oversight of those providers. The author argues hospitals, courts, police and universities deserve similar scrutiny |
| Proposed responses | Plan a "minimum viable service" that keeps essential functions running without the main provider; decentralise higher up the stack (identity, email, documents), at a cost; over the long term, use local tools and locally run agents to reduce dependence |
| Outlook | Pessimistic: outages will increase, centralisation is unlikely to be reversed, and AI may shift dependence to the few firms with enough compute |

The post does not substantively discuss GDPR, the Digital Markets Act or competition law.

## Why it matters for privacy and cyber teams

1. **Availability is a security objective.** GDPR Art. 32 names the ability to restore availability and access to personal data, and NIS2 Art. 21(2)(c) covers business continuity. A provider outage is a resilience failure even when no data is lost or exposed.
2. **Identity is the hidden single point of failure.** If the identity provider is down, sign-in to everything else fails, including incident tooling and communications. Break-glass accounts and out-of-band channels matter.
3. **Concentration is a supply-chain question.** Regulators increasingly ask for dependency maps and exit plans. See the [Luxembourg ILR NIS2 reporting](nis2-luxembourg-ilr-security-measures-reporting-2027.md), where regulators may request supplier and service-provider dependency lists.
4. **Sovereignty is a compliance input, not only politics.** Jurisdictional exposure to a provider's home law affects transfer assessments, government-access risk and exit options, which connects to the hub's [transatlantic transfers](transatlantic-transfers-ftc.md) page.
5. **"Minimum viable service" is testable.** Define which functions must run during a provider outage (for example, patient safety, emergency response, regulatory reporting), the offline fallback for each, and rehearse it.

## Practical questions

- Which of our critical processes would stop if our email, identity or collaboration provider failed for 24 hours?
- Do we hold an offline contact list, an out-of-band messaging channel and break-glass credentials that do not depend on the same provider?
- Do contracts give us credits only, or also incident reporting, root-cause analysis and exit support?
- Is this dependency covered by our regulator's third-party rules (DORA, UK CTP, NIS2), and by our board's risk appetite?

## What this page does not establish

- I could not confirm the cause, scope or duration of the Microsoft 365 outage the post describes. Searches returned other 2026 Microsoft incidents (for example 21 Jan, 8 Apr, 31 Aug and 9 Nov 2026), and I did not find a Microsoft post-incident report for the Thursday outage. Treat the post's causal explanation as the author's hypothesis.
- The post's examples of affected public bodies and its list of past incidents were not independently checked.
- Nothing here is legal advice, and the application of DORA, the UK CTP regime or NIS2 to any entity depends on its sector and status.

## Sources

- Andres Guadamuz, "Attack of the clouds: the centrality menace revisited", TechnoLlama (13 Nov 2026): <https://www.technollama.co.uk/attack-of-the-clouds-the-centrality-menace-revisited>
