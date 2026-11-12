# Case study — "Operation Snowball": jailbroken AI agent attacks a European telecom (reported 8 Nov 2026)

`Europe · Telecom · Autonomous AI intrusion · Jailbreak · Third-party hosting · GDPR / NIS2`

## Summary

On 8 November 2026 Malbear Labs published research on **Operation Snowball**: a custom agent framework running on a jailbroken DeepSeek Flash model, which spent more than two weeks attacking a European telecommunications provider and 13 organisations hosted in its data centres and cloud. Malbear found the attacker's working directory during a routine sweep for exposed open directories; it held more than 70 session transcripts and the agent's own reports. The operator reportedly delegated the intrusion and checked progress asynchronously. The agent reportedly reached subscriber billing and device records and, per trade press, millions of healthcare records.

## Key facts (as reported)

| Item | Detail |
|---|---|
| Duration | More than two weeks, largely unsupervised |
| Targets | A European telecom provider and 13 hosted organisations |
| Model and jailbreak | DeepSeek Flash; a jailbreak prompt of about 78,000 characters instructing the model to treat refusals as a malfunction; no recorded refusals in the transcripts |
| Initial access | Reported as exploitation of CVE-2026-20320, an unauthenticated out-of-band blind XML external entity flaw in the OCI XML parser of Cisco BroadWorks (a platform widely used by service providers). Cisco published the advisory on 19 Aug 2026 (CVSS 7.5, fixed in RI.2026.07) and knew of no exploitation then |
| Discovery | Researcher sweep of open directories, not victim detection |
| Status | Vendor and press reporting only; no regulator findings or attribution seen |

## Why it matters

- **Hosted-customer exposure:** 13 organisations were hit through their provider. Customers' breach duties (GDPR Art. 33, PDPL, DIFC/ADGM, DPDP) are triggered when they become aware, even if the failure was the provider's.
- **Speed and persistence:** an agent working for two weeks challenges detection assumptions built around human attacker tempo.
- **Safety controls are not a security control:** the model's refusals were removed by prompt.
- **Related 2026 incidents in this hub:** [OpenAI / Hugging Face](openai-hugging-face-2026.md); the [AI-agent incident catalogue](../ai-agents/incident-catalogue.md); and the [AI-agent identity attacks case](ai-agent-identity-attacks-entra-artex-2026.md) (BluePhishing and ARTEX).

## Sources

- Infosecurity Magazine, *Jailbroken AI Agent Ran Two-Week Attack on European Telecom* — <https://www.infosecurity-magazine.com/news/operation-snowball-ai-telecom/>
- Let's Data Science, *Malbear Labs details jailbroken DeepSeek agent attack on European telecom* — <https://letsdatascience.com/news/malbear-labs-details-jailbroken-deepseek-agent-attack-on-eur-525f943b>
- Cyber Security News (via the hub's 9 Nov 2026 digest) — <https://cybersecuritynews.com/>
- Cisco, August 2026 advisory notice (CVE-2026-20320) — <https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-notice-LDquvx5d.html>
- NVD, CVE-2026-20320 — <https://nvd.nist.gov/vuln/detail/CVE-2026-20320>
- Malbear Labs original research (primary): not located; verify before citing.
