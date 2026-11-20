# CFR (Adam Segal): why a run of tech outages looks more like fragility than attack (Nov 2026)

`Systemic outages · AI-accelerated patching · Attribution caution · Critical infrastructure · Incident communication · Source: Council on Foreign Relations`

Status as of 20 Nov 2026. This page is based on the full article text, supplied as a paste. I have not checked the incidents or official statements against other sources, and the article's hyperlinks (which carried dates for some incidents) were not in the paste. An earlier version of this page, built from a tool-generated summary, included a few details that the full text does not contain (CISA alert date for PHP, a South Korean emergency meeting, dates for the Microsoft and Apple outages). I removed them.

## The source

Adam Segal, Ira A. Lipman Chair in Emerging Technologies and National Security and Director of the Digital and Cyberspace Policy Program at CFR; senior adviser in the State Department's Bureau of Cyberspace and Digital Policy from Apr 2023 to Jun 2024. "The Real Reason Why Everything Seems to Be Crashing", published 18 Nov 2026: <https://www.cfr.org/articles/the-real-reason-why-everything-is-crashing>. An analysis and opinion piece, not a technical investigation. CFR notes it takes no institutional positions.

## Thesis

Turn the Silicon Valley adage around: not "move fast and break things" but "move fast and fix things, but still break them inadvertently". Segal argues the recent failures look unconnected and technical in origin, not malicious, and that AI-driven pressure to patch quickly is a plausible indirect factor.

## Main points

- **Incidents.** In the past week, a Microsoft outage, a nationwide FAA ground stop, disruption to banking and Apple services, and an outage of NSANet, the NSA's internal network, which interrupted top-secret communications. The photo caption says the FAA lifted the ground stop on 14 Nov 2026.
- **Unconnected causes.** All available public evidence suggests different technical sources and causes, though large outages quickly prompt questions about attackers and the "cyber Pearl Harbor" scenario.
- **Real threat background.** As the war with Tehran continues, the FBI, CISA, NSA and Department of Energy have warned operators that hackers linked to Iran's Islamic Revolutionary Guard Corps targeted PLCs and other operational technology. Segal adds that French authorities attributed to Iran, last week, an attack that reset temperatures on hundreds of supermarket refrigerators, spoiling tens of millions of euros' worth of food.
- **But these events do not look like attacks.** No victim has said hackers were responsible, and US officials have said adversaries are not behind them. Segal quotes Director of National Intelligence Jay Clayton as saying the events are not a cyberattack or a coordinated nation-state effort. He still says US critical infrastructure is vulnerable, especially to a highly capable actor such as China.
- **AI, direct theory.** The FAA reportedly installed a new AI-supported air traffic tool (Strategic Management of Airspace, Routes and Trajectories, SMART) a few days before the outage, prompting speculation about interaction with legacy systems. Transportation Secretary Sean Duffy denied it was connected to core radar and tracking systems, and the FAA blamed a new router.
- **AI, indirect theory.** Over recent weeks researchers have used AI tools to find major bugs in PHP and Java, widely used code. Analysts warn of a "cyber apocalypse" where defenders are overwhelmed, which creates pressure to patch fast, and first updates sometimes work imperfectly. Segal cites Senator Mark Warner (Senate Intelligence Committee Vice Chair) as saying what appears to be happening follows from how quickly AI is changing the cybersecurity landscape.
- **Conclusion.** Whatever the cause, society depends on complex systems vulnerable to technical error and malice, and it will get worse before it gets better as new AI systems are integrated with legacy software.
- **Recommendation.** No formal policy proposals. The one explicit call is for clear, timely communication from platforms and government about what they know, because people often see patterns where none exist.

## Incidents as the article states them

| Incident | What the article says |
|---|---|
| Microsoft outage | Part of the week's failures; no cause given |
| FAA ground stop | Lifted 14 Nov; AI tool speculation; FAA blamed a new router |
| Banking and Apple services | Disrupted; no detail |
| NSANet | Went down; top-secret communications interrupted |
| French refrigerators | Attributed to Iran by French authorities; hundreds of units; tens of millions of euros of food lost |

The article gives no outage durations or counts of affected users.

## Why a privacy and cyber hub should care

- **Attribution discipline.** Simultaneous failures invite attack narratives. The [Bridgewater analysis](bridgewater-ai-cyber-virus-2026.md) treats the same disruptions as worth watching while saying malicious involvement is unconfirmed; the two pieces differ in emphasis, not in the facts they cite.
- **Change risk as a security risk.** Rapid patching can itself cause outages, which bears on testing, staged rollout and rollback. See the [Java4Shell page](java4shell-cisa-alert-hotspot-base64-2026.md) for a fast patch advisory.
- **Incident communication.** Early, accurate statements about what is and is not known are the control Segal names. Compare the [Equinor case](../case-studies/equinor-cyberattack-it-systems-2026.md).
- **Resilience and concentration.** Outages across email, aviation, banking and cloud services point to third-party and operational-resilience dependency.
- **Refrigerator attacks.** The French incident Segal cites is separate from the [EFS blood-plasma freezers case](../case-studies/efs-coolworld-refrigeration-2026.md).

## Gaps and cautions

- Opinion piece; the AI link is a hypothesis the author presents, not an established cause.
- The Iran attribution, the SMART tool details and the NSANet outage rest on the article alone here.
- I paraphrase the Clayton and Warner statements and do not give their exact wording.
- Not legal or security advice.
