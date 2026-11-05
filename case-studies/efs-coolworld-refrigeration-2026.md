# Case study — French blood-plasma freezers tampered with via a cooling contractor (1–2 November 2026)

`France / EU · Health sector · OT / ICS security · Supply-chain · NIS2 · GDPR`

## Summary

Overnight on 1–2 November 2026, attackers reportedly altered the temperature setpoints on refrigeration units used by the **Établissement français du sang (EFS)** — France's national blood service — moving controllers from roughly **−30 °C to +110 °C**. The intrusion did not target EFS directly: it went through **Coolworld**, EFS's cooling-equipment and maintenance provider. Facilities in Bourgogne-Franche-Comté were among those reported as concerned. Donor samples kept for blood-safety surveillance were initially reported as affected; EFS later told *Le Canard enchaîné* that frozen plasma intended for transfusion was also involved. France's Health Ministry said staff detected the abnormal temperatures in time and that the incident had **no operational consequences**. No attacker has been publicly identified and no entry point has been confirmed.

The incident landed in the same week as an **ENISA joint statement on cyber incidents in refrigeration systems across the EU** (4 Nov 2026 — see the [4 Nov digest](../updates/2026-11-04.md)) and three weeks after a **CERT-FR alert (12 Oct 2026)** on compromises of Danfoss AK-SM/AK-SC, Copeland and Dixell XWEB refrigeration controllers. No public evidence links those alerts to the EFS event, and the reporting is careful to say so.

## Timeline (as publicly reported)

| When | Event |
|---|---|
| 12 Oct 2026 | CERT-FR alert on compromises of internet-exposed refrigeration controllers (Danfoss AK-SM/AK-SC, Copeland, Dixell XWEB) |
| Oct 2026 | Earlier attacks reported on supermarket refrigeration systems in France |
| 1–2 Nov 2026 (night) | Setpoints on EFS refrigeration units changed to ~110 °C via the Coolworld-managed systems; abnormal temperatures detected by staff |
| 3–4 Nov 2026 | *Le Canard enchaîné* / Cyberattaque report the incident; Health Ministry states "no operational consequences"; EFS confirms transfusion plasma was among the stock concerned |
| 4 Nov 2026 | ENISA joint statement on refrigeration-system cyber incidents across the EU; Cyber Security News write-up (Guru Baran) |

## What is known — and what is not

**Known**
- Attack path ran through a **third-party cooling/maintenance provider**, not EFS's own IT.
- The manipulated value was a **controller setpoint**, not a confirmed measurement of product temperature.
- Detection was **human**, by on-site staff noticing abnormal temperatures — not an automated OT alarm feeding a SOC.

**Not known / not confirmed**
- Initial access vector (no specific controller model, vulnerability, or stolen maintenance account has been identified — attributing it to a particular Danfoss flaw would go beyond the evidence).
- Number of units affected, duration of the disruption, temperatures actually reached inside stored products.
- Any destroyed plasma, cancelled transfusions, or patient harm.
- Any theft of donor personal data (reporting contains no confirmed exfiltration).
- Attribution.

## Why it matters for privacy, cyber and compliance programmes

1. **The attack surface was a contractor's remote-management interface.** Refrigeration controllers are routinely exposed to the internet so a maintenance vendor can monitor them. That vendor becomes a single point of failure for every client site it serves. Third-party risk programmes built around data processors need to extend to **OT service providers** that hold write access to physical parameters.
2. **Cyber-physical safety, not just data, is the harm.** A 140-degree setpoint swing on blood products is a patient-safety event. Incident classification, escalation and regulatory notification paths designed for data breaches may not fire for an integrity attack on a physical process — this case is a useful tabletop scenario (CISA ran a cyber-physical tabletop the same week; see the [4 Nov digest](../updates/2026-11-04.md)).
3. **NIS2 essential-entity obligations are directly engaged.** Blood establishments are health-sector essential entities under NIS2 (Annex I); the directive's supply-chain security requirements (Art. 21(2)(d)) and 24-hour early-warning / 72-hour notification regime (Art. 23) apply. Whether a setpoint manipulation with "no operational consequences" is a "significant incident" is exactly the kind of threshold question national CSIRTs will now have to answer.
4. **GDPR exposure is secondary but real.** Donor samples kept for safety surveillance are linked to identifiable donors (special-category health data). Even absent exfiltration, loss of availability or integrity of those samples can be a personal-data breach under Art. 4(12) GDPR, triggering the Art. 33 assessment with the CNIL.
5. **Detection by people is a control gap, not a success story.** The outcome was good because someone noticed. The lesson is that OT telemetry (setpoint changes, out-of-band temperature excursions) should alert automatically and be correlated with vendor remote-access logs.

## Controls to review

- Inventory every OT/IoT system a vendor can reach remotely; remove direct public exposure of management interfaces (CERT-FR's recommendation).
- Enforce VPN/zero-trust access for vendor remote maintenance, with per-technician accounts, MFA and session logging; rotate default and shared credentials.
- Apply controller firmware updates; review configuration baselines and alert on setpoint changes outside an approved window.
- Add **physical-parameter integrity** scenarios to incident-response and NIS2 notification playbooks; define who decides whether an OT event is "significant".
- Flow down NIS2 Art. 21 supply-chain requirements into maintenance contracts (security obligations, breach notification SLAs, audit rights).
- Map which stored biological samples constitute personal data and pre-build the Art. 33/34 GDPR assessment for integrity/availability incidents.

## Framework mapping

| Framework | Relevant provisions |
|---|---|
| **NIS2 Directive (EU 2022/2555)** | Art. 21(2)(d) supply-chain security; Art. 21(2)(b) incident handling; Art. 23 reporting (24h early warning / 72h notification / 1-month final report); Annex I health sector |
| **GDPR** | Art. 4(12) personal-data breach (availability/integrity); Art. 9 special-category (health) data; Arts. 32–34 security and breach notification |
| **EU Cyber Resilience Act** | Security-by-default and vulnerability-handling obligations for connected refrigeration controllers once in application |
| **IEC 62443** | Zones and conduits, remote-access requirements (SR 1.13), security levels for vendor connectivity |
| **NIST CSF 2.0 / SP 800-82r3** | GV.SC (supply chain), DE.CM (continuous monitoring of OT), OT-specific guidance |
| **ISO/IEC 27001:2022** | A.5.19–5.22 supplier relationships; A.8.16 monitoring activities |

## Sources

- Cyber Security News — [French Blood Plasma Freezers Hacked: Temperatures Pushed to 110 °C](https://cybersecuritynews.com/french-blood-plasma-freezers-hacked/) (Guru Baran, 4 Nov 2026), drawing on Cyberattaque and *Le Canard enchaîné*
- ENISA — Joint statement on cyber incidents in refrigeration systems across the EU (4 Nov 2026) — via [4 Nov digest](../updates/2026-11-04.md)
- CERT-FR — alert on compromised refrigeration controllers (12 Oct 2026)

*Status: developing. Figures and scope are as reported in the press on 4 Nov 2026 and have not been confirmed by an official EFS or ANSSI incident report.*
