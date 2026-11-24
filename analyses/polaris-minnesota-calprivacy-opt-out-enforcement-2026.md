# Polaris fined over opt-out failures in the first Minnesota privacy act action (Nov 2026)

`US state privacy · Opt-out of sale and targeted advertising · Global Privacy Control · Tracking technologies · Multistate enforcement · Law-firm alert plus regulator and press excerpts`

Status as of 25 Nov 2026. This page rests on a tool-generated summary of the Holland & Knight alert (published 24 Nov 2026, by Rachel Marmor and Sophia Lee) and on search excerpts of the Minnesota Attorney General's press release (19 Nov 2026) and press coverage (Valley News Live, PPC Land). I have not read the settlement documents, the CalPrivacy decision or the full AG release. The Holland & Knight alert also promotes the firm's Digital Risk Assessment service, so treat its takeaways as commentary.

## What happened

Polaris Industries Inc., a Minnesota-based maker of off-road vehicles, snowmobiles, motorcycles and boats, settled with two regulators that announced the actions on 19 Nov 2026. Both are members of the Consortium of Privacy Regulators, which coordinates investigations under state privacy laws.

| Regulator | Outcome (as reported) |
|---|---|
| California Privacy Protection Agency (CalPrivacy) | Administrative fine of USD 910,986 |
| Minnesota Attorney General | USD 150,000 settlement, plus a further USD 150,000 civil penalty stayed unless a court finds a material violation of the assurance |

Polaris did not admit liability. Per the alert, it admitted limited factual findings in the California order and denied the Minnesota allegations. Minnesota describes this as its first enforcement action under the Minnesota Consumer Data Privacy Act (MCDPA), in force since 31 Jul 2025 per PPC Land. The alert adds that it is the first public action testing the MCDPA's data privacy assessment requirement.

## Alleged failures

- **Verification for opt-outs.** Opt-out requests were denied when the consumer did not answer a verification email. The AG says the law allows verification for some requests, such as access, but opt-outs must be honoured when received.
- **Opt-out preference signals.** After a configuration update, Global Privacy Control was applied only on later visits, so tracking could run during the first session.
- **Risk assessments.** Polaris produced one assessment, dated April 2026, covering sale and targeted advertising; regulators inferred no earlier formal written assessments existed.
- **Notice.** The privacy notice did not adequately disclose the required opt-out information.
- **California context.** The alert says California also cited email verification, a "Decline All" cookie button that still fired the Meta pixel, unconfigured tools that ignored opt-out signals, and a policy that did not explain signal handling.

## Remedies

The Minnesota assurance largely restates existing law (minimal-step opt-outs without verification, a working opt-out link, staff training). Additional terms reported: quarterly scans or audits of tracking technologies for three years, an internal approval process for new tracking tools, a technical specialist to review opt-out configuration, and annual signed compliance certifications to CalPrivacy for three years.

## Why a privacy and cyber hub should care

- **A banner is not a control.** Regulators tested whether cookie settings stopped data flows to ad-tech, not whether a banner existed.
- **Signals before tags.** Opt-out signals must be read before tracking tools fire, which is an engineering and tag-governance requirement.
- **Multistate coordination.** The same facts produced parallel outcomes in two states, so exposure is not confined to one law.
- **Assessments are enforceable.** Documented data protection assessments for sale and targeted advertising are now being tested, which links to the hub's DPIA material.
- **Tracking governance as relief.** Recurring scans and approval gates for new tags resemble the vendor and change-control practices in other hub cases.

## Gaps and cautions

- The alert does not cite MCDPA section numbers, so I have not mapped the findings to specific provisions. The statute is at Minn. Stat. ch. 325M per search excerpts, and I did not verify the sections.
- Amounts and findings come from the alert and press excerpts; the primary orders were not read. One search result described the Minnesota press release's content only in part.
- Allegations are largely unadmitted. Settlements set no court precedent.
- Not legal advice.
