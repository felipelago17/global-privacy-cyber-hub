# Twenty cybersecurity reference sites

`Reference sites · Vulnerability data · Frameworks · Detection · Threat intelligence`

Status as of 18 Nov 2026. This page records a social-media graphic titled "20 Cybersecurity Websites to Know", credited on the image to Excellog.Biz and seen as a LinkedIn screenshot. The one-line purposes below are the graphic's own wording, lightly reworded. I did not open or test any site, so treat this as a pointer list, not a vetted source list. The graphic gives site names only; the operator of each site is my addition from general knowledge and should be checked.

| # | Site | Purpose per the graphic | Group |
|---|---|---|---|
| 1 | cisa.gov | Track actively exploited vulnerabilities | Vulnerability data |
| 2 | nvd.nist.gov | Inspect CVEs and risk data | Vulnerability data |
| 3 | first.org/epss | Estimate the chance a CVE is exploited | Vulnerability data |
| 4 | attack.mitre.org | Map adversary tactics | Frameworks |
| 5 | d3fend.mitre.org | Explore defensive techniques | Frameworks |
| 6 | atlas.mitre.org | Map attacks against AI systems | Frameworks |
| 7 | cwe.mitre.org | Study software weaknesses | Frameworks |
| 8 | nist.gov/cyberframework | Structure cyber risk | Frameworks |
| 9 | asvs.owasp.org | Review application security requirements | Frameworks |
| 10 | genai.owasp.org | Explore LLM and agent risks | Frameworks |
| 11 | portswigger.net/web-security | Free web labs | Practice |
| 12 | cylabacademy.org | Free cybersecurity CTFs | Practice |
| 13 | gchq.github.io/CyberChef | Decode data | Tools |
| 14 | wireshark.org | Inspect network packet captures | Tools |
| 15 | zeek.org | Generate network security logs | Tools |
| 16 | sigmahq.io | Shareable detection rules | Detection |
| 17 | abuse.ch | Research malware and threat intelligence | Threat intelligence |
| 18 | urlscan.io | Inspect site requests and redirects | Threat intelligence |
| 19 | shodan.io | Find internet-exposed services | Threat intelligence |
| 20 | ssllabs.com/ssltest | Test HTTPS and TLS settings | Hardening |

## Where they connect to this hub

- **Vulnerability data (1 to 3)** support patch-priority and breach-risk judgements. KEV-style "actively exploited" lists and exploit-probability scores are inputs to risk-based remediation, relevant to the [Optimizely third-party script case](../case-studies/optimizely-third-party-script-compromise-178-sites-2026.md).
- **AI frameworks (6 and 10)** pair with the [AI agents section](../ai-agents/index.md) and the [AI security labs](ai-security-labs.md), which cover the same attack classes in practice.
- **Practice sites (11 and 12)** overlap with the [foundations to defence labs](cyber-labs-foundations-to-defence.md); PortSwigger also appears on the AI labs page for its web LLM labs.
- **Exposure and TLS tools (18 to 20)** map to the external-attack-surface checks that DPAs and incident reviews often cite. Use scanning tools only on assets you own or are authorised to test; Shodan and urlscan.io results can also expose third-party data.

## Cautions

- Source is a social-media graphic with no commentary; I have not verified that each URL is current or the preferred landing page.
- Descriptions are the graphic's, not the operators'.
- Follow the [safe-use rules](README.md).
