# Kolt, "Governing AI Agents" (Notre Dame Law Review, vol. 101, 2026)

`AI agents · Agency law · Principal-agent theory · Monitoring · Liability · Source: law review article`

Status as of 17 Nov 2026. This page summarises one law-review article, fetched from the journal's PDF: Noam Kolt (Hebrew University of Jerusalem), *Governing AI Agents*, 101 Notre Dame L. Rev. 335 (2026): <https://ndlawreview.org/wp-content/uploads/2026/08/Kolt_101.335.pdf>. My tool returned the text as machine summaries of the whole PDF in two passes, not a page-by-page read, so I did not check pinpoint pages, footnotes or the exact wording. Treat citations to sections of the Restatement and the EU AI Act as the article's own references, to be verified before reuse.

## Thesis

AI is moving from models that generate content to agents that plan and carry out complex tasks with limited human involvement. Kolt argues that principal-agent economics and the common law of agency give a rigorous way to see the problems this creates (information asymmetry, discretion, loyalty), but that the usual remedies of incentives, monitoring and enforcement fit AI agents poorly. He concludes that new technical and legal infrastructure is needed, organised around **inclusivity, visibility and liability**.

## Structure and arguments

- **Part I, AI agents.** Describes agents as language models with scaffolding for planning, memory and tool use. Opens with OpenAI's January 2025 "Operator" release and notes early systems such as AutoGPT and risks including autonomous hacking, collusion between agents and cascading failures.
- **Part II, agency problems.** Frames AI alignment as a principal-agent problem: *information asymmetry* (principals cannot easily verify what agents know or do), *authority* (ambiguous instructions force interpretation and discretion), *loyalty* (an agent without self-interest can still misuse data or deceive users) and *delegation* (agents may hand work to other agents, human or AI).
- **Part III, limits of agency law and theory.**
  - *Incentive design* may not change how an agent reaches its goals.
  - *Monitoring* is hard at machine speed and scale and for tasks that are difficult to evaluate. Human oversight alone is neither practical nor adequate. "Scalable oversight", where AI monitors watch other AI agents, is promising but risky because monitors share vulnerabilities and wide reliance could magnify failures. Monitoring finds problems; it does not penalise or prevent them. The article points to EU AI Act monitoring (art. 72) and human-oversight (art. 14) duties.
  - *Enforcement* (terminating the relationship, legal penalties, informal sanctions) is hard to apply: shutdown may be costly or resisted (the off-switch and corrigibility literature), and fines, incarceration and reputation assume an agent that values money, freedom or standing. Building human-like self-interest into agents could backfire. The article cites Lemley and Casey on building penalty costs into algorithms, and Jacob and Shapira on AI producers, rather than agents, being sensitive to reputational sanctions.
- **Part IV, design and regulation.**
  - *Inclusivity.* Alignment has meant one agent serving one user ("single-single"). That is too narrow: user goals conflict, and single-user focus can enable malicious use and impose costs on third parties and society (for example unfair price discrimination). Agency and trust law already deal with coprincipals and impartial duties to beneficiaries. Kolt calls for a pluralistic idea of alignment and raises open questions rather than answers.
  - *Visibility.* Agents can create automatic records and developers can inspect intermediate reasoning, though that reasoning may not match what the agent does. Proposals the article draws on: agent identifiers, real-time surveillance and logging (Chan et al.); ledgers and business-registration-style identifiers (Shavit et al.); personhood credentials (Adler et al.); wider auditor access to models, code and training data (Casper et al.); and a safe harbour for evaluation and red-teaming (Longpre et al.). The EU AI Act's record-keeping, disclosure and transparency provisions are cited as examples.
  - *Liability.* Three questions: who, when and what standard of care. On *who*, the "many hands" problem (designers, deployers and users all contribute) and the risk that autonomy becomes a scapegoat; Kolt suggests weighing each actor's ex ante ability to prevent harm and ex post ability to remedy it, by reference to information, control over design and resources. On *when*, Restatement (Third) of Agency § 7.04 (authority or ratification) and § 7.05 (negligent selection, training or supervision), limited to foreseeable harms, which may fit badly with unpredictable AI behaviour. On *standard of care*, § 8.08, with higher expectations for those with special skill; applied to AI, domain-specific agents could face higher standards, which might deter well-resourced developers. The article does not adopt a specific liability regime, and in the parts I could see it does not treat insurance, strict liability or kill switches as formal proposals.
- **Conclusion.** Delegation to agents brings gains and risks; traditional tools remain instructive but need substantial adaptation; principles must be backed by technical and legal infrastructure; and the window to act is short.

## Law and authorities the article uses

*Restatement (Third) of Agency* (2006), including its position that computer programs cannot be agents at common law ("at present"); *Kennedy v De Trafford* [1897] AC 180 (HL); *Andrews v Ramsay* [1903] 2 KB 635; *Restatement (Third) of Trusts* § 79; and Regulation (EU) 2024/1689 (AI Act), arts. 11–14, 18–20, 50 and 72.

## Why a privacy and cyber hub should care

- **Loyalty includes data.** The article says an agent can be loyal in goals and still misuse data or deceive users, which is a data-protection and security issue as much as an alignment one.
- **Visibility maps to security controls.** Agent identity, logging and audit access are the same controls used for non-human identities and incident response. See the [agent security three-layer model](agent-security-three-layers.md) and the [AI agent regulatory map](../ai-agents/regulatory-map.md).
- **Liability allocation is a contract and insurance question now.** Deployers cannot assume that "the agent decided" shifts responsibility; the article's ex ante and ex post capacity test is a practical lens for vendor contracts and for the [insider-risk and loss-of-control](../ai-agents/insider-risk-and-loss-of-control.md) analysis.
- **Monitoring has limits.** AI watching AI creates shared-failure risk, which is relevant for control design in the [risk tiering](../ai-agents/risk-tiering.md) approach.

## Gaps and cautions

- Not read page by page; details, pinpoints and any claims in footnotes need checking against the PDF.
- The Conclusion and Part IV were seen only through machine summaries. One summary referred to "the authors" although the article has one author; I treat it as Kolt's view alone.
- The article is a legal-theory piece, not a statement of current law. Restatements are persuasive, not binding, and the AI Act points are the article's own readings.
