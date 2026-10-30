# 2. Get Ollama running

This example uses Docker so the setup can be reproduced from a single Compose file.

From the repository directory:

```bash
docker compose up -d
docker compose ps
```

Check the API:

```bash
curl --fail http://127.0.0.1:11434/api/version
```

You should get JSON containing a version number.

Check which address Docker published:

```bash
docker compose port ollama 11434
```

It should show a binding to `127.0.0.1`. If it shows `0.0.0.0`, stop and review your Compose configuration.

This is a local development setup. Loopback binding limits network exposure, but it does not provide user authentication or protect against other local processes.

Next: [download a model](03-first-model.md).
