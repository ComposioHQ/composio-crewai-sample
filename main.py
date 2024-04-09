#!/usr/bin/env python
from serhant import SerhantCrew

from flask import Flask, request

app = Flask(__name__)

TRIGGER_ID = "ed7f8789-b93b-4636-9d34-c6376a9aef60"  # 53e67c17-c9a8-4d96-83ad-c7c508ffe462 example
CHANNEL_ID = "C06S0P99Q8G"  # Specify the Slack channel ID here to monitor and capture its messages


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
