# 6. Test the model instead of just chatting with it

I want to make this part more useful than asking the model a few questions and deciding it seems good.

The included script sends a small set of prompts to the local API and saves the responses as JSON. It checks whether the model follows a simple output instruction and gives me a place to review failures.

Run it after downloading the model:

```bash
python3 scripts/evaluate.py
```

This is an initial smoke test, not a validated benchmark. I'll eventually add more cases for prompt injection, unsupported claims, privacy-sensitive requests, and consistency across repeated runs.

I also want to document what I expected, what actually happened, and whether I can reproduce the result.
