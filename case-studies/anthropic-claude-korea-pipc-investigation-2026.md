# Anthropic / Claude: South Korean PIPC investigation after vendor-software intrusion

`Third-party / SaaS risk · Bug bounty scope · Enterprise account metadata · Cross-border breach notification · South Korea PIPA · Status: investigation open`

Status as of 13 Nov 2026. The matter is developing; no findings have been published.

## Summary

A US security start-up, Cathedral, used AI agents to reach parts of Anthropic's internal business systems through weaknesses in third-party software used for sales and administration, not through Claude itself. The testing took place under Anthropic's bug bounty programme. Anthropic told South Korea's Personal Information Protection Commission (PIPC) on 31 Oct 2026 that information tied to roughly 100 or more Korean corporate Claude accounts may have been exposed. On 10 Nov 2026 MLex reported that the PIPC will open a formal investigation.

## Timeline

| Date (2026) | Event | Source basis |
|---|---|---|
| Early Oct | Cathedral tests Anthropic business systems under the bug bounty programme (exact dates, around 8 to 10 Oct, come from a secondary summary and are not confirmed) | Reported |
| 26 Oct | The Washington Post reports the incident, citing a draft Cathedral report; Cathedral says its agents found paths in under 12 hours | Press |
| 31 Oct | Anthropic reports the incident to the PIPC | PIPC via Yonhap |
| 8 Nov | An Anthropic staff post says prompts, outputs and payment information were not accessed | Press |
| 9 Nov | PIPC confirms it received the report and says it is in preliminary review | Yonhap |
| 10 Nov | MLex reports a PIPC spokesperson said a formal investigation will open | MLex |

## What is disputed and what is claimed

- **Scope of access.** Cathedral's draft report, as described by the Post, claims broad access to internal data and messaging systems. Anthropic says the researchers reached a limited set of sales, HR and IT systems and that source code and model weights were not accessed.
- **Programme rules.** Anthropic says Cathedral did not fully disclose its activity and so broke the bounty rules. Cathedral says it kept data access to a minimum. Anthropic also says Cathedral overstated national-security implications.
- **Data in the Korean report.** Reported categories are account and organisation identifiers, names, business email addresses and subscription plan details. Some coverage adds usage and spend metrics; I did not confirm that from a primary source.
- **Number of accounts.** Most outlets say "about 100"; MLex says "more than 100"; a figure of about 112 appears in a secondary summary and is not confirmed.

## What is not public

- Anthropic has not, as far as I found, published its own incident report or named the vendor.
- The PIPC's legal basis, the provisions of the Personal Information Protection Act under review, and any timetable are not public.
- Reports that the Ministry of Science and ICT is also examining the incident, and that customers were notified around 7 Nov, come from a secondary summary and were not confirmed here.
- Whether deletion of the accessed data was confirmed in writing by Cathedral rests on the same summary.

## Why it matters

1. **A metadata exposure is still personal data.** Business names and work emails of employees are personal information in most regimes. "No prompts or outputs accessed" narrows the harm but does not remove notification or regulator interest.
2. **Third-party and SaaS risk sits behind the headline.** The weakness was in business software, not the core product. Vendor inventories and patch obligations for internal tooling matter as much as the product's own security.
3. **Bug bounty scope is a legal boundary.** The dispute over what counted as in-scope testing shows why programme terms, disclosure duties and stop conditions need clear drafting, especially when AI agents widen the reach of a test. Compare the [Uber/Sullivan case](uber-sullivan-ciso-obstruction.md) on bounty handling.
4. **Regulators in the customer's country can act on a foreign provider.** The PIPC is reviewing an overseas company on the basis of Korean enterprise accounts. Overseas reviews can involve document requests and take time.
5. **Customer-side lesson.** Enterprises using AI services should know which account metadata the provider holds, how incidents are notified under the contract, and which regulators each affected business must itself notify.

## Framework mapping

| Framework | Relevance |
|---|---|
| South Korea PIPA | Breach notification and security safeguards for personal information; the PIPC's formal investigation will test both (provisions to be confirmed) |
| NIS2 Art. 21(2)(d) | Supply-chain security applies by analogy to the vendor-software route |
| GDPR Arts. 33 to 34 | Comparable notification duties would apply to any EU personal data in the affected systems; not alleged here |
| Vendor risk management | Software inventory, patching SLAs, tenant isolation for admin and sales tooling |
| Bug bounty governance | Scope, safe harbour, disclosure duties, AI-agent testing rules |

## Related

- [Operation Snowball and AI agents](operation-snowball-ai-agent-2026.md)
- [OpenAI / Hugging Face incident](openai-hugging-face-2026.md)
- [Luxembourg NIS2 reporting](../analyses/nis2-luxembourg-ilr-security-measures-reporting-2027.md)

## Sources

- MLex, Jenny Lee, "Anthropic faces South Korean privacy investigation over Claude account data exposure" (10 Nov 2026): <https://www.mlex.com/mlex/articles/2548285>
- Yonhap via Money Today, "Anthropic's Claude suffers personal data breach" (9 Nov 2026): <https://www.mt.co.kr/en/economy/2026/11/09/2026110920322255936>
- Decrypt, "AI agents found a way into Anthropic's business systems in under 12 hours": <https://decrypt.co/381860/ai-agents-hack-anthropic-business-systems-12-hours>
- TechRadar, "AI startup claims it hacked Anthropic in 12 hours": <https://techradar.com/pro/security/ai-startup-claims-it-hacked-anthropic-in-12-hours-gains-access-to-employee-details-and-internal-messages>
- Let's Data Science summary of the Washington Post report of 26 Oct 2026: <https://letsdatascience.com/news/startup-cathedral-says-ai-agents-reached-anthropic-systems-i-d2d81cc2>
- OECD AI Incidents Monitor entry (9 Nov 2026): <https://oecd.ai/en/incidents/2026-11-09-3f76>
- Data Studios, incident timeline and Korean filing (secondary): <https://www.datastudios.org/post/anthropic-claude-account-data-exposure-100-korean-companies-cathedral-pipc>
