# main.py

import os

from dotenv import load_dotenv
from flask import Flask, request

load_dotenv()

from client import ClientCrew

app = Flask(__name__)

TRIGGER_ID = os.environ.get("TRIGGER_ID", None)
CHANNEL_ID = os.environ.get("CHANNEL_ID", None)

if TRIGGER_ID is None or CHANNEL_ID is None:
    print("Please set TRIGGER_ID and CHANNEL_ID environment variables in the .env file")
    exit(1)


def run_crew(topic: str):
    inputs = {"topic": topic}
    ClientCrew().crew().kickoff(inputs=inputs)


async def async_run_crew(channel, text, user):
    if channel == CHANNEL_ID:
        run_crew(text)
    return "Crew run initiated", 200


@app.route("/", methods=["POST"])
async def webhook():
    payload = request.json

    message_payload = payload.get("payload", {})
    channel = message_payload.get("channel", "")

    if channel == CHANNEL_ID:
        print("Payload received", payload)

    text = message_payload.get("text", "")
    user = message_payload.get("user", "")

    return await async_run_crew(channel, text=text, user=user)


if __name__ == "__main__":
    app.run(port=2000, debug=True)
