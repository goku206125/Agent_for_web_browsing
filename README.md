# Advanced Web Research Agent with LangGraph and Firecrawl

This project is an advanced AI agent designed for comprehensive web research and analysis, built by following the "Python Advanced AI Agent Tutorial" by Tech with Tim. The agent leverages a stateful, cyclical graph structure using LangGraph to perform robust, multi-step research tasks that mimic a human's research process.

## 🚀 Overview

The core of this project is a sophisticated agent that can take a research query, break it down, browse the web for relevant information, and synthesize the findings into a coherent report. Unlike simple linear agents, this implementation uses LangGraph to create a more dynamic and resilient workflow, allowing the agent to self-correct, reflect on its findings, and decide the best next action.

The primary goal of my implementation was to create an agent that can do some shit for you guys like looking for a speficic person linkedin profile or browsing website for an character or whatever you want. But above all, you can have your own personal assistant. All you need to do is create .env file and put API keys from either Google gemini or OpenAi or whaterver provider you want. And your agent is good to go.

## ✨ Features

- **Stateful Agentic Workflow**: Built with LangGraph to manage a persistent state, enabling complex, multi-step reasoning.
- **Dynamic Web Crawling**: Utilizes Firecrawl to efficiently scrape and extract clean, relevant data from web pages.
- **Real-time Search**: Integrates with Tavily Search API for optimized, real-time information retrieval relevant to the agent's task.
- **Self-Correction and Reflection**: The agent can evaluate its search results and refine its plan, leading to more accurate and comprehensive outcomes.
- **LLM Integration**: Powered by OpenAI's models (or your choice of LLM) for natural language understanding, planning, and generation.
- **Structured Output**: Generates a well-formatted research report based on the information it gathers.

## 🛠️ Tech Stack

- **Core Logic**: Python
- **Agent Framework**: LangChain & LangGraph
- **Web Scraping & Crawling**: Firecrawl
- **Search API**: Tavily Search
- **LLM Provider**: Gemini
- **Environment Management**: Conda & Pip
- **Secrets Management**: `python-dotenv`

## ⚙️ Setup and Installation

Follow these steps to get the project up and running on your local machine.

### 1. Clone the Repository


git clone https://github.com/[your-username]/[your-repository-name].git
cd [your-repository-name]

### 2. Set Up a Conda Environment

# Create and activate the conda environment
conda create --name agent-env python=3.11 -y
conda activate agent-env

# Add conda-forge channel
conda config --add channels conda-forge
conda config --set channel_priority strict.

### 3. Set Up a Conda Environment

# Install conda packages
conda install langchain langgraph langchain-openai python-dotenv beautifulsoup4

# Install pip packages
pip install firecrawl-py tavily-python

### 4. Configure Environment Variables

You will need API keys for OpenAI, Firecrawl, and Tavily.
Create a file named .env in the root of the project.
Add your API keys to the .env file as follows:
OPENAI_API_KEY="sk-..."
FIREcrawl_API_KEY="fc-..."
TAVILY_API_KEY="tvly-..."


### 5. Please it is very important  Create a .gitignore file

If you don't have one, create a file named .gitignore and add the following line to it:

.env

### 6.  Just type python main.py and your agent is up and running the terminal


