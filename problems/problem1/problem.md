# Operation Caesar Cipher

Encrypt the agent's name using Caesar cipher.

## Tools

- `encode_name_caesar(name, shift=3)`: Encrypt the agent's name using Caesar cipher.

## Agent

- `Agent Caesar Cipher`

## System Prompt

You are a spy agent. For every message, respond ONLY with the output of the encode_name_caesar tool, and nothing else.

## How to Run the Tests for Problem 1

To run the tests for Problem 1, use the following command from your project root:

```bash
pytest -k test_problem1.py
```

Or, if you are using `uv`:

```bash
uv run pytest -k test_problem1.py
```

Good luck, Agent. The fate of the mission (and your reputation) depends on your code!
