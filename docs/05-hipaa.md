# 5. HIPAA safeguards and local LLMs

When working with systems that may handle electronic protected health information (ePHI), the model is only one part of the environment. I wanted this guide to connect the technical setup with the larger privacy and security requirements.

The HIPAA Security Rule includes administrative, physical, and technical safeguards. The exact controls and documentation depend on the organization, its risk analysis, and how the system is used.

| Area | Questions to address |
| --- | --- |
| Risk analysis | What data enters the system, where does it go, and what could expose it? |
| Access control | How are users identified and authorized? |
| Audit controls | What activity needs to be recorded and reviewed? |
| Integrity | How are unauthorized changes detected or prevented? |
| Transmission security | How is data protected between services and users? |
| Physical security | Who can access the equipment and storage? |
| Contingency planning | How are backups, recovery, and outages handled? |
| Policies and training | Who is responsible for administration and oversight? |

## Applying this to a local LLM

I would review the complete data path, including the user interface, API, model runtime, storage, logs, backups, and any connected applications. A local inference endpoint can help with data control, but the surrounding architecture still matters.

The chapters on encryption, access management, and validation provide examples of how to document and check technical safeguards.

## References

- [HHS Security Rule](https://www.hhs.gov/hipaa/for-professionals/security/index.html)
- [NIST SP 800-66 Rev. 2](https://csrc.nist.gov/pubs/sp/800/66/r2/final)

Next: [model evaluation](06-evaluation.md).
