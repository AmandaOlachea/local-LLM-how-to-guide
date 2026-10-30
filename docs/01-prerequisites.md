# 1. Before installing anything

I would start by checking the computer rather than downloading a huge model and hoping it runs.

## Check Docker

Install Docker Engine or Docker Desktop for your operating system, then run:

```bash
docker --version
docker compose version
docker info
```

If `docker info` fails, fix Docker before continuing.

## Check available resources

A small 1B parameter model is a reasonable starting point for experimenting. Memory requirements depend on the model and its quantization, and you need extra space for the runtime and downloaded weights.

```bash
docker system df
```

Check your operating system's free memory and disk space too.

## A few decisions

- This guide assumes a single computer and one local user.
- Keep the API on loopback for now.
- Use synthetic examples only.
- Do not expose port 11434 directly to the internet.

Next: [install Ollama](02-install.md).
