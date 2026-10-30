# 4. Security checks I would do first

Getting a response from the model is the easy part. Before adding an interface or letting other people use it, I want to know what the service can access.

## Check the listening port

```bash
docker compose port ollama 11434
```

The example binds to `127.0.0.1`, so it is intended for local access only.

## Think about the data

I would trace where prompts, responses, model files, logs, and backups might be stored. Docker logs and any future web interface need to be part of that review.

## What this example doesn't add

There is no multi-user authentication, role-based access control, centralized audit trail, TLS termination, or backup policy here. I would not connect it to real healthcare data in this state.

## Before expanding it

- Decide who needs access and how they'll authenticate.
- Use a secure network design and TLS for any remote connections.
- Check logs for sensitive prompt content.
- Define retention, deletion, and backup procedures.
- Review image versions and patching.
- Test what happens when the service is unavailable.

Next: [HIPAA considerations](05-hipaa.md).
