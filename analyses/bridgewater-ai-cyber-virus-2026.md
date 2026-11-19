# Bridgewater: "Current Efforts Aren't Enough to Slow the AI Cyber Virus" (Nov 2026)

`AI and cyber risk · Patch windows · Open-source dependency · Policy responses (Japan, South Korea, US, UK) · Investment-firm research · Source: Bridgewater Associates`

Status as of 19 Nov 2026. The page is based on a tool-generated summary of the Bridgewater web page, not a direct reading of the page, and the charts were not in the text I received. Figures below are as the summary reported them and have not been checked against the page or against the underlying data (CISA KEV, CVE counts). The summary lists the article date as 13 Nov 2026 while the page metadata shows 18 Nov 2026; I have not resolved which is right.

## The source

Hudson Attar and Arham Habib, Bridgewater Associates, Research & Insights: <https://www.bridgewater.com/research-and-insights/current-efforts-arent-enough-to-slow-the-ai-cyber-virus>. This is an investment firm's client research, written for markets and macro readers, not a technical or peer-reviewed paper.

## Thesis

AI is speeding up attacks faster than defenders can patch. The authors say current defensive and policy efforts will not stop a continuing rise in damaging attacks, and expect things to worsen without a forceful, coordinated policy response.

## Main arguments (as summarised)

1. **Asymmetry.** Defenders must fix every security-critical bug; attackers need one. Zero-day exploits are said to have roughly doubled since the first truly cyber-capable open-source models appeared.
2. **Shrinking patch window.** A published open-source patch reveals the flaw before downstream users have applied it. The average time from disclosure to exploitation is said to have fallen from about a month to 11 days.
3. **Policy is helpful but limited.** The authors say Japan's and South Korea's responses do not address dependence on volunteer- and nonprofit-maintained open-source software.
4. **Growing attack surface.** AI coding tools add very large volumes of new code, much of which will contain bugs; volume may outweigh any per-line safety gain.
5. **Temporary defender advantage.** The head start between Anthropic's Glasswing launch and the arrival of cyber-capable open-source models is described as a one-time gift that will erode. Attackers are not yet broadly using fully autonomous workflows, but open-source models are said to be close.

## Method and evidence claimed

- The authors say they built an incident time series, a root-cause taxonomy and a real-time exploit-tracking pipeline from public disclosures, media and corporate filings, adjusted for reporting lags. They report that incident counts and the AI-attributed share have "skyrocketed", and that practitioners called October "Black October".
- Evidence cited: a surge in CVE submissions, rising counts in CISA's Known Exploited Vulnerabilities catalogue, and growth in Bridgewater's own code output.
- Bridgewater says it is managing money on a one-in-three chance of an economically destabilising cyberattack in the next year. This is the firm's positioning, not an independent estimate.
- The authors say they lack full details on recent Microsoft outages and vishing campaigns against financial firms, and that malicious involvement is unconfirmed.

## Policy landscape described

| Jurisdiction | Measure as summarised |
|---|---|
| Japan (Oct) | Active cyber-defence powers, with an oversight commission set up in Apr 2026; an emergency package including a METI AI "top gun" team and a public/private "cyber rescue team"; ¥10bn (about US$63m) allocated |
| South Korea (Oct) | Proposed 24-hour incident reporting, turnover-based fines and mandatory executive-level CISOs; the summary gives penalties of up to 10% of sales for large-scale leaks (up from 3%) and up to 3% for repeated incidents. These two fine statements sit uneasily together, so check the original |
| United States (Aug) | Presidential memorandum for a programme authorising vetted private firms to run cyber operations against foreign cybercriminal groups under federal control |
| United Kingdom | Cyber Security and Resilience Bill: report a major incident within 24 hours and file a full report within 72 hours |

The authors call the effectiveness of these measures unclear and untested, and name three gaps: under-resourced open-source maintainers, the need for faster downstream patching, and reliance on AI labs to balance speed against containment and misalignment risk.

## Why a privacy and cyber hub should care

- **Patching and vulnerability SLAs.** An 11-day disclosure-to-exploitation figure, if accurate, challenges patch cycles measured in weeks. See the [Java4Shell page](java4shell-cisa-alert-hotspot-base64-2026.md) for a live example of a fast-moving patch advisory.
- **Third-party and open-source dependency.** The argument rests on software supply chains, which links to the [Optimizely case](../case-studies/optimizely-third-party-script-compromise-178-sites-2026.md).
- **Incident-reporting clocks.** The 24-hour and 72-hour proposals in Korea and the UK would sit alongside GDPR's 72 hours and sector rules.
- **Board and disclosure risk.** A market-facing firm treating a major cyberattack as a one-in-three event shows how this risk is being framed for investors.

## Gaps and cautions

- Not read directly; charts not seen; the figures are unverified.
- Authors' forecasts and a firm's positioning, not neutral measurement. The methodology is described only at a high level and cannot be reproduced from the summary.
- Unconfirmed incidents (Microsoft outages, vishing) are expressly not attributed to attackers.
- Not investment, legal or security advice.
