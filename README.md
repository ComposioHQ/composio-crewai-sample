# Client Crew - Building Agents with Composio and CrewAI

This is a starter repository for building agents with [Composio](composio.dev) and CrewAI. You can use this to update and build your own dynamic agents. This is an example for integrating Slack messages, conducting research, generating detailed analyses, and automating report creation in Notion.

## Overview

The project follows this workflow:

- Using Composio to get Slack messages.
- Using CrewAI to build two agents: one for researching the topic and the second for writing a detailed analysis on the topic.
- Using Composio to write the detailed report in Notion, sending a confirmation message to Slack.

Here's a visual representation of the workflow:

![Composio Image Diagram](assets/work_flow.png)

Below is the basic setup you can do to run the repository.

## Setup

1. **Environment Setup**

   Add a `.env` file and insert your OPENAI_API_KEY and Slack Channel ID:

   ```bash
   cp .env.sample .env && code .env
   ```

   **Note**: No need to add `TRIGGER_ID` in the `.env` file right now; we'll get to that in the next steps.

2. **Run setup script**

   This script installs necessary dependencies and tools for running the project.

   - Installs Poetry and project dependencies.
   - Installs Ngrok for tunneling.
   - Activates the Poetry shell for managing project dependencies.

   You can run this script to automate the setup process for your development environment.
   
   NB: Required Python version (>=3.10, <=3.13)

   ```bash
   chmod +x setup.sh && ./setup.sh
   ```

   Setup ngrok for tunneling and set up webhook (Use any method).
    - Using ngrok token
       ```bash
       ngrok config add-authtoken < your auth token >
       ```
    - Local ngrok setup
       ```bash
       ngrok http http://0.0.0.0:2000
       ```

3. **Composio Integration**

   Use Composio CLI to add integrations for Notion and Slack:

   ```bash
   poetry run composio-cli add notion
   poetry run composio-cli add slack
   ```

   Complete the authorization flows for Notion and Slack.

4. **Update the trigger callback URL**

   ```bash
   poetry run composio-cli set global-trigger-callback "<ngrok-url>"
   ```

5. **Enable Slack receive trigger**

   ```bash
   poetry run composio-cli enable-trigger slack_receive_message
   ```

   Update `TRIGGER_ID` in .env

6. **Run the Project**

   To start the AI agents and initiate task execution:

    ```bash
    poetry run python main.py
    ```
    
    This command initializes the Client Crew, assembling the agents and assigning them tasks according to the configuration.
    By default, it generates a `report.md` file with the output of research on LLMs in the root folder.
    
    Start sending messages to the Slack channel and see Composio in action, seamlessly updating Notion with detailed reports.
    
#### Public Server Setup

For public setups, directly set the global trigger callback to the public URL and enable the trigger.




## Customization

You can modify this repository to create additional agents for various tasks:

1. Add desired apps for authentication and use.
2. Modify `main.py` and `src/client/crew.py` for new functions.
3. Update `src/client/config/agents.yaml` and `src/client/config/tasks.yaml` for new agents and tasks.
4. Adjust any other environment variables as needed.

## Support

For support, questions, or feedback regarding the Client Crew or crewAI:

- Check out our [documentation](https://docs.composio.dev).
- Visit our [GitHub repository](https://github.com/SamparkAI/hermes).
- Join our [Discord community](https://discord.gg/xwT747R7NE).
