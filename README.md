# CoDoc AI

Welcome to CoDoc project API.
This API powered by [Crewai](https://www.crewai.com/) and [FastAPI](https://fastapi.tiangolo.com/)

## Demo & UI Links

* [Project Demo](https://codoc.onrender.com)
* [UI git repo](https://github.com/AiQotayba/codoc-ai)

## Installation

Ensure you have Python >=3.10 <3.13 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

```bash
cd hack4syria_medai && uv sync
```

Then, enable the virtual environment

```bash
source .venv/bin/activate
```

One last step is to make sure OpenAI keys are set

```bash
echo "MODEL=gpt-4o                                                                                                                                                              hack4syria-medai
OPENAI_API_KEY=sk-proj-xxx" > .env
```

### Customizing

- Modify `src/hack4syria_medai/config/agents.yaml` to define your agents
- Modify `src/hack4syria_medai/config/tasks.yaml` to define your tasks
- Modify `src/hack4syria_medai/crew.py` to add your own logic, tools and specific args
- Modify `src/hack4syria_medai/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

enable the virtual environment

```bash
source .venv/bin/activate
```

run (dev mode)

```bash
fastapi dev src/api/main.py
```

## Understanding Your Crew

The hack4syria_medai Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the CoDoc Project rise an issue on this repo or send email to [bassam.essam.ahmad@gmail.com](bassam.essam.ahmad@gmail.com)
