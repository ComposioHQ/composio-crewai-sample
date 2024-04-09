# Matter Crew

Welcome to the Matter Crew project, powered by [crewAI](https://crewai.com). This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

### Composio
1. Add .env file and add your OPENAI_API_KEY
```
cp .env.sample .env && code .env
```

2. Run setup script
```bash
chmod +x setup.sh && ./setup.sh
```

**For the auth management and integrations, let's use Composio**

3. Use Composio CLI
```bash
composio-cli add notion
composio-cli add slack
```

Go through the flow to notion, and complete the authorization flow.

### To setup slack trigger to get messages:
You need to either create a public server or tunnel to setup webhook to get messages from composio.

#### Local setup
4. To tunnel to setup webhook to get messages from composio, you can use ngrok.
```bash
ngrok http http://0.0.0.0:2000
```
5. Add your trigger callback URL - URL of your server where your agent will recieve all the update
```bash
poetry run composio-cli set global-trigger-callback "<ngrok-url>"
```
This will setup the callback url to get messages from composio.

6. Enable slack recieve trigger
```bash
poetry run composio-cli enable-trigger slack_receive_message
```
This will enable the trigger to get messages from slack when a message is sent.

7. Now edit the .env file again, and update `TRIGGER_ID` and `CHANNEL_ID`
```bash
code .env
```

Instructions:
- You'll get the `TRIGGER_ID` when you run step (6)
- To get `CHANNEL_ID` go to slack channel settings and you'll see it at the end of about settings

#### Public server setup
Public setup doesn't require ngrok and you can directly set global-trigger-callback to the public url and enable the trigger.

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
poetry run python main.py
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
