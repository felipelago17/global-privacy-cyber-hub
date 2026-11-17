# Hands-on training labs

Status as of 17 Nov 2026. A short guide to places where privacy, security and governance practitioners can practise how attacks and defences work, so that policy and control decisions rest on first-hand understanding. Reading about an incident (see the [case studies](../case-studies/README.md)) and reproducing the technique in a safe lab teach different things.

| Page | What it covers |
|---|---|
| [AI security and red-teaming labs](ai-security-labs.md) | Prompt-injection games, AI CTFs and web LLM labs; descriptions checked against operator or published sources where reachable |
| [Foundations, offensive, cloud and defensive labs](cyber-labs-foundations-to-defence.md) | 17 general cybersecurity platforms from the same source list; pointers only, not individually checked |

## Why a privacy and cyber hub lists labs

- **Agent and LLM risks become concrete.** The [AI agents section](../ai-agents/index.md) describes prompt injection, excessive agency and data exfiltration. Labs let you see these failures happen and judge which controls would have stopped them.
- **Cloud and web misconfiguration is a data-protection issue.** Exposed storage, over-broad identity roles and third-party script compromise (see the [Optimizely case study](../case-studies/optimizely-third-party-script-compromise-178-sites-2026.md)) are common routes to personal-data incidents.
- **Defensive practice supports incident response.** Detection and forensics exercises build the skills behind breach-notification decisions.

## Safe-use rules

1. Attack only the environments an operator provides for that purpose.
2. Do not enter real personal data, real credentials or employer information into any lab or AI challenge.
3. Read each platform's privacy notice. Some labs collect telemetry, including AI interaction logs.
4. Check terms and licences before reusing any challenge dataset or publishing attack prompts.
5. Results from live-LLM labs vary between attempts and are not benchmark scores.

## Source note

The starting list came from a social-media post that collected 23 labs; it is not cited here. Entries were checked where noted on each page. No lab was run for this hub, and links were not tested.
