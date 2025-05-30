# 🦙 The Llamanator

> *Your mission, should you choose to accept it: Master the art of local AI agents, outwit the mundane, and become a legend in the world of secret AI ops.*

---

## 🕵️ Mission Briefing

Welcome, Agent. You have just been recruited by **The Llamanator**, the world’s most clandestine (and stylish) AI agency. Here, you’ll learn how to wield the power of [Ollama](https://ollama.com/) and the formidable `qwen3:0.6b` LLM to solve secret tasks, crack codes, and maybe save the world (or at least your next project).

This repo is your top-secret training ground. Each problem is a mission. Each solution brings you closer to earning your License to Skill.

---

## 🧰 Your Gadgetry

- **Ollama**: Your AI handler. Runs large language models locally—no cloud, no leaks, all stealth.
- **qwen3:0.6b**: The LLM of choice for The Llamanator. Small, nimble, and ready for action.
- **Local AI Agents**: Your loyal operatives, ready to take on any task you throw their way.

---

## 🛠️ How to Deploy Your Agents

1. **Clone this repository** (don’t worry, Q has wiped your fingerprints):

   ```bash
   git clone https://github.com/your-username/The-Llamanator.git
   cd The-Llamanator
   ```

2. **Install your dependencies** (no exploding pens required):

   ```bash
   pip install -r requirements.txt
   ```

   Or, for agents who like their installs shaken, not stirred (and much faster), use [uv](https://docs.astral.sh/uv/):

   ```bash
   uv sync
   ```

   *Don’t have `uv` yet? Get it from [the official docs](https://docs.astral.sh/uv/).*

3. **Install Ollama** (if you haven’t already):

   - [Ollama Installation Guide](https://ollama.com/download)

4. **Pull the qwen3:0.6b model**:

   ```bash
   ollama pull qwen3:0.6b
   ```

5. **Begin your training**:

   ```bash
   pytest
   ```

   Or, for maximum agent style:

   ```bash
   uv run pytest
   ```

---

## 🎯 Training Exercises

Each mission (problem) will test your skills in:

- Building and using local AI agents
- Integrating with Ollama
- Encoding, decoding, and agent communication
- Thinking like a secret agent (wit required!)

Check out the `problems/` and `tests/` directories for your assignments. Hints are hidden like microdots in the code. Stay sharp.

---

## 🪪 License to Skill

This project is licensed under the MIT License. Use your powers for good, Agent.

---

*Remember: In the world of The Llamanator, the only thing more powerful than AI is your imagination. Now get out there and make Q proud!* 🦙
