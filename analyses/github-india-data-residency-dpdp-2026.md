# GitHub offers India data residency as AI and cloud vendors prepare for DPDP enforcement (Nov 2026)

`India · DPDP Act and Rules · Data residency · Significant data fiduciaries · Cloud and AI inference residency · Source: Analytics India Magazine`

Status as of 22 Nov 2026. This page is based on the full text of the Analytics India Magazine article (Kanishk Singh, published 19 Nov 2026), supplied as a paste, and on search excerpts about the DPDP Rules' timeline from law-firm and news sources. I have not read the Rules themselves or GitHub's announcement. Vendor product claims are as the article reports them and are not verified.

## The source

Kanishk Singh, "GitHub Now Lets Indian Enterprises Store Code Locally Ahead of DPDP Deadline", Analytics India Magazine, 19 Nov 2026: <https://analyticsindiamag.com/ai-news/github-now-lets-indian-enterprises-store-code-locally-ahead-of-dpdp-deadline>. The "key takeaways" box on the page is marked as AI-drafted.

## What the article says

- **GitHub.** It is bringing data residency options in India to GitHub Enterprise Cloud customers, who can host their code and in-scope repository data locally. GitHub says storage location can be an important consideration for financial services, telecommunications, government and other sectors with data location requirements. The aim is to let customers develop software without running and upgrading their own GitHub infrastructure.
- **How it works.** Customers use a dedicated GHE.com subdomain and Enterprise Managed Users, and manage accounts and access through their own identity provider, keeping the environment under their identity governance.
- **Wider trend.** Global AI labs and cloud providers have accelerated residency and local inference rollouts in India. Earlier this month OpenAI introduced API inference residency in India for supported GPT-6 Luna workloads (the model name is as given in the article); Amazon Web Services expanded its India inference profile across Mumbai and Hyderabad; and Microsoft, which owns GitHub, opened its fourth data centre in Hyderabad earlier this year, with a Microsoft executive quoted on cooling efficiency.
- **Regulation.** The article ties this to a "May 2027 deadline for full enforcement" of the Digital Personal Data Protection (DPDP) Rules, which it attributes to the Data Protection Board of India. It says the Rules do not impose a blanket localisation ban but impose targeted localisation mandates for significant data fiduciaries (SDFs), based on data volume, sensitivity and national security risk, under Rule 13(4).

## Checking the regulatory statements

- **Who set the date.** Search excerpts from several law firms say the Ministry of Electronics and Information Technology notified the DPDP Rules 2025 on 13 Nov 2025, with phased commencement over 18 months, so the core obligations take effect on 13 May 2027. Rule 4 (consent managers) takes effect on 13 Nov 2026. I found nothing showing the Data Protection Board set the date, so I treat the article's attribution as imprecise.
- **What takes effect then.** Excerpts list notices, consent, data principal rights, reasonable security safeguards, breach intimation (including a 72-hour element, per one secondary source), SDF obligations and cross-border transfer rules as part of the 13 May 2027 set. I have not verified rule numbers, and sources number the rules inconsistently.
- **Localisation.** Hogan Lovells says Rule 13 lets the government restrict cross-border transfers, especially for SDFs, and Khaitan says the government may impose restrictions to be complied with before sharing or transferring data. That is consistent with the article's description of targeted localisation, but I did not confirm the "Rule 13(4)" citation or the exact wording.

## Why a privacy and cyber hub should care

- **Residency as a procurement requirement.** Vendors are building regional storage and inference options before the Rules bite, so contract and architecture choices now will shape compliance in 2027.
- **Residency is not the whole answer.** Where data sits does not settle who can access it, what logs and support access cross borders, or which law applies. The [Dragos canary-token analysis](dragos-ai-supply-chain-canary-tokens-2026.md) reports prompts reaching a different jurisdiction despite customers choosing regional hosting; that is one vendor's research and not about GitHub.
- **Source code and personal data.** Code repositories can hold credentials and personal data, so repository residency interacts with secrets management and DPDP safeguards.
- **Targeted localisation.** Organisations that might be designated SDFs should track the designation criteria and any notified restrictions. See the hub's [DPDP readiness checklist](../resources/checklists/dpdp-readiness-checklist.md).
- For another jurisdiction moving on data protection in 2026, see the [Oman PDPL amendment page](oman-pdpl-amendment-royal-decree-68-2026.md).

## Gaps and cautions

- Trade-press article; GitHub, OpenAI, AWS and Microsoft claims are unverified, and the article quotes only GitHub and a Microsoft executive.
- The Board attribution and the rule citation are imprecise or unconfirmed, as above.
- It says nothing on pricing, availability dates or which GitHub data is "in scope".
- Not legal advice.
