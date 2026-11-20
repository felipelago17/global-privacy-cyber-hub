# CFR (Adam Segal): why a run of tech outages looks more like fragility than attack (Nov 2026)

`Systemic outages · AI-accelerated patching · Attribution caution · Critical infrastructure · Incident communication · Source: Council on Foreign Relations`

Status as of 20 Nov 2026. The page is based on a tool-generated summary of the CFR article, not a direct reading, so wording and detail may differ from the original. I have not independently verified the incidents or official statements it lists. A web search for the title returned only unrelated pieces.

## The source

Adam Segal, Ira A. Lipman Chair in Emerging Technologies and National Security and Director of the Digital and Cyberspace Policy Program at CFR (and a State Department cyber and digital policy adviser from Apr 2023 to Jun 2024), published 18 Nov 2026: <https://www.cfr.org/articles/the-real-reason-why-everything-is-crashing>. The summary renders the title as "The Real Reason Why Everything Seems to Be Crashing". This is an opinion and analysis piece, not a technical investigation.

## Thesis

The recent run of failures appears to have separate technical causes and not hacking. Segal links the instability to the pace of AI-driven change, including pressure to patch software quickly, and plays on the Silicon Valley motto: move fast and fix things, but still break them by accident.

## Main points (as summarised)

- **The outages look unconnected.** Public evidence points to different technical sources, though outages tend to trigger fears of malicious actors.
- **Real threats exist.** US critical infrastructure is vulnerable, particularly to a capable actor like China, and Iran-linked groups have targeted operational technology.
- **These events do not look like attacks.** No victim has said hackers were responsible, and US officials have said adversaries are not behind the disruptions.
- **AI as an indirect factor.** AI tools find software bugs quickly, pushing companies to patch fast, and updates can create new problems.
- **Dependence is the larger lesson.** Society relies on complex systems, and AI integration with legacy software will probably worsen instability before it improves.

## Incidents named (as summarised, not verified)

| Incident | Detail given |
|---|---|
| Microsoft outage | Linked article dated 12 Nov 2026; office workers affected nationwide |
| FAA nationwide ground stop | Around 13–14 Nov; reportedly lifted 14 Nov. The FAA reportedly installed the SMART AI air traffic tool days earlier; the Transportation Secretary denied it connects to core radar and tracking systems, and the FAA blamed a new router |
| Banking disruptions | Chase, Wells Fargo, Truist |
| Apple services outage | Linked article dated 17 Nov |
| NSANet outage | The NSA's internal network; interrupted top-secret communications |
| Refrigerator attack (France) | French authorities attributed to Iran an attack that reset temperatures on hundreds of supermarket refrigerators, spoiling tens of millions of euros of food. Compare the [EFS freezers case](../case-studies/efs-coolworld-refrigeration-2026.md), which is a different incident |
| Government advisories | FBI, CISA, NSA and DOE warned that IRGC-linked hackers targeted PLCs and other operational technology |
| AI-found bugs | PHP (CISA alert 21 Oct 2026) and Java (South Korean emergency meeting, 18 Nov); see the [Java4Shell page](java4shell-cisa-alert-hotspot-base64-2026.md) |

The article reportedly gives no counts of affected users or outage durations.

## Official statements cited

- The Director of National Intelligence, Jay Clayton, said these events are not a cyberattack or a coordinated nation-state effort.
- Senator Mark Warner said the situation is a consequence of how quickly AI is changing the cybersecurity landscape.

I paraphrase both because I have only the summary and not the article's exact wording.

## Recommendation

No formal policy recommendations. The one explicit call is for clear, timely communication from platforms and government about what they know, which matters more as instability becomes routine and people see patterns that are not there.

## Why a privacy and cyber hub should care

- **Attribution discipline.** The piece argues against assuming malice from simultaneous failures. The [Bridgewater analysis](bridgewater-ai-cyber-virus-2026.md) treats the same outages as worth watching even though malicious involvement is unconfirmed; the two views differ in emphasis, not in the facts they cite.
- **Change risk as a security risk.** Rapid patching creates its own outage risk, which bears on change management, testing and rollback planning.
- **Incident communication.** Early, accurate statements about what is and is not known are the control Segal names. Compare the wording in the [Equinor case](../case-studies/equinor-cyberattack-it-systems-2026.md).
- **Resilience and concentration.** Outages across email, aviation, banking and cloud services show dependency on a few providers, relevant to operational-resilience and third-party risk work.

## Gaps and cautions

- Summary only; incidents and quotations unverified here. Some items (FAA tool, NSANet, French refrigerator attribution) rest wholly on the article as summarised.
- Opinion piece; the AI link is described as a possible indirect factor, not proven.
- Not legal or security advice.
