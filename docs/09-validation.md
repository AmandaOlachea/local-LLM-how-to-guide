# 9. How I would check the security setup

I don't want a checklist where everything gets marked complete just because I installed a tool. I want to be able to show what I tested.

| Test | Expected result | Current status |
| --- | --- | --- |
| API network binding | Loopback only | Not independently verified |
| Disk encryption | Model data stored on unlocked encrypted volume | Not implemented in starter Compose |
| Remote TLS | Valid certificate and encrypted connection | Not implemented |
| User authentication | Anonymous requests denied at gateway | Not implemented |
| Access revocation | Disabled account loses access | Not implemented |
| Audit trail | Relevant access events recorded | Not implemented |
| Backup restoration | Restore succeeds and data is usable | Not tested |
| Model evaluation | Test script saves responses | Script provided, not run |

## Evidence I would save

For each control, I would document the date, test environment, command or procedure, expected result, actual result, and what I changed if it failed.

I would only use synthetic records and redact identifying information from screenshots or logs.

## The HIPAA question

Even after all these tests pass, that would not establish HIPAA compliance for an organization. There are administrative, physical, legal, and operational requirements that can't be proven by a Docker test alone.

I would use [HHS guidance](https://www.hhs.gov/hipaa/for-professionals/security/index.html) and [NIST SP 800-66 Rev. 2](https://csrc.nist.gov/pubs/sp/800/66/r2/final) to organize the larger review.
