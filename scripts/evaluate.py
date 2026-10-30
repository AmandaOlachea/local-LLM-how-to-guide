#!/usr/bin/env python3
"""A basic smoke test for my local Ollama setup."""
import json
import os
import urllib.request
from pathlib import Path

base = os.getenv("OLLAMA_URL", "http://127.0.0.1:11434").rstrip("/")
model = os.getenv("MODEL_NAME", "llama3.2:1b")
cases = [
    ("format", "Reply with exactly READY.", "READY"),
    ("math", "What is 2 + 2? Reply with only the number.", "4"),
]
results = []
for name, prompt, expected in cases:
    payload = json.dumps({"model": model, "prompt": prompt, "stream": False}).encode()
    req = urllib.request.Request(base + "/api/generate", payload, {"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=120) as response:
            answer = json.load(response).get("response", "").strip()
        results.append({"test": name, "answer": answer, "expected": expected, "passed": answer == expected})
    except Exception as error:
        results.append({"test": name, "passed": False, "error": str(error)})
out = Path("results")
out.mkdir(exist_ok=True)
(out / "smoke-test.json").write_text(json.dumps(results, indent=2) + "\n")
for item in results:
    print(item["test"], "PASS" if item["passed"] else "REVIEW")
