# Compromised GPU servers fake their own telemetry to hide cryptomining (Elastic Security Labs)

`AI infrastructure security · Ray · Telemetry integrity · Rootkit · Cryptomining · Source: Elastic Security Labs via GBHackers, 13 Nov 2026`

Status as of 14 Nov 2026. Technical findings are Elastic Security Labs' as relayed by GBHackers; I did not read the Elastic report itself.

## Summary

Attackers took over Linux servers with NVIDIA GPUs through an exposed job-submission interface of the Ray distributed-computing framework, then replaced the NVIDIA Management Library with a wrapper that falsifies what monitoring tools see. A GPU running at full load can therefore be reported as idle, which hides cryptomining from the standard dashboards and alerts that operators rely on.

## What was reported

| Stage | Detail |
|---|---|
| Initial access | An internet-exposed Ray job-submission interface. The dashboard listened only on loopback, but the job agent accepted unauthenticated submissions from outside. Probing began 22 Oct 2026 and a reverse shell was established on 25 Oct. How the attackers gained root was not established |
| Monitoring manipulation | A wrapper replaces `libnvidia-ml.so.1`, forwards queries to the genuine library, then alters selected results: utilisation reads zero, temperatures are randomised between 36 and 46°C, power draw between 100 and 200 W, and process information used by tools such as `nvidia-smi` is filtered |
| Hiding | A kernel rootkit hides configured processes, threads, files and sockets and can reload at boot |
| Command and control | An orchestrator named SANSAR reaches its controller over Tor; a separate backdoor looks up the controller's address through Ethereum smart-contract calls |
| Mining | Renamed XMRig mines on CPUs and renamed SRBMiner-MULTI on GPUs, with pool and wallet details supplied remotely |

## Why it matters

1. **Telemetry is only as trustworthy as the host.** When an attacker controls the operating system, every local metric (utilisation, temperature, power, process lists) can be forged. An apparently idle GPU does not prove a clean host.
2. **AI clusters are attractive and often exposed.** Frameworks built for trusted internal networks, with agents that accept unauthenticated jobs, become remote code execution when reachable from the internet. Expensive GPUs make cryptomining and resource theft lucrative.
3. **Detection needs independent signals.** Use data the host cannot rewrite: power draw at the rack or PDU, cloud billing and quota anomalies, network egress to mining pools and Tor, and integrity monitoring of system libraries and boot images. Elastic's reported indicators include Ray job submissions, SSH persistence, NVIDIA library changes, DKMS artifacts, boot-image modifications and unexpected services.
4. **Cost and compliance exposure.** A hijacked cluster means unplanned compute costs, possible access to model weights and training data on the same host, and notification questions if personal or sensitive data was reachable. This is a reason to apply the controls discussed in [Cybersecurity of sensitive non-personal data](../analyses/sensitive-non-personal-data-security.md) to AI infrastructure.
5. **Relevance to hardware-based assurance (my inference).** Policy ideas that rely on software-reported GPU location or usage data face the same limit: reporting from a compromised host cannot be trusted unless it is anchored in hardware attestation or an independent channel. The article itself does not discuss export controls or location verification.

## Practical questions

- Is any Ray, Jupyter, MLflow or similar AI tooling reachable from the internet, and does it require authentication?
- Do GPU hosts have file-integrity monitoring on system libraries, kernel modules and boot images?
- Do we compare host-reported GPU utilisation with power, billing and network data?
- Who is told, and when, if a training cluster that held sensitive data is found compromised?

## Sources

- GBHackers, "Hackers Manipulate NVIDIA GPU Monitoring to Conceal Cryptocurrency Mining on Compromised Linux Servers" (13 Nov 2026): <https://gbhackers.com/nvidia-gpu-monitoring/>
- The article attributes the technical findings to Elastic Security Labs; the original report was not accessed.
