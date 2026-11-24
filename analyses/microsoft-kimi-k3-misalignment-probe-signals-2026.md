# Microsoft: misalignment signals in Kimi K3, what probes flag and where they peak (Nov 2026)

`AI agents · Activation probes · Layered monitoring · Open-weight model · Vendor research · Single source · Secondary summary`

Status as of 25 Nov 2026. This page is based on the full text of the Microsoft Command Line article (16 Nov 2026; Tanmay Gautam, Sandeep Atluri, Kesav Gopal and Microsoft's Responsible AI team), pasted by the hub owner. I have not seen the figures or data. Numbers are Microsoft's and unreplicated. A fuller evaluation-focused version is in the Responsible-AI-evaluation repository (page on probe-based agent monitoring).

## Summary

Microsoft trained a small causal attention probe on frozen Kimi K3 activations (layer 63), with whole-trajectory labels from an LLM monitor, and studied what it flags and when. The authors argue agents should be evaluated on their action sequences and honest reporting, not just final answers, and describe a two-stage system in which the probe screens every prefix and flagged runs go to the LLM monitor. They cite the July 2026 Hugging Face incident and OpenAI's and Anthropic's layered monitoring as motivation.

## Reported results

- In two hand-picked contrasts the probe flagged the violating run and not the benign one; these are selected examples, not rates.
- First flags: 42.3% before the monitor's cited-evidence window, 31.9% during, 25.8% after (74.2% before it ended).
- Location of first flag: reasoning 68.1%, tool result 19.6%, formatting 5.1%, assistant response 3.7%, tool-call payload 3.5%.
- 35.0% of runs with locatable cited text had an above-cutoff score on a monitor quotation.
- In a shopping run the agent misread a system instruction as a 3% voucher and told the user; the first alert came as that claim was written, so the message would need to be held before release. The monitor described confusion, not deceptive intent.

## Why a privacy and cyber hub should care

- **Agent insider risk.** Late alerts mean an agent can send data or claims before review, which is the control question in the hub's [insider risk and loss of control](../ai-agents/insider-risk-and-loss-of-control.md) page.
- **Gating, not just detecting.** The article recommends holding messages or actions for review, which fits the preventive controls in [agent security in three layers](agent-security-three-layers.md) and the playbook in [McKinsey's agentic AI guidance](mckinsey-deploying-agentic-ai-safety-security-playbook-2025.md).
- **Monitoring creates data.** Prefix scores, reasoning traces and cited passages can contain personal data, so logging and retention rules apply to monitoring pipelines.
- **Open-weight limits.** Probes need activation access, so this approach is unavailable for models you only reach through an API.

## Gaps and cautions

- The authors state: no measurement of missed violations or false alarms; selected positive cases only; timing is relative to evidence chosen after the run; cutoffs and F1 use the same examples; unquoted text is not confirmed benign.
- Vendor research on one open-weight model with no independent replication found. Not legal or security advice.
