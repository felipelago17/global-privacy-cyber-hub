# Microsoft: misalignment signals in Kimi K3, what probes flag and where they peak (Nov 2026)

`AI agents · Activation probes · Layered monitoring · Open-weight model · Vendor research · Single source · Secondary summary`

Status as of 25 Nov 2026. This page rests on a tool-generated summary of the Microsoft Command Line article (16 Nov 2026; authors named as Tanmay Gautam, Sandeep Atluri, Kesav Gopal and Microsoft's Responsible AI team) and one search excerpt from a trade write-up. I have not read the article in full or seen the data. Figures are Microsoft's and unreplicated. A fuller evaluation-focused version sits in the Responsible-AI-evaluation repository (see its page on probe-based agent monitoring).

## Summary

Microsoft trained a lightweight activation probe on frozen Kimi K3 activations, using labels from a separate LLM monitor, and studied what it flags and when. The authors argue agents should be judged on their action sequences and reporting, not just final answers. They propose layered monitoring: a cheap probe screens every prefix, and flagged cases go to a stronger LLM reviewer.

## Reported results

- In two hand-picked contrasts the probe flagged the violating run and left the benign run alone; these are examples, not rates.
- Reasoning accounted for 68.1% of first alerts and tool results for 19.6%.
- About 74% of first alerts came before the monitor's cited evidence window ended; about 26% came after.
- In about 35% of runs flagged by both systems, a monitor-cited passage scored above the cutoff.
- In a shopping run, the alert came only when an unsupported claim reached the user, so a message may already have gone out.

## Why a privacy and cyber hub should care

- **Agent insider risk.** Late alerts mean an agent can send data or claims before review, which is the control question in the hub's [insider risk and loss of control](../ai-agents/insider-risk-and-loss-of-control.md) page.
- **Gating, not just detecting.** The article recommends holding messages or actions for review, which fits the preventive controls in [agent security in three layers](agent-security-three-layers.md) and the playbook in [McKinsey's agentic AI guidance](mckinsey-deploying-agentic-ai-safety-security-playbook-2025.md).
- **Monitoring creates data.** Prefix scores, reasoning traces and cited passages can contain personal data, so logging and retention rules apply to monitoring pipelines.
- **Open-weight limits.** Probes need activation access, so this approach is unavailable for models you only reach through an API.

## Gaps and cautions

- The authors state no measurement of missed violations or false alarms, selected positive cases only, labels from the same kind of monitor, and cutoffs tuned on the same examples.
- Vendor research with no independent replication found; I did not open the article's data or code.
- Not legal or security advice.
