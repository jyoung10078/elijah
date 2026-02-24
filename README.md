Elijah — AI research & presentation tools
=======================================

This repository contains utilities and example workflows for using LLMs to analyze datasets, save research outputs, and generate PowerPoint presentations from AI-generated insights. The original genealogy-focused README is out of date — current code primarily demonstrates an LLM-driven research assistant and PPTX generation pipeline (not a full genealogy product).

What’s in this repo
--------------------
- `main.py` — Example agent entrypoint that wires an LLM agent, defines the `ResearchResponse` Pydantic model, and shows parsing of model output.
- `tools.py` — Project tools used by agents (search/wiki helpers, save tool, and helpers for exporting results).
- `testing/pp_main.ipynb` — Notebook demonstrating dataset analysis with an LLM (loads a CSV, requests insights, and generates a PPTX).
- `requirements.txt` — Python dependencies (includes LangChain, OpenAI bindings, `pandas`, and `python-pptx`).
- `.env` (not committed) — expected to contain API keys like `OPENAI_API_KEY` or Anthropic keys for running notebooks/scripts.

Optional / example outputs
--------------------------
- The notebook shows how to send dataset summaries to an LLM and convert the returned insights into a PowerPoint (`dataset_insights.pptx`).

Key behaviors and notes
-----------------------
- The notebook and tools expect the insights text to use simple markers (for example `###` for section headings). The PPT generation code turns `###` sections into slide titles and formats content into readable slides.
- `main.py` demonstrates using a LangChain-style agent with tools and enforces structured output using `PydanticOutputParser`.
- The repository contains examples of both OpenAI and other LLM provider usage (notebooks may use OpenAI; other scripts may reference LangChain/Anthropic). Ensure appropriate API keys are present in your environment before running.

Quickstart (local)
-------------------
1. Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Add API keys to `.env` (example):

```
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=claude-...
```

4. Run the notebook to generate insights and a PowerPoint:

```bash
jupyter lab testing/pp_main.ipynb
```

Or run `python main.py` to start the example agent (it will attempt to use configured tools and LLM settings).

Limitations & next steps
------------------------
- This repo contains example and demo code rather than a production application. Expect to adapt API keys, model names, and tool descriptions to your environment.
- If you want a different PPTX style, the notebook contains code that adds a simple banner and formats headings — you can change colors, fonts, or add a corporate template.

Files of interest
-----------------
- `main.py` — agent wiring & `ResearchResponse` model
- `tools.py` — tools exposed to the agent
- `testing/pp_main.ipynb` — dataset analysis → PPTX example
- `requirements.txt` — installable dependencies

Contact / Contribution
----------------------
If you'd like more detailed developer docs, example outputs, or CI/test hooks added to this README, tell me which sections to expand and I will update it.