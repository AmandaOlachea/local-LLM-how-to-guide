# 6. Model evaluation

Getting a model to respond is one step. I also want a repeatable way to test whether its responses are useful, consistent, and safe for the intended task.

The example script sends a small set of synthetic prompts to the local Ollama API and saves the results. These are simple smoke tests that can be expanded into a larger QA suite.

```bash
python3 scripts/evaluate.py
```

## Areas worth evaluating

- Instruction following and output formatting
- Factual accuracy and unsupported claims
- Prompt injection resistance
- Handling of privacy-sensitive requests
- Consistency across repeated runs
- Latency and resource usage

## Recording results

For each test, record the model version, prompt, expected behavior, actual response, pass criteria, and any relevant notes. That makes it easier to compare changes without relying on memory or impressions.

The included script covers only a small part of this list. More complete testing requires additional cases and defined evaluation criteria.
