# Case study — AI-agent identity attacks: BluePhishing and ARTEX (November 2026)

`Cloud identity · Microsoft Entra Agent ID · OAuth consent · Exposed secrets · Agentic offensive tooling`

## Summary

Two November 2026 disclosures show attackers targeting the identity layer that agent platforms create. **BluePhishing** (Proofpoint) extends OAuth consent phishing to agent identities: an attacker socially engineers a victim into granting consent to a malicious *agent blueprint* in Microsoft Entra Agent ID, gaining initial access without stealing a password. **ARTEX** (Microsoft Threat Intelligence, 5 November 2026) is an agentic offensive framework that searches public GitHub repositories for exposed credentials, application secrets and AI API keys; in one observed case an agent went from scanning GitHub to exfiltrating Azure Key Vault data in five minutes.

## Key facts

| Item | Detail |
|---|---|
| BluePhishing | Proofpoint research; consent to a third-party agent blueprint gives the attacker an agent identity in the tenant |
| ARTEX | Observed since August 2026 per trade reporting; a follow-on activity from 28 October used valid leaked application credentials to sign in to Entra tenants |
| Speed | One case: five minutes from GitHub scan to Key Vault exfiltration (a single data point, not a baseline) |
| Mitigations advised by Microsoft | Scan code for secrets, rotate exposed keys, use managed identities |
| CSA view (9 Nov 2026) | Scheduled rotation alone no longer bounds exposure |

## Why it matters

- **New consent surface:** approving an agent is now an access decision; consent workflows need security review.
- **Secrets hygiene is a "reasonable measures" question:** exposed secrets in public repositories convert quickly into data breaches with notification duties.
- **Offboarding:** leavers' tokens, service principals and agent identities must be revoked as well as their accounts.
- Related: [Operation Snowball](operation-snowball-ai-agent-2026.md); [OpenAI / Hugging Face](openai-hugging-face-2026.md).

## Sources

- Proofpoint, *BluePhishing: Initial Access via Third-Party Agent Blueprint Consent* — <https://www.proofpoint.com/us/blog/threat-insight/BluePhishing-Initial-Access-via-Third-Party-Agent-Blueprint-Consent>
- Let's Data Science, *Microsoft reports threat actors using ARTEX agentic tooling to abuse exposed secrets* — <https://letsdatascience.com/news/microsoft-reports-threat-actors-using-artex-agentic-tooling-15b88fc8>
- Cloud Security Alliance, *Five Minutes from Search to Key Vault: Agentic Secret Harvesting* (9 Nov 2026) — <https://labs.cloudsecurityalliance.org/research/csa-research-note-agentic-secret-harvesting-rotation-windows/>
- Fourweekmba summary of Microsoft's report — <https://fourweekmba.com/ai-microsoft-ai-agent-took-5-minutes-from-github-to-key-vault/>
- Microsoft's original post: not opened; verify before citing.
