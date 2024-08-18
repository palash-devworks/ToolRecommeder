# Tool Recommender

Welcome to the Tool Recommender project, created with [crewAI](https://crewai.com). This project leverages a multi-agent AI system to recommend tools for specific use cases across various industries. By utilizing the powerful and flexible framework provided by crewAI, we enable our AI agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

## Installation

Ensure you have Python >=3.10 <=3.13 installed on your system. This project uses [Poetry](https://python-poetry.org/) for dependency management.

1. Install Poetry if you haven't already:
```bash
pip install poetry
```

2. Navigate to your project directory and install the dependencies:
```bash
poetry lock
poetry install
```

## Configuration

1. Add your keys
    `OPENAI_API_KEY` to the `.env` file in the `crew` directory.
    `OPENAI_ORGANIZATION_ID` to the `.env` file in the `crew` directory.
    `SERPER_API_KEY` to the `.env` file in the `crew` directory.
    `AGENTOPS_API_KEY` to the `.env` file in the `crew` directory. // remove agentops.init() references from main.py if not needed

2. Customize the project:
   - Modify `src/crew/config/agents.yaml` to define your agents
   - Modify `src/crew/config/tasks.yaml` to define your tasks
   - Adjust `src/crew/crew.py` to add your own logic, tools, and specific arguments
   - Update `src/crew/main.py` to add custom inputs for your agents and tasks

## Running the Project

To start your crew of AI agents and begin the tool recommendation process, run this command from the root folder of your project:

```bash
poetry run crew
```

This command initializes the Tool Recommender Crew, assembling the agents and assigning them tasks as defined in your configuration.

## Using the Tool Recommender API

The project includes a Flask-based API service. To run the service:

```bash
poetry run serve
```

This will start the Flask server, allowing you to interact with the Tool Recommender through HTTP requests.

### Making a Recommendation Request

To get a tool recommendation, you can use the following curl command:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"industry": "construction industry", "use_case": "Keep track of the deal pipeline. Let other input and view their deals. I have a 6 people team. I want to view the whole pipeline but want to control what others can see.", "other_requirements": "It should be easy to use. Should be cost effective, yet scalable when I grow the company. Permissions and access controls are important."}' http://127.0.0.1:5000/run_crew
```

This will trigger the AI agents to analyze your requirements and provide a recommendation.

## Understanding Your Crew

The Tool Recommender Crew consists of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks to provide comprehensive tool recommendations. The crew includes:

1. Market Researcher
2. Comparative Analyst
3. Requirements Clarifier
4. Recommendation Specialist
5. Industry Expert
6. Technical Evaluator
7. User Experience Specialist
8. Cost-Benefit Analyst
9. Implementation Strategist

Each agent performs specific tasks in the recommendation process, from initial research to final implementation strategies.
