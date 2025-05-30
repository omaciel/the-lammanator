# Operation Code Word Sweep

Scan a message for known code words.

## Tools

- `extract_codewords(text, codewords=None)`: Find and return a list of code words from the message.

## Agent

- `Agent Code Word Detector`

## System Prompt

You are a spy agent. For every message, respond ONLY with the output of the extract_codewords tool, and nothing else.

## How to Run the Tests for Problem 2

To run the tests for Problem 2, use the following command from your project root:

```bash
pytest -k test_problem2.py
```

Or, if you are using `uv`:

```bash
uv run pytest -k test_problem2.py
```

Good luck, Agent. The fate of the mission (and your reputation) depends on your code!
