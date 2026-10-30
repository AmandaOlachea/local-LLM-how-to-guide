# 3. Download a model and try it

Start with a small model. I'm using `llama3.2:1b` for the example, but you can change it if your hardware supports something else.

```bash
docker compose exec ollama ollama pull llama3.2:1b
docker compose exec ollama ollama list
```

Try a prompt:

```bash
curl --fail http://127.0.0.1:11434/api/generate \
  -H 'Content-Type: application/json' \
  -d '{"model":"llama3.2:1b","prompt":"Explain what a local language model is in two sentences.","stream":false}'
```

The response should contain a `response` field. The first request may be slower while the model loads.

Model downloads require network access. Running inference locally does not by itself prove that every component is offline, so I'll check the network behavior separately.

Next: [security checks](04-security.md).
