# AI security and red-teaming labs

`Prompt injection · AI agents · Red teaming · CTF · Status: operator pages not opened, descriptions from operator blogs, papers and trade press`

Status as of 17 Nov 2026. Free or low-cost places to practise attacking and defending AI systems. Operator sites were not on my fetch allowlist, so I did not open the labs themselves or test links. See [safe-use rules](README.md#safe-use-rules) first.

## The five AI-security labs

| Lab | Operator | What it offers | Evidence checked |
|---|---|---|---|
| Gandalf: Agent Breaker (<https://gandalf.lakera.ai/agent-breaker>) | Lakera (a Check Point company) | Hacking simulator with ten mock agentic AI apps at escalating difficulty | Lakera's blog calls it a public red-teaming testbed with ten mock agentic apps. Trade press says the Check Point/Lakera b3 benchmark, built with the UK AI Security Institute, combines 10 agent threat snapshots with 19,433 attacks collected from the game. One third-party guide says the original Gandalf password game now redirects to Agent Breaker (Nov 2026); not confirmed on Lakera's site |
| Crucible (<https://crucible.dreadnode.io>) | Dreadnode | Free, hosted AI red-teaming CTF challenges solved mostly through code | Dreadnode's papers describe Crucible as a free, open environment for AI red teaming; its AIRTBench paper uses 70 black-box CTF challenges from it to test autonomous exploitation by models |
| HackAPrompt (<https://hackaprompt.com>) | Learn Prompting | Prompt-injection and jailbreak competitions and learning hub | The HackAPrompt 1.0 paper (arXiv 2311.16119) describes a global competition and dataset; HackAPrompt 2.0 was announced in January 2025 with five tracks. Check current status |
| Prompt Airlines (<https://promptairlines.com>) | Wiz | Chatbot CTF: manipulate a fictional airline's support bot into a free ticket; no coding | Wiz's launch post says it is based on real AI vulnerabilities found by Wiz Research and open to all skill levels |
| Web LLM attacks (<https://portswigger.net/web-security/llm-attacks>) | PortSwigger Web Security Academy | Free labs on LLM API abuse, excessive agency, indirect prompt injection, insecure output handling, and AI-powered scanner vulnerabilities | PortSwigger lab pages confirm the topics and that the labs use a live LLM. Some AI-scanner labs collect telemetry, including AI interaction logs |

## What each lab teaches, in privacy and security terms

| Failure mode | Where to see it | Control to review |
|---|---|---|
| System-prompt or secret leakage | Prompt Airlines, Gandalf | Keep secrets out of prompts; output filtering; least-privilege tool credentials |
| Indirect prompt injection (instructions hidden in content the AI reads) | PortSwigger labs, Agent Breaker | Treat retrieved content as untrusted; separate data from instructions; confirm actions |
| Excessive agency (too many tool permissions) | PortSwigger labs | Narrow tool scopes; human approval for destructive or data-moving actions |
| Insecure output handling | PortSwigger labs | Validate and encode model output before it reaches a browser, shell or database |
| Automated attack discovery | Crucible, AIRTBench | Assume attackers can automate probing; rate-limit and monitor |

For the matching controls, see the [agent security checklist](../resources/checklists/agent-security-checklist.md), the [risk tiering](../ai-agents/risk-tiering.md) approach and the [AI agent regulatory map](../ai-agents/regulatory-map.md).

## Gaps

- Descriptions rest on operator blogs, research papers and trade press, not on opening the labs.
- The Agent Breaker redirect claim comes from one third-party guide.
- No lab was run; difficulty, availability and sign-up requirements are untested.
