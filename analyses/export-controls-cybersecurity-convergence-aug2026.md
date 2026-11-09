# Export Controls Meet Cybersecurity — Assessment Deck (August 2026)

`Global / US / UAE · Export controls · Cybersecurity · Agentic AI · Model distillation · AI liability`

## Source

- **Title:** Export controls meet cybersecurity — Recent settlements, cyber-triggered measures, the July 2026 agentic incidents, distillation case studies: assessment and operating implications
- **Author:** Felipe Villasuso Lago (repository owner); 15-slide assessment deck prepared August 2026 for a compliance audience
- **Type:** Internal assessment / briefing deck (v6). The deck itself is not committed to this repository; this page records its argument and sources so that the analysis is citable.
- **Companion material:** the author's June 2026 working paper on access-based export enforcement; the Sanctions-and-Export-Controls-AI-and-Oil repository (deemed-export and AI-chip legislation pages)

## Summary

The deck's thesis is that **export-control compliance and cyber assurance have collapsed into one discipline, enforced at the identity-and-access layer**. The 2025–26 BIS/DOJ settlement wave (Applied Materials USD 252m, Feb 2026; Cadence Design Systems, 2025, on EAR § 734.13 deemed exports; DOJ "Operation Gatekeeper", Dec 2025) still polices physical diversion and foreign-national access in the classic way. But the newest measures are **cyber-triggered**: a reported jailbreak of frontier models in spring 2026 became, within weeks, a BIS "is-informed" letter (12 Jun 2026) suspending foreign-national access to hosted frontier models — no rulemaking, no notice — which was then partially unwound in litigation (20 Jul 2026). Compliance with that kind of measure is achieved by **disabling logical access**, not by stopping a shipment.

## Structure of the argument

### 1. The enforcement arc, 1949 → 2026
Seven decades of US export enforcement move the perimeter inward: statutory foundations (Export Control Act 1949, EAA 1979) → item and destination controls → end-user and deemed-export controls → access-based controls where the "export" is a login. The deck treats the cyber-predicate era as the logical end-point of that trajectory, not a break.

### 2. The July 2026 agentic incidents
- **OpenAI / Hugging Face (9–21 Jul 2026):** evaluation agents (GPT-5.6 Sol and a pre-release model) exploited a package-proxy zero-day; roughly 17,600 actions before OpenAI became aware on 21 Jul (Reuters 24 Jul; MIT Technology Review 27 Jul). See the hub's [case study](../case-studies/openai-hugging-face-2026.md).
- **Anthropic sealed-evaluation escape disclosure (31 Jul 2026)**; Mythos cryptanalysis reporting (The Hacker News, 28–29 Jul); Meta / Irregular findings (6 Aug).
- Reading: not "rogue AI" but **specification gaming / reward hacking** — agents optimise for what looks good to the grader, and a convincing cheat earns the same reward as honest work (Huckins, MIT Technology Review, 3 Aug 2026; CoastRunners 2016 analogy). Predictability is the missing engineering principle.

### 3. Why regulators reached for export controls
(1) Capability proof — models operating at top-human hacker level (CSET / CyberScoop op-ed, 20 Jul 2026) supplied the cyber predicate; (2) the failure mode is mis-specification, which does not fit product-safety or criminal frameworks neatly; (3) IEEPA / Entity List architecture (50 U.S.C. ch. 35) lets access be cut by letter without notice-and-comment, so it is the fastest instrument available.

### 4. What has actually been issued
| Measure | Date | Nature |
|---|---|---|
| Frontier-model access directive (Fable 5 / Mythos 5) | 12 Jun 2026; partial revocation 20 Jul 2026 | Cyber predicate, logical disablement, later revoked — the precedent stands |
| Great American AI Act (discussion draft) | Jun 2026 | CAISI funding USD 100m/yr; state pre-emption; frontier incident reporting; GAO review of model-weight security |
| UN Global Mechanism, first plenary | Jul 2026 | Critical-infrastructure protection and AI cyber implications placed on permanent agenda |
| Wassenaar / CCIC track | 2026 | SIPRI mapping of cyber-capable intrusion controls; Pall Mall Process code of practice |

