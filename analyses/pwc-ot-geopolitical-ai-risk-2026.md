# PwC: Defending the core: securing OT against AI and geopolitical risk (Nov 2026)

`Operational technology · ICS · Critical infrastructure · Geopolitics · AI-enabled attacks · NIS2 · IEC 62443 · Source: PwC Cyber & Risk Innovation Institute`

Status as of 15 Nov 2026. This page summarises one consultancy publication; its incident examples are PwC's descriptions and I did not check them against primary sources.

## The piece

PwC's Cyber & Risk Innovation Institute (Cyber, Data & Tech Risk practice) published the piece in November 2026, titled "Defending the core: Securing OT against AI and geopolitical risk" (the page metadata calls it "OT cybersecurity: Managing geopolitical risk"): <https://www.pwc.com/us/en/services/consulting/cybersecurity-data-tech-risk/library/geopolitical-shifts-amplify-ot-risks.html>. The contributors include Rob Joyce, a former US national security cyber official. The page presents no survey data; its figures come from the incidents it cites and industry loss estimates. The summary below is paraphrased.

## The argument

Geopolitical tension and AI tools are making operational technology easier and more attractive to attack, which raises risk to critical infrastructure, safety and operations. Legacy "technology debt" in OT compounds the problem. PwC argues for clear executive ownership, strong network segmentation, better asset visibility and less internet exposure of control systems, built up through a staged maturity approach.

## Incidents cited (as described by PwC, not independently checked)

| Incident | PwC's description |
|---|---|
| Aug 2026 US advisory | Five US agencies warned that attackers were using AI-generated exploitation scripts, disguised as monitoring tools, against programmable logic controllers (PLCs) |
| European supermarket refrigeration | Refrigeration control panels compromised across several chains, reportedly running outdated firmware; freezers reached 50°C and industry estimates put French losses at tens of millions of euros; failures at US military commissaries were also treated as a suspected cyberattack |
| US water utilities | Internet-exposed PLCs altered in Minnesota and Colorado, causing operator lockouts, manual operation and boil-water notices |
| Poland, Dec 2025 | A coordinated attack temporarily cut remote monitoring and control for 30 wind and solar facilities; at a smaller combined heat and power plant attackers used a private APN to reach the OT network and shut down a steam turbine and water treatment |

## OT risk themes it names

Legacy systems on modern networks; third-party and remote vendor access; edge and cloud connectivity creating exposed endpoints; physical access (USB, direct connections); IT/OT convergence without segmentation; weak asset inventories and little passive monitoring; fragmented ownership and scarce hybrid OT skills; opaque vendor relationships.

## Recommended actions (PwC)

- Align leadership on accountability, budget and a cross-functional RACI; include OT risk in board reporting.
- Build OT-specific incident response playbooks.
- Deploy passive network monitoring to build asset inventories.
- Segment OT into zones with an industrial DMZ and filter traffic between zones; limit internet exposure.
- Require vendor transparency, telemetry sharing and security provisions in SLAs.
- Use compensating controls where patching is not possible; enforce MFA and secure remote access, including service accounts.
- Test backups for recovery; build OT skills.
- Assess maturity across four tiers: foundational readiness, intermediate maturity, advanced capabilities and strategic integration.

Frameworks referenced: EU NIS2, US CISA, TSA and EPA OT expectations, IEC 62443, ISO 27001 extensions and O-PAS edge security standards.

## Why it matters for privacy and cyber teams

1. **OT is the non-personal data and safety side of the programme.** Control-system data and process parameters are rarely personal data, yet incidents can still carry reporting duties, contractual consequences and safety impact. This is the operational side of the [sensitive non-personal data](sensitive-non-personal-data-security.md) analysis.
2. **NIS2 puts OT inside the board's remit.** Art. 20 management accountability and Art. 21 risk-management measures apply to operators of essential services regardless of whether the compromised system holds personal data; see the [Luxembourg ILR reporting update](nis2-luxembourg-ilr-security-measures-reporting-2027.md) for how one regulator expects annual evidence.
3. **Vendor and remote access is the recurring weak point.** The same theme appears in the hub's vendor-breach cases such as [Uber/Fireworks AI](../case-studies/uber-fireworks-ai-vendor-breach-2026.md) and [Maersk](../case-studies/maersk-legacy-system-whitearmor-extortion-2026.md), and in supplier contract terms for NIS2.
4. **Telemetry cannot be trusted on a compromised host.** OT monitoring that relies on host-reported data has the same limit shown in the [GPU monitoring manipulation](../case-studies/gpu-monitoring-manipulation-ray-cryptomining-2026.md) case; passive network monitoring is a useful independent signal.
5. **Incident response must include operations.** Playbooks that stop at "notify the regulator" miss manual-operation fallbacks, safety checks and restart decisions that decide the real impact.

## Questions to ask

- Do we have a current inventory of OT assets and which are reachable from the internet or through vendor links?
- Who owns OT risk, and does the board see it in the same report as IT and privacy risk?
- Could each critical site run manually for several days, and has that been tested?
- Do vendor contracts require security provisions, telemetry sharing and breach notice for remote access?

## What this page does not establish

- I did not verify the incident descriptions or loss estimates. PwC gives no sourcing on the page for several of them, including the supermarket refrigeration cases and the figure for French losses.
- PwC sells cyber services, so the recommendations should be read as advisory positioning rather than neutral findings.
- Nothing here is legal advice, and applicability of NIS2 or US sector rules depends on entity type and status.

## Sources

- PwC Cyber & Risk Innovation Institute, "Defending the core: Securing OT against AI and geopolitical risk" (Nov 2026): <https://www.pwc.com/us/en/services/consulting/cybersecurity-data-tech-risk/library/geopolitical-shifts-amplify-ot-risks.html>
