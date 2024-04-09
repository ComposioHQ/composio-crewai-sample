# Matter Crew

Welcome to the Matter Crew project, powered by [crewAI](https://crewai.com). This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

### Composio
Run setup script
```bash
chmod +x setup.sh && ./setup.sh
```

**For the auth management and integrations, let's use Composio**

```bash
composio-cli add notion
composio-cli add slack
```

Go through the flow to notion, slack

### To setup slack trigger to get messages:
You need to either create a public server or tunnel to setup webhook to get messages from composio.

#### Local setup
To tunnel to setup webhook to get messages from composio, you can use ngrok.
```bash
ngrok http http://0.0.0.0:2000
```
```bash
composio-cli set global-trigger-callback "<ngrok-url>"
```
This will setup the callback url to get messages from composio.

```bash
composio-cli enable-trigger slack_receive_message
```
This will enable the trigger to get messages from slack when a message is sent.

#### Public server setup
Public setup doesn't require ngrok and you can directly set global-trigger-callback to the public url and enable the trigger.


### Customizing

**Add `OPENAI_API_KEY` in src/serhant/crew.py.**

- Modify `src/serhant/config/agents.yaml` to define your agents
- Modify `src/serhant/config/tasks.yaml` to define your tasks
- Modify `src/serhant/crew.py` to add your own logic, tools and specific args
- Modify `src/serhant/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
poetry shell
python main.py
```

This command initializes the serhant Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folser

## Understanding Your Crew

The serhant Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the Serhant Crew or crewAI.

- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Joing our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat wtih our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.
