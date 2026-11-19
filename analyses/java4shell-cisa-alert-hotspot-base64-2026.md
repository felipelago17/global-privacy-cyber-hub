# Java4Shell: CISA urges patching of the HotSpot Base64 flaw (Nov 2026)

`Vulnerability · Java / OpenJDK · Remote code execution · Patch management · Source: trade press (The Hacker News)`

Status as of 19 Nov 2026. This page rests on one article: Ravie Lakshmanan, "CISA Urges Immediate Patching of Java4Shell Flaw That Could Allow Remote Code Execution", The Hacker News, 18 Nov 2026: <https://thehackernews.com/2026/11/cisa-urges-immediate-patching-of.html>. I did not open CISA's alert, the OpenJDK or Oracle advisories, the Keycloak advisory or the Blackpoint Cyber research. A web search for the CVE identifier returned nothing that corroborates it (only unrelated 2026 Java HotSpot CVEs), so the identifier, score and product list are as the article states them and should be checked against NVD and the vendors before use.

## What the article reports

- **Flaw.** CVE-2026-114938, nicknamed "Java4Shell", CVSS 8.1. An out-of-bounds write in the Base64 decoder of the x86-64 HotSpot JVM (part of the JDK) that can cause denial of service or, under certain conditions, remote code execution. CISA is quoted as saying specially crafted Base64 input could crash the JVM and allow unauthenticated remote code execution.
- **Status.** Oracle and OpenJDK have released patches. No in-the-wild exploitation at publication. No threat actor named.
- **Products said to be exposed (from the outlet's earlier reporting).** Unauthenticated code execution under default settings on Keycloak, Atlassian Jira, Atlassian Confluence, JFrog Artifactory, Jenkins and PingFederate; code execution with a login on Apache Kafka Broker, Apache Solr, Elasticsearch, Gerrit and Spinnaker.
- **Keycloak guidance (18 Nov update).** Possible exposure needs all of: an unpatched OpenJDK build from 17.0.6 onward (including unpatched 21 and 25); a host or VM exposing the `avx512vbmi` CPU feature to Java; and a running JVM with Base64 intrinsics enabled and not limited to AVX2 through `-XX:UseAVX=2`. Container tags 26.8.2-1 and 26.8.2-2 bundle an affected OpenJDK 21.0.13 build, but tags alone do not decide exploitability; standalone ZIP or TAR.GZ distributions can also be affected. Keycloak provides a host-level command to check the CPU feature, and temporary mitigations until patched images ship.
- **Blackpoint Cyber testing.** On a local Spring Boot application with Spring Security, about 28,000 unauthenticated requests carrying a malformed Base64 authentication value crashed the JVM after roughly 20 seconds; testing also showed corruption of nearby Java objects and changes to live application data, sometimes with no immediate crash.
- **CISA's asks, per the article.** Identify affected Java installations; review inventories for JDKs and runtimes, including those bundled in third-party applications, container images and appliances; apply Java and vendor patches as available. The article does not mention a Known Exploited Vulnerabilities listing or a deadline. Interim steps: restrict and validate Base64 input at the application boundary, enforce input-size limits, limit unauthenticated access.

## Why a privacy and cyber hub should care

- **Integrity, not only availability.** Corrupted live application data without a crash is a data-integrity and incident-detection problem, which matters for personal-data breach assessment as well as uptime.
- **Hidden runtimes.** The advice to inventory bundled JDKs in appliances and container images is the same software-bill-of-materials and supplier-visibility problem behind the [Optimizely case](../case-studies/optimizely-third-party-script-compromise-178-sites-2026.md) and [NIS2 supplier security](nis2-supplier-security-contract-negotiation-computing-2026.md).
- **Identity infrastructure.** Keycloak, PingFederate and similar products sit in front of authentication, so a flaw triggered by a malformed authentication value affects the control point many privacy programmes depend on.
- **Conditional exposure.** Exploitability turns on CPU features and JVM flags, so a blanket "affected or not" answer from a version scan will be wrong in both directions; hardware and runtime settings need checking.
- For prioritisation sources, see the [reference sites list](../training-labs/cyber-reference-sites-20.md) (CISA, NVD, EPSS).

## Gaps and cautions

- Single secondary source; identifier and CVSS unconfirmed by me.
- The product list is described as coming from earlier reporting, not from vendors, and I did not verify any vendor's own statement beyond Keycloak's as relayed.
- "No exploitation" was true at publication and may have changed.
- Not legal or patching advice; confirm versions against the vendor advisories.
