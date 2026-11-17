# Optimizely third-party script compromise: 178 organisations, 188 scripts (Newsweek, 17 Nov 2026)

`Web supply chain · Third-party JavaScript · Client-side skimming · Crypto-address swapping · Status: vendor says fixed, impact unknown`

Status as of 17 Nov 2026. Everything below comes from one Newsweek article by Chris Matthews, published 17 Nov 2026 ("Cyber attack hits 178 major websites: full list of organizations"): <https://www.newsweek.com/cyber-attack-websites-affected-12725863>. I could not find Report URI's own write-up of this incident or Optimizely's status page, so the researcher findings and the vendor statement are second-hand. Newsweek paraphrases Optimizely rather than quoting it.

## Summary

Attackers did not breach each organisation. Per Newsweek, they exploited a vulnerability in Optimizely, a website-testing service, and tampered with it so that malicious code ran on the sites that used the service. Visitors could be exposed just by opening an affected site. Report URI researchers identified the attack on Monday 16 Nov; Optimizely posted a status update on Tuesday 17 Nov saying it had fixed the problem and removed the malicious code. Newsweek does not attribute the attack to any actor.

## Scale (as reported)

- 178 organisations and 188 affected website scripts.
- Named examples: Zoom, BBC, CNN, HSBC, IKEA, Salesforce, Equifax, Fox News, Alaska Airlines, GitLab. Newsweek cautions that the list may be incomplete.
- By sector: banking and finance 32, technology and software 23, retail and fashion 20, streaming and entertainment 12, news and media 10, airlines and travel 9, healthcare and pharmaceuticals 8, industrial and manufacturing 8, telecoms 7, crypto and trading 6, insurance 6, property 6, with smaller counts in other sectors.
- About USD 7,040 in cryptocurrency payments traced to linked wallets. Total financial impact and number of victims are unknown.

## What the malicious code could do (per the researchers)

- Swap copied cryptocurrency wallet addresses so payments go elsewhere.
- Steal credit-card details.
- Read information stored in the browser and capture screenshots.
- Target older iOS versions on iPhones and iPads.

Newsweek says it is unclear how many people, if any, had data stolen, and that visiting an affected site does not mean data was taken.

## Timeline

| Date (2026) | Event |
|---|---|
| 16 Nov | Attack observed; Report URI identifies it; traced crypto payments dated to this day |
| 17 Nov | Optimizely status update: fixed, malicious code removed; Newsweek publishes |

## Why it matters

1. **One vendor, many victims.** The 178 organisations had no shared flaw of their own. They shared a script supplier. The affected firms span banks, media, airlines and healthcare, so sector-specific controls would not have helped; script-level controls would.
2. **Large, well-resourced firms are included.** Brand size and strong server-side security do not protect against code that the browser loads from a trusted third party.
3. **Data-protection angle.** If payment or personal data was captured in visitors' browsers, the website owner is likely the controller and could face notification and security-of-processing questions even though the compromise sat with a vendor. Whether any such data was captured here is not established.
4. **Short window, delayed visibility.** Reported impact started on 16 Nov and the fix came the next day, but organisations that do not log third-party script changes may not know whether they were exposed.
5. **Same pattern as earlier cases.** Compare Polyfill.io (June 2024), where a Report URI case study describes a domain acquisition leading to malicious JavaScript on 100,000+ sites. The mechanism there was a changed owner; here, per Newsweek, it was a vulnerability in a service.

## Controls to test

- Inventory every third-party script on payment, login and account pages, with an owner and a business reason for each.
- Use Content Security Policy and Subresource Integrity where the vendor allows them; note that hash pinning (Subresource Integrity) does not work for scripts that legitimately change often, which is how experimentation tools behave, so monitoring is needed as well.
- Monitor for script changes and unexpected outbound connections from the browser (for example with CSP reporting, which is Report URI's core service).
- Remove testing and analytics tags from sensitive pages such as checkout where they are not needed.
- Contract terms: vendor security requirements, incident notification timelines, and who tells the website owner when a script is tampered with.
- For users and staff: update devices, check for unfamiliar payments, and verify crypto addresses before sending (Newsweek's advice).

## Gaps and cautions

- Single secondary source. Not checked: Report URI's findings, Optimizely's status page or root cause, the vulnerability type, which Optimizely product was involved, the duration of exposure, or whether any listed organisation has confirmed impact.
- "Affected" means the organisation's site loaded a tampered script, not that the organisation was breached or that data was stolen.
- No CVE, no attribution, no regulator action reported.
- Separate context, not part of this incident: Report URI's Scott Helme wrote on 6 Nov 2026 that Report URI had identified 15,579 sites serving malicious JavaScript (reported by secondary sites; I did not read the original post).
