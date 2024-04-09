pip install poetry
poetry add crewai
poetry add composio_crewai 
poetry add composio_langchain 
poetry add composio_core
poetry add flask
poetry lock && poetry install
curl -s https://ngrok-agent.s3.amazonaws.com/ngrok.asc | sudo tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null && echo "deb https://ngrok-agent.s3.amazonaws.com buster main" | sudo tee /etc/apt/sources.list.d/ngrok.list && sudo apt update && sudo apt install ngrok
ngrok config add-authtoken 1cUL5fKjAVu1XMZdICmxv1EpTVd_22pfqPT7aqNq1DiyqCmH
poetry shell