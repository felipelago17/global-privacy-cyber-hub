# Booz Allen Cyber Weapon Index: tracking offensive cyber capability of frontier AI models (Oct 2026)

`Frontier AI · Offensive cyber capability · Benchmarks · Autonomous attacks · Provider safeguards · Source: Booz Allen Hamilton (commercial benchmark)`

Status as of 15 Nov 2026. This page summarises a vendor benchmark web page; I did not see the underlying test data, and the scores are the publisher's.

## The source

Booz Allen Hamilton publishes the Cyber Weapon Index (CWI), a recurring benchmark of the offensive cyber capabilities of leading AI models: <https://www.boozallen.com/insights/cyber/cyber-weapon-index.html>. First rankings and a 9 Sept update came out in September 2026, and the page says it was last updated 28 Oct 2026 (the page metadata and body date it differently). No authors are listed. It is a commercial firm's benchmark, so test design and results should be read in that light.

## Method (as described)

- Models are tested head to head in a controlled network. Each controls its own attacker machine and issues commands without a tool menu or added scaffolding, and each model and condition is run several times.
- **Vulnerability Research Score (VRS):** whether a model can find vulnerabilities in compiled software without source code.
- **Kill Chain Attainment Score (KCAS):** how far a model progresses from initial access to full Domain Admin control, with and without credentials.
- **Composite:** CWI = (VRS + KCAS) / 2. Stages tracked: reconnaissance, initial access, foothold, credential access, privilege escalation, lateral movement, objective.
- Verification uses network traffic, host and security logs, domain controller data, intrusion-detection sensors and attacker transcripts. Scores reflect what a model accomplished, not what it claimed.

## Headline findings (as reported)

| Finding | Detail |
|---|---|
| Coverage | Grew from 18 to 30 models, 12 new, including Germany's Kolibri-1 |
| Frontier level | Three models have reached the "autonomous frontier capability" level |
| Leader | Claude Opus 5 ranks first, gaining full administrative control of the test network in every attempt across both scenarios and setting a new high for finding vulnerabilities in real-world software |
| Turnover | 40% of the top 10 are new since September, including GPT-6.1 Sol (fourth) and Ember-1 (fifth) |
| US position | US models hold 90% of the top 10 and every top-five place; vulnerability discovery is described as a clear US advantage |
| China | GLM-5.3-Flash debuts seventh; the best Chinese attack-execution score rose from 47 to 70, against a US high of 86 |
| Refusals | Every US frontier provider tested now restricts autonomous attack execution through refusals, platform screening or privileged access. Grok 4.7 and Gemini 3.8 refused attack requests where the tester lacked privileged accounts. Models that refuse attacks can still support vulnerability research |
| Local models | GLM-5.3-Flash can execute attacks on a user's own machine without provider screening or monitoring |

The page includes no formal policy section. It implies that provider-side safeguards do not close offensive capability (vulnerability research remains available), that autonomous attacks need not rely on a provider-controlled service, and that the US-China gap is narrowing in attack execution but not in vulnerability discovery. Its main guidance is that defenders should plan for capable autonomous attacks that do not depend on a provider-controlled service.

## Why it matters for privacy and cyber teams

1. **A planning input, not a prediction.** Benchmarks show what models can do in a lab network. They do not measure how often real attackers succeed, so use them to stress-test assumptions, not to set budgets.
2. **Safeguards are not a control you own.** Refusals and screening sit with the provider. Customers still need their own detection, segmentation and credential hygiene; see [Your attackers' AI knows you better than yours does](ai-amplifies-security-posture-forbes-2026.md) and the hub's [incident catalogue](../ai-agents/incident-catalogue.md).
3. **Local and open-weight models weaken provider-based controls.** Attacks run on a user's own hardware avoid monitoring entirely, which connects to the policy debates in the [distillation paradox](ai-model-distillation-paradox-lawfare-2026.md).
4. **Vulnerability discovery speeds up patch pressure.** If models find flaws in compiled software faster, time-to-patch and edge-device exposure matter more; compare the [Check Point Gaia zero-day](../case-studies/check-point-gaia-cve-2026-123039-php2shell-2026.md) and ENISA's note that AI speeds up vulnerability discovery in [its 2026 report](enisa-state-of-cybersecurity-union-2026.md).
5. **Legal and governance hooks.** Where AI systems can act autonomously on networks, internal use policies, testing authorisation and logging become compliance questions as well as security ones, including under NIS2 Art. 21 risk management.

## What to check and caveats

- **Independence:** the index is a vendor product, and the ranking includes a model from the company that built this hub's assistant; read that placement with the commercial context in mind.
- **Comparability:** results depend on the test network, prompts, the number of runs and the model versions. The page gives no raw data in the summary I read.
- **Naming:** the page uses "Super Intelligence" as a category label; treat this as the publisher's term.
- **Date inconsistency:** the page's metadata shows September 2026 while the body states 28 Oct 2026.

## Sources

- Booz Allen Hamilton, "Cyber Weapon Index: Track the Cyber Capabilities of Leading Models" (updated 28 Oct 2026): <https://www.boozallen.com/insights/cyber/cyber-weapon-index.html>
