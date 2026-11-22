# Bridgewater: "Current Efforts Aren't Enough to Slow the AI Cyber Virus" (Nov 2026)

`AI and cyber risk · Patch windows · Open-source dependency · Policy responses (Japan, South Korea, US, UK) · Investment-firm research · Source: Bridgewater Associates`

Status as of 22 Nov 2026. The page is based on a tool-generated summary of Bridgewater's PDF version of the report (the document link, which is dated 13 Nov 2026), checked against an earlier summary of the web page. I did not read the PDF directly and the charts' values were not in the text I received. Figures below are as the summaries report them and have not been checked against the underlying data (CISA KEV, CVE counts). The PDF dates the report 13 Nov 2026; the web page metadata had shown 18 Nov 2026, probably the web publication date, which I have not confirmed.

## The source

Hudson Attar and Arham Habib, Bridgewater Associates, Research & Insights, © 2026: web page <https://www.bridgewater.com/research-and-insights/current-efforts-arent-enough-to-slow-the-ai-cyber-virus> and PDF <https://www.bridgewater.com/_document/current-efforts-arent-enough-to-slow-the-ai-cyber-virus?id=000001a1-d6ff-da40-a7e5-f6ff77190000>. This is an investment firm's client research, written for markets and macro readers, not a technical or peer-reviewed paper.

## Thesis

AI is speeding up attacks faster than defenders can patch. The authors say current defensive and policy efforts will not stop a continuing rise in damaging attacks, and expect things to worsen without a forceful, coordinated policy response.

## Main arguments (as summarised)

1. **Defensive discovery is accelerating, but bugs still get through.** Programmes such as Anthropic's Glasswing, OpenAI's Daybreak and Google's Fairwind are said to have produced a record number of discovered vulnerabilities. Defenders must fix every security-critical bug; attackers need one. Zero-day exploits are said to have roughly doubled since the first truly cyber-capable open-source models appeared.
2. **Shrinking patch window.** A published open-source patch reveals the flaw before downstream users have applied it. The average time from disclosure to exploitation is said to have fallen from about a month to 11 days.
3. **Policy is helpful but limited.** The authors say Japan's and South Korea's responses do not address dependence on volunteer- and nonprofit-maintained open-source software.
4. **Growing attack surface.** AI coding tools add very large volumes of new code, much of which will contain bugs; volume may outweigh any per-line safety gain.
5. **Temporary defender advantage.** The head start from Glasswing's launch before the summer release of cyber-capable open-source models is described as a one-time advantage that will erode. The authors suspect attackers are earlier on the learning curve but improving quickly. Attackers are not yet broadly using fully autonomous workflows, but open-source models are said to be close.

## Method and evidence claimed

- The authors say they built an incident time series, a root-cause taxonomy and a real-time exploit-tracking pipeline from public disclosures, media and corporate filings, adjusted for reporting lags. They report that incident counts and the AI-attributed share have "skyrocketed", and that practitioners called October "Black October".
- Evidence cited: a surge in CVE submissions, rising counts in CISA's Known Exploited Vulnerabilities catalogue, and growth in Bridgewater's own code output.
- Bridgewater says it is managing money on a one-in-three chance of an economically destabilising cyberattack in the next year. This is the firm's positioning, not an independent estimate.
- The authors say they lack full details on a recent Microsoft outage and a series of vishing campaigns against major financial firms. They argue such outages deserve attention even without confirmed malicious activity, because waiting for proof of damaging attacks could be too late for markets.
- The charts reportedly show incident counts and the AI-attributed share, CVE submissions, CISA KEV additions split into n-days and zero-days, and Bridgewater's internal code production; I did not see the values.

## Policy landscape described

| Jurisdiction | Measure as summarised |
|---|---|
| Japan (Oct) | Active cyber-defence powers enabled, letting police and the Self-Defense Forces access and disable attacker servers; an independent oversight commission set up in Apr 2026; an emergency package with initial funding of ¥10bn (about US$63m) creating a METI AI "top gun" team, a public/private cyber rescue team and a hardening team for vulnerable companies |
| South Korea (Oct) | October legislation with a 24-hour incident reporting deadline, turnover-based fines of up to 3% of sales for repeated incidents, and mandatory executive-level CISOs. Separately, the privacy law's maximum penalty for large-scale data leaks rises to 10% of sales from 3%. The PDF summary presents these as two different measures, which resolves the apparent conflict in the earlier summary |
| United States (Aug) | Presidential memorandum for a programme authorising vetted private firms to run cyber operations against foreign cybercriminal groups under federal control |
| United Kingdom | Cyber Security and Resilience Bill strengthens requirements for essential services and suppliers, including reporting within 24 hours and a full report within 72 hours of a major incident |

The report says Japan and South Korea are mobilising after waves of attacks on financial institutions and that Western initiatives are more limited. It has no formal recommendations section; its implicit call is for immediate and forceful coordinated policy on supporting open-source maintainers, speeding adoption of fixes and overseeing defensive AI deployment. The earlier summary quoted the authors as calling the effectiveness of these measures unclear and untested, and named three gaps: under-resourced open-source maintainers, the need for faster downstream patching, and reliance on AI labs to balance speed against containment and misalignment risk.

## Why a privacy and cyber hub should care

- **Patching and vulnerability SLAs.** An 11-day disclosure-to-exploitation figure, if accurate, challenges patch cycles measured in weeks. See the [Java4Shell page](java4shell-cisa-alert-hotspot-base64-2026.md) for a live example of a fast-moving patch advisory.
- **Third-party and open-source dependency.** The argument rests on software supply chains, which links to the [Optimizely case](../case-studies/optimizely-third-party-script-compromise-178-sites-2026.md).
- **Incident-reporting clocks.** The 24-hour and 72-hour requirements in Korea and the UK would sit alongside GDPR's 72 hours and sector rules.
- **Board and disclosure risk.** A market-facing firm treating a major cyberattack as a one-in-three event shows how this risk is being framed for investors.

## Gaps and cautions

- Not read directly (tool summaries of the web page and the PDF); charts not seen; the figures are unverified.
- Authors' forecasts and a firm's positioning, not neutral measurement. The methodology is described only at a high level and cannot be reproduced from the summary.
- Unconfirmed incidents (Microsoft outages, vishing) are expressly not attributed to attackers.
- The report carries standard disclaimers: informational only, not investment advice, Bridgewater's positions may differ from its conclusions and it may hold interests in the positions discussed, data comes from third-party sources not guaranteed accurate, and redistribution requires written consent. I paraphrase and do not reproduce it.
- Not investment, legal or security advice.
