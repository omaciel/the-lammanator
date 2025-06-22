# Operation Dead Drop Logger

Log messages (e.g., from an LLM) to a secure local file.

## Tools

- `log_message_to_file(message, filename="drop.txt")`: Log a message to a secure drop file with a timestamp.

## Agent

- `Agent Dead Drop Logger`

## System Prompt

You are a spy agent. For every message, save the message to a file and NOTHING ELSE and respond with the name of the file.

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
