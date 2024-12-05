from AI_core import RepintelAI

# 🔎 RepIntel AI
[![Official Website](https://img.shields.io/badge/Official%20Website-repintelai.dev-blue?style=for-the-badge&logo=world&logoColor=white)](https://repintelai.dev)
[![Discord Follow](https://dcbadge.vercel.app/api/server/QgZXvJAccX?style=for-the-badge)](https://discord.com/invite/QgZXvJAccX)

[![GitHub Repo stars](https://img.shields.io/github/stars/assafelovic/RepIntel_AI?style=social)](https://github.com/assafelovic/RepIntel_AI)
[![Twitter Follow](https://img.shields.io/twitter/follow/tavilyai?style=social)](https://twitter.com/tavilyai)
[![PyPI version](https://badge.fury.io/py/RepIntel_AI.svg)](https://badge.fury.io/py/RepIntel_AI)

**RepIntel AIis an autonomous agent designed for comprehensive online research on a variety of tasks.** 

The agent can produce detailed, factual and unbiased research reports, with customization options for focusing on relevant resources, outlines, and lessons. Inspired by the recent [Plan-and-Solve](https://arxiv.org/abs/2305.04091) and [RAG](https://arxiv.org/abs/2005.11401) papers, RepIntel AIaddresses issues of speed, determinism and reliability, offering a more stable performance and increased speed through parallelized agent work, as opposed to synchronous operations.

**Our mission is to empower individuals and organizations with accurate, unbiased, and factual information by leveraging the power of AI.**

#### PIP Package
> **Step 0** - Install Python 3.11 or later. [See here](https://www.tutorialsteacher.com/python/install-python) for a step-by-step guide.
> **Step 1** - install RepIntel AIpackage [PyPI page](https://pypi.org/project/RepIntel_AI/)
```bash
$ pip install repintelai
```
> **Step 2** - Create .env file with your OpenAI Key and Tavily API key or simply export it
```bash
$ export OPENAI_API_KEY={Your OpenAI API Key here}
```
```bash
$ export TAVILY_API_KEY={Your Tavily API Key here}
```
> **Step 3** - Start Coding using RepIntel AIin your own code, example:

```python
from AI_core import RepintelAI

import asyncio


async def get_report(query: str, report_type: str) -> str:
    researcher = RepintelAI(query, report_type)
    report = await researcher.run()
    return report


if __name__ == "__main__":
    query = "what team may win the NBA finals?"
    report_type = "research_report"

    report = asyncio.run(get_report(query, report_type))
    print(report)

```

### Customize the configuration (optional)
This will override the default settings with your custom configuration. You can find all available configuration options in the [RepIntel AIdocumentation](https://docs.repintelai.dev/docs/RepIntel_AI/repintelai/config).


#### Using a Custom JSON Configuration

If you want to modify the default configuration of RepIntel AI, you can create a custom JSON configuration file. This allows you to tailor the researcher's behavior to your specific needs. Here's how to do it:

a. Create a JSON file (e.g., `your_config.json`) with your desired settings:

```json
{
  "retrievers": ["google"],
  "fast_llm": "cohere:command",
  "smart_llm": "cohere:command-nightly",
  "max_iterations": 3,
  "max_subtopics": 1
}
```

b. When initializing the RepintelAI, pass the path to your custom configuration file:

```python
researcher = RepintelAI(query, report_type, config_path="your_config.json")
```

#### Using Environment Variables

Alternatively, you can set up the same configuration using environment variables instead of a JSON file. Here's how the example from Part 1 would look in your `.env` file:

```
RETRIEVERS=google
FAST_LLM=cohere:command
SMART_LLM=cohere:command-nightly
MAX_ITERATIONS=3
MAX_SUBTOPICS=1
```

Simply add these lines to your `.env` file, and RepIntel AIwill use the environment variables to configure its behavior. This approach provides flexibility when deploying in different environments.