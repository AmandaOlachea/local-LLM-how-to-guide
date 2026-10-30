# Running an LLM locally, from setup to security testing

I wanted to put together a guide for running a language model on your own computer. There are plenty of tutorials that get a model responding to prompts, but I wanted to go further and look at what happens when privacy, security, and sensitive information are part of the conversation.

This is my walkthrough for setting up Ollama with Docker, testing it locally, and thinking through the controls that would matter in a healthcare environment.

I'm using **made-up data** for all the examples. This is a learning project, and I haven't validated it for use with real patient information.

## What we'll build

- A local Ollama API that listens on your computer only.
- A model you can run without sending each prompt to a hosted inference API.
- A few repeatable tests for basic functionality and risky model responses.
- A checklist for security decisions and HIPAA-related safeguards.

## Start here

1. [Get your computer ready](docs/01-prerequisites.md)
2. [Install and run Ollama](docs/02-install.md)
3. [Download a model and test it](docs/03-first-model.md)
4. [Check the network and data flow](docs/04-security.md)
5. [Understand the HIPAA side](docs/05-hipaa.md)
6. [Run some evaluations](docs/06-evaluation.md)

## What you need

Docker with the Compose plugin, enough memory and disk space for the model you choose, and a terminal. I'm starting with a small model because I want the guide to be approachable without a dedicated GPU.

## Why the HIPAA section?

Running a model locally gives you more control over where inference happens, but there are still questions about authentication, audit trails, backups, access, and what data ends up in logs. I wanted to work through those questions rather than assume local means secure.

This project does **not** establish HIPAA compliance. That requires a broader organizational assessment and safeguards beyond the example Docker deployment.

## Where I am with this

The repository contains a starting configuration and tests. I haven't recorded a successful end-to-end deployment of this exact stack yet. As I run through it, I'll add actual results, issues, and changes instead of marking things complete just because the instructions look good.

## References

- [HHS: HIPAA Security Rule](https://www.hhs.gov/hipaa/for-professionals/security/index.html)
- [NIST SP 800-66 Rev. 2](https://csrc.nist.gov/pubs/sp/800/66/r2/final)
- [Ollama documentation](https://docs.ollama.com/)

## Going further with security

After getting the model running, I wanted to work through the parts that are easy to overlook:

7. [Encryption at rest and in transit](docs/07-encryption.md)
8. [Authentication, permissions, and audit logs](docs/08-access-and-auditing.md)
9. [Security validation and evidence](docs/09-validation.md)

These are walkthroughs and test plans. The starter Compose file is still a local development example, so the additional controls have to be configured and verified before using it for anything sensitive.
