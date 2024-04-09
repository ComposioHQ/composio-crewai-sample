#!/usr/bin/env python
from dotenv import load_dotenv
load_dotenv()
from serhant import SerhantCrew
from flask import Flask, request
import os

app = Flask(__name__)

TRIGGER_ID = os.environ.get("TRIGGER_ID", None)
CHANNEL_ID = os.environ.get("CHANNEL_ID", None)

if TRIGGER_ID is None or CHANNEL_ID is None:
    print("Please set TRIGGER_ID and CHANNEL_ID environment variables in the .env file")
    exit(1)


def run_crew(topic: str):
    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    inputs = {"topic": topic}
    SerhantCrew().crew().kickoff(inputs=inputs)


async def async_run_crew(channel, text, user):
    if channel == CHANNEL_ID:
        run_crew(text)
    return "Crew run initiated", 200

@app.route("/", methods=["POST"])
async def webhook():
    payload = request.json
    # trigger_id = payload.get("trigger_id", {})
    # if trigger_id != TRIGGER_ID:
    print("Payload received", payload)

    print("Received payload:", payload)

    message_payload = payload.get("payload", {})

    channel = message_payload.get("channel", "")
    text = message_payload.get("text", "")
    user = message_payload.get("user", "")

    return await async_run_crew(channel, text=text, user=user)


if __name__ == "__main__":
    app.run(port=2000, debug=True)
