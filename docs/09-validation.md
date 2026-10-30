# 9. Security validation

I like having a way to check a configuration instead of assuming it works because a service starts successfully.

This worksheet can be used to record the results of security checks in whichever environment you're working with.

| Control | Verification |
| --- | --- |
| Network binding | Confirm the API is reachable only through intended interfaces |
| Encryption at rest | Check the encrypted volume and where application data is stored |
| TLS | Verify the certificate and encrypted connection |
| Authentication | Confirm anonymous requests are denied where authentication is required |
| Authorization | Verify users cannot access functions outside their permissions |
| Access revocation | Confirm disabled accounts lose access |
| Audit logs | Review access events and retention settings |
| Backups | Restore a backup and verify data integrity |
| Model QA | Run the evaluation suite and review failures |

## Test record template

| Field | Value |
| --- | --- |
| Environment | |
| Date | |
| Control | |
| Test procedure | |
| Expected result | |
| Actual result | |
| Evidence reference | |
| Follow-up | |

Keep sensitive details and internal evidence in the appropriate private system. Public documentation can describe the method without publishing the actual environment.

## References

- [HHS Security Rule](https://www.hhs.gov/hipaa/for-professionals/security/index.html)
- [NIST SP 800-66 Rev. 2](https://csrc.nist.gov/pubs/sp/800/66/r2/final)