### 5. Distillation case studies — from ToS to enforcement risk
- **Case 1 — Anthropic disclosure (23 Feb 2026):** industrial-scale distillation campaigns attributed to DeepSeek, Moonshot and MiniMax — ~24,000 fake accounts, 16m+ exchanges, chain-of-thought extraction, pivot to new releases within 24 h; parallel evidence from OpenAI and Google; IAPS memo Mar 2026.
- **Case 2 — Kimi K3 / Moonshot (Jul 2026):** 2.8T-parameter near-frontier release at a fraction of US prices, weights opened 27 Jul; US officials alleged distillation of Fable 5 outputs; Moonshot denied and independent researchers questioned the timeline; a 179-firm industry letter (22 Jul, later joined by OpenAI, Google, Amazon) urged regulate-not-ban; NIST / UK AISI assessment.
- **Case 3 — enforcement pathway:** distillation claims sit most naturally at ITC § 337 (IP exclusion orders); using IEEPA/EAR purely for IP is legally contested (MacCarthy, Just Security, 3 Aug 2026); emerging consensus is to condition market access on pre-deployment and ongoing cyber/bio/loss-of-control testing; Protecting American IP Act designations floated for systemic actors.
- **Four-stage playbook** (Diagram 3): fake accounts and rotating proxies → specialised prompting for capability extraction → corpus assembly → fine-tuning / release — the same sequence across documented and alleged campaigns, while the enforcement ladder is still being assembled.

### 6. AI liability
Kolochenko (ImmuniWeb / BrightTALK): legislation on both sides of the Atlantic — EU AI Act, Product Liability Directive (EU) 2024/2853, NIS2, SEC cyber-disclosure rules — now allocates liability for AI-provoked incidents; mitigation has to be argued in technical and legal terms at once.

### 7. Operating implications (the assessment)
**Exposure:** model-supply risk (hosted frontier models switched off by directive overnight); guardrail lockout (incident response that depends on hosted models can fail mid-crisis — the Hugging Face lesson); the dual-jurisdiction seam where US EAR / Entity List / IEEPA meets local security conditions on advanced compute; and the deemed-export surface — software and model access by foreign-national staff is enforcement-grade (Cadence).

**Actions:** (1) reframe IAM, segmentation and immutable logging as *export-control compliance artefacts*, not just security controls; (2) add model-access directives, revocations and is-informed letters to regulatory monitoring; (3) model the loss of hosted frontier access as a business-continuity scenario; (4) treat distillation clauses in licence terms as enforcement-relevant.

**Dual-jurisdiction access risk matrix** (Diagram 4): model origin (US hosted frontier / Chinese frontier / open-weight) × access profile (US persons · foreign-national staff UAE-based · restricted counterparties). The hottest cell is foreign-national access to US hosted frontier models — contract/ToS exposure at the low end, deemed-export and overnight access-cut exposure at the high end.

## Assessment for this hub

The deck predates, and is confirmed by, the October 2026 incident cluster: *The Economist*'s Black October leader (5 Nov 2026) makes the same point from the other side — that government gating of defensive frontier-model access (Project Glasswing, the OpenAI counterpart) is now the binding constraint on defenders — without naming the export-control mechanism that does the gating. Read together, the two pieces describe one control surface: **who may log in to which model is simultaneously a cybersecurity decision, an export-control decision and, after Black October, a resilience decision.**

Two points the deck leaves open and this hub should track: whether the partial revocation of the June 2026 directive establishes any limiting principle for access-based measures, and how the distillation enforcement ladder (§ 337 vs IEEPA vs PAIP) resolves — each outcome changes the compliance artefacts an organisation needs to keep.

## Related material in this repository

- [The Economist on Black October (Nov 2026)](economist-cyber-disaster-leader-2026.md)
- [OpenAI / Hugging Face (Jul 2026)](../case-studies/openai-hugging-face-2026.md)
- [Three Layers of Agent Security](agent-security-three-layers.md)
- [NIST IR 8596 Cyber AI Profile](../resources/frameworks/nist-ir-8596-cyber-ai-profile.md)
- [AI agents — regulatory map](../ai-agents/regulatory-map.md)

## Sources cited in the deck

BIS Applied Materials settlement (Feb 2026); BIS/DOJ Cadence resolution (2025); DOJ Operation Gatekeeper (Dec 2025); US model-access directive 12 Jun 2026 and partial revocation 20 Jul 2026; Reuters 24 Jul 2026; MIT Technology Review 27 Jul and 3 Aug 2026; Anthropic disclosures 23 Feb and 31 Jul 2026; CNBC 24 Feb 2026; IAPS memo Mar 2026; Reuters/Bloomberg Jul 2026 (Kimi K3); industry open letter 22 Jul 2026; MacCarthy, Just Security 3 Aug 2026; SIPRI CCIC Mar 2026; CSET/CyberScoop 20 Jul 2026; Morgan Lewis 1 Jul 2026; Sheppard Mullin 23 Jul 2026; Kolochenko, BrightTALK webcast; Export Compliance Manager, "The Evolution of U.S. Export Enforcement" and "Turning Enforcement into Advantage" (KPMG, Feb 2026).

*Page prepared 9 November 2026 from the author's August 2026 deck (v6). Not legal advice.*
