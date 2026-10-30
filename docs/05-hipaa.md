# 5. Where HIPAA fits in

This was one of the reasons I wanted to build the guide. I work with systems where privacy and data handling matter, and I wanted to understand how the requirements translate into technical decisions.

The HIPAA Security Rule covers administrative, physical, and technical safeguards for electronic protected health information (ePHI). A local model is just one component of a larger system.

| Area | What I'd need to think through |
| --- | --- |
| Risk analysis | What data is involved, who can access it, and what could go wrong? |
| Access controls | How are users identified and permissions managed? |
| Audit controls | Can the organization review activity without collecting unnecessary sensitive data? |
| Integrity | How do we prevent or detect unauthorized changes? |
| Transmission security | How is data protected when it travels between systems? |
| Physical safeguards | Who can access the machine and storage? |
| Contingency planning | How are backups, recovery, and outages handled? |
| Policies and training | Who is responsible for operating and reviewing the system? |

These are discussion points, not completed controls. The example deployment is not intended to process ePHI.

For a real healthcare deployment, the organization would also need to assess vendors and business associate arrangements where applicable, document risk decisions, and evaluate its own environment.

I used the [HHS Security Rule summary](https://www.hhs.gov/hipaa/for-professionals/security/laws-regulations/index.html) and [NIST SP 800-66 Rev. 2](https://csrc.nist.gov/pubs/sp/800/66/r2/final) as references.

Next: [evaluation](06-evaluation.md).
