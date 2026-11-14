# "Your attackers' AI knows you better than yours does" (Forbes Technology Council, 13 Nov 2026)

`AI-enabled attacks · Security fundamentals · Attack path analysis · Japan and South Korea 2026 · Commentary (vendor author, paid Council Post)`

Status as of 14 Nov 2026. This page summarises one opinion piece and checks its main examples against other public reporting.

## The piece

Kumar Ritesh, founder and CEO of CYFIRMA (an AI-driven threat-intelligence firm), wrote a Forbes Technology Council post dated 13 Nov 2026: <https://www.forbes.com/councils/forbestechcouncil/2026/11/13/your-attackers-ai-knows-you-better-than-yours-does/>. It is a paid Council Post and the author's company sells in this area, which bears on its recommendations. The summary below is paraphrased.

## The argument

AI is now needed for defence because attacks move at machine speed, but it only multiplies the posture underneath it: if the basics are weak, AI does not fix them. The author argues the 2026 attacks in Japan and South Korea succeeded by exploiting known, unfixed weaknesses, not because attackers had better models.

## Examples and what other sources say

| Claim in the piece | Check against other reporting |
|---|---|
| Japan declared its first cyber "state of emergency" on 9 Oct 2026 after ransomware spread through IDC Frontier, a SoftBank-owned cloud provider, reaching nearly 500 clients | IDC Frontier confirmed ransomware on its IDCF Cloud East Japan Region 1 from 7 Oct, affecting 495 companies and local governments, with virtual servers in four zones unable to restart. A security-vendor advisory says Japan's National Cybersecurity Strategy Headquarters declared an emergency on 9 Oct. I did not find a government source for the declaration |
| An open-source AI agent "worked through" seven South Korean banks and lenders; credential stuffing run by ARTEX | Seven institutions were hit between late September and early October, with roughly 65,000 to 68,000 people's data exposed. ARTEX, an open-source Chinese agentic pentesting tool, was identified in at least one attack. Reporting says its role in all seven is not established, credential stuffing and weakly protected side systems could also explain the intrusions, and a human may still have been driving |
| Teenagers arrested in Japan for using ChatGPT in mobile-line hijacking and a 7.25-million-record theft; Kimsuky used ChatGPT to help forge a Korean military ID | Not checked |
| Anthropic's Nov 2025 disclosure of a campaign where AI performed about 80% to 90% of tactical work | Matches the GTG-1002 entry in the hub's [incident catalogue](../ai-agents/incident-catalogue.md) |
| Best open-weight models match closed frontier models at finding vulnerabilities at a fraction of the cost | An assertion by the author; not supported in the piece by a cited measurement I could check |

## Recommended actions in the piece

- Start with sector-specific threat modelling, then choose a detection model.
- Feed AI outside-in data (what is discussed, sold, scanned or staged about the organisation), not only internal logs.
- Use attack path analysis rather than vulnerability lists, and break the cheapest link on each path.
- Keep a reliable asset inventory and a third-party map so tools have context.
- Commission an external threat assessment for exposed assets, leaked credentials and contractor weaknesses.

## Why it matters for privacy and cyber teams

1. **The thesis is useful and testable.** The attacks it cites mostly used weak authorisation, exposed admin interfaces, embedded keys, unpatched flaws and credential reuse. These are controls a privacy or security programme can audit regardless of AI.
2. **Concentration risk shows up in the examples.** One cloud provider outage reaching about 500 organisations is an operational-resilience and vendor-dependency case as much as a ransomware case; see [cloud concentration](cloud-centrality-menace-technollama-2026.md).
3. **Be careful with attribution to AI.** Where the evidence is traces of a tool on servers, the claim that an agent carried out the attack may overstate what is known. Incident reports should separate what is observed from what is inferred.
4. **Vendor-authored guidance.** Recommending outside-in threat intelligence is consistent with the author's business. The advice is reasonable but should be judged against alternatives such as basic exposure management and identity hardening.

## What this page does not establish

- I did not verify the arrests, the Kimsuky claim or the open-weight model cost claim.
- The Japanese emergency declaration rests on a secondary vendor source.
- Nothing here measures how much AI changed attacker success compared with earlier tools.

## Sources

- Kumar Ritesh, "Your Attackers' AI Knows You Better Than Yours Does", Forbes Technology Council (13 Nov 2026): <https://www.forbes.com/councils/forbestechcouncil/2026/11/13/your-attackers-ai-knows-you-better-than-yours-does/>
- teiss, "Ransomware attack on IDC Frontier affects nearly 500 organisations in Japan" (14 Oct 2026): <https://www.teiss.co.uk/news/ransomware-attack-on-idc-frontier-affects-nearly-500-organisations-in-japan-18305>
- SDxCentral on the IDC Frontier attack (9 Oct 2026): <https://www.sdxcentral.com/news/softbank-national-cloud-arm-attacked-in-seven-minutes-taking-japan-infrastructure-offline/>
- UV Cyber threat advisory on Japan's cyber emergency: <https://www.uvcyber.com/resources/threat-advisories/threat-advisory-japans-cyber-emergency-and-its-ripple-effects>
- Cloud Security Alliance research note on ARTEX and South Korean bank intrusions: <https://labs.cloudsecurityalliance.org/research/csa-research-note-artex-agentic-pentest-bank-breaches-202610/>
- Orca Router, "Korean banks breached with an open-source AI pentest agent": <https://www.orcarouter.ai/blog/2026-10-06-artex-ai-south-korea-banks>
- Security Point Break, South Korea bank hacks (7 Oct 2026): <https://securitypointbreak.com/2026/10/07/beyond-shinhan-south-koreas-bank-hacks-hit-66000-with-an-ai-clue/>
