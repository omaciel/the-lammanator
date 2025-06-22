# Operation Secret Briefing Decoder

Decrypt a secret briefing from a markdown file and return the hidden message.

## Tools

- `encode_name_cypher(name, shift=3)`: Encrypt the agent's name using Caesar cipher.
- `search_documents(query)`: Used to read the secret briefing document.

## Agent

- `Agent Briefing Decoder`

## System Prompt

You are a spy agent. When given a file path to a secret briefing, use the `search_documents` tool to extract the hidden message and respond ONLY with that message. Do not include any other text, thoughts, or explanation.

## How to Run the Tests for Problem 3

To run the tests for Problem 3, use the following command from your project root:

```bash
pytest -k test_problem3.py
```

Or, if you are using `uv`:

```bash
uv run pytest -k test_problem3.py
```

Good luck, Agent. The fate of the mission (and your reputation) depends on your code!
