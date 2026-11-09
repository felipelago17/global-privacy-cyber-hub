# NIST IR 8596 (Initial Preliminary Draft) — Cybersecurity Framework Profile for Artificial Intelligence ("Cyber AI Profile")

`US (voluntary, global use) · NIST CSF 2.0 · AI security · AI-enabled defence · AI-enabled attacks`

## At a glance

| Attribute | Detail |
|---|---|
| **Full title** | Cybersecurity Framework Profile for Artificial Intelligence (Cyber AI Profile) — NIST Community Profile |
| **Identifier** | NIST IR 8596 iprd (Initial Preliminary Draft), December 2025; DOI 10.6028/NIST.IR.8596.iprd |
| **Status** | Preliminary draft released for comment **16 Dec 2025 – 30 Jan 2026**; comments feed an Initial Public Draft (IPD). Not final guidance. |
| **Authors** | Katerina Megas, Barbara Cuthill, Marissa Dotter, Michael Garris, Ishika Khemani, Bronwyn Patrick, Noah Schiro, Julie Nethery Snyder, Mohammad Zarei (NIST / NCCoE) |
| **Length** | 107 pp. — six CSF Function tables (GOVERN, IDENTIFY, PROTECT, DETECT, RESPOND, RECOVER) occupy pp. 16–91 |
| **Type** | CSF 2.0 **Community Profile** — prioritised Subcategory outcomes for a specific context, not a new framework and not certifiable |
| **Companion work** | NIST SP 800-53 **Control Overlays for Securing AI Systems (COSAiS)** — implementation-level overlays for generative AI, predictive AI, and single/multi-agent agentic AI (csrc.nist.gov/projects/cosais) |
| **Primary source** | <https://csrc.nist.gov/pubs/ir/8596/iprd>; NCCoE Cyber AI Profile project page |

## What it is

The Cyber AI Profile applies the NIST Cybersecurity Framework 2.0 to AI. It assumes an organisation already runs a cybersecurity programme and asks, for each CSF Subcategory, what changes when AI is in the picture. It does this through **three Focus Areas**, shown side by side in every table:

| Focus Area | Question it answers | Typical content |
|---|---|---|
| **Secure** — Securing AI System Components | How do we protect models, agents, algorithms, prompts, training data and pipelines that we build or buy? | AI asset inventory, supply-chain provenance for models and datasets, access control for model endpoints, poisoning/extraction/prompt-injection threats |
| **Defend** — Conducting AI-Enabled Cyber Defense | How do we use AI inside the SOC and what new risks does that create? | Analytics, triage and response automation; over-reliance, explainability, adversarial manipulation of the defensive model |
| **Thwart** — Thwarting AI-Enabled Cyber Attacks | How do we stay resilient against adversaries using AI? | AI-generated phishing and deepfakes, automated vulnerability discovery and exploitation at scale, faster patch-to-exploit cycles |

Each row of the tables gives: the CSF Subcategory; *General Considerations* common to all three Focus Areas; and, per Focus Area, a **Proposed Priority (1 = highest, 3 = lowest)**, *Sample Focus Area Considerations*, and *Example Informative References* (SP 800-53 Rev 5, OWASP AI Exchange and LLM Top 10, MITRE ATLAS, ENISA Threat Landscape, Databricks DASF, NIST AI 100-2, academic papers). Where AI adds nothing, the row says "standard cybersecurity practices apply".

## How the priorities fall (illustrative)

| Subcategory | Secure | Defend | Thwart | Why |
|---|---|---|---|---|
| ID.RA-01 Vulnerabilities identified | 1 | 1 | 1 | AI introduces new vulnerability classes and accelerates discovery on both sides |
| PR.AA-01 Identities and credentials managed | 1 | 2 | 1 | Model endpoints, agents and service accounts are new identity surfaces |
| DE.CM-01 Networks monitored | 2 | 1 | 1 | AI-enabled defence lives here; AI-enabled attacks show up here |
| GV.RM-01 Risk management objectives | 3 | 2 | 3 | Governance largely unchanged; Defend needs explicit objectives for AI tooling |
| GV.OC-01 Mission understood | 3 | 3 | 3 | No AI-specific delta |

The pattern across the document: **IDENTIFY, PROTECT and DETECT** carry most of the Priority-1 outcomes; **GOVERN** is mostly Priority 2–3 with the exception of supply-chain and policy outcomes; RESPOND and RECOVER gain AI-specific considerations around model rollback, retraining and incident taxonomy.

## Who it is for

Any organisation that uses AI (stand-alone or embedded, built or bought), wants to use AI in cyber defence, needs to defend against AI-enabled attacks, or develops AI systems. NIST positions it as a communication tool between AI and cybersecurity teams and as an input to leadership prioritisation — not as a compliance checklist.

## Development history

- Feb 2025: Cybersecurity and AI Workshop concept paper
- Apr 2025: public workshop; reflections published
- Aug–Sep 2025: three public working sessions, one per Focus Area
- Dec 2025: this preliminary draft; comment period to 30 Jan 2026
- Next: Initial Public Draft incorporating comments; glossary (Appendix B) to be added

Specific questions NIST asked commenters include whether the three Focus Areas should be presented side by side or separately, whether the Focus Area descriptions capture the right scope, and which additional Informative References to include.

## Interaction with other frameworks

- **NIST AI RMF 1.0** — the AI RMF points to the CSF for cybersecurity risk; this Profile is the bridge back.
- **SP 800-53 Rev 5 / COSAiS** — the Profile says *what* outcomes matter; the overlays say *which controls*.
- **ISO/IEC 27090:2026** — closest international counterpart for the *Secure* Focus Area; see [ISO/IEC 27090](iso-27090-ai-security.md). ISO 27090 does not cover the Defend or Thwart perspectives.
- **ISO/IEC 42001** — AI management system; the Profile can populate its security controls.
- **EU AI Act Art. 15** (accuracy, robustness, cybersecurity for high-risk systems) — the Profile is a plausible way to evidence Art. 15 compliance for US-aligned organisations.
- **OWASP, MITRE ATLAS, ENISA** — cited throughout as Informative References rather than re-stated.

## Why it matters for this hub

1. It is the first NIST artefact to treat **AI-enabled attack** (the *Thwart* column) as a first-class cybersecurity planning input — the exact gap exposed by the October 2026 incident cluster (see [The Economist on Black October](../../analyses/economist-cyber-disaster-leader-2026.md)).
2. The *Secure* column is a ready-made structure for the agent-security work in this repository ([Three Layers of Agent Security](../../analyses/agent-security-three-layers.md); [agent security checklist](../checklists/agent-security-checklist.md)); COSAiS's agentic-AI overlays are the implementation layer to watch.
3. For privacy teams, the Profile is cybersecurity-only by design — privacy considerations are routed to the NIST Privacy Framework — so it should be paired with a DPIA rather than treated as covering data-protection risk.

## Caveats

- Preliminary draft: priorities, references and even the Focus Area structure may change in the IPD.
- Technology-neutral and deliberately broad on "AI system"; it does not give model-type-specific controls (that is COSAiS's job).
- US-centric informative references; organisations under EU or GCC regimes will need a crosswalk.

**Related analyses in this hub:** [ISO/IEC 27090](iso-27090-ai-security.md) · [Three Layers of Agent Security](../../analyses/agent-security-three-layers.md) · [AI agents — privacy & cyber risks](../../ai-agents/index.md) · [Export controls × cybersecurity convergence (Aug 2026)](../../analyses/export-controls-cybersecurity-convergence-aug2026.md)

*Framework note prepared 9 November 2026 from the December 2025 preliminary draft.*
