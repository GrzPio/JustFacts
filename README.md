# Justfacts Crew

Welcome to the Justfacts Crew project, powered by [crewAI](https://crewai.com). The webapp fetches recent news for the given topic, summarizes the news articles, and checks the major claims against fact=checking sources.

## Installation

Ensure you have Python >=3.10 <3.14 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:
```bash
uv sync
```

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
### Configuration

**Add your `OPENAI_API_KEY`, API key for NewsAPI `NEWS_API_KEY`, and Google Fact Checking API `FACTCHECK_API_KEY` into the `.env` file**


## Running the Application

To run the application, activate your python environment
```bash
source venv/bin/activate
```
and run the application by
```bash
python3 webapp/app.py
```
The command line interface will output a link to access the webapp.
