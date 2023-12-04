# Basic threads test
# reference https://github.com/openai/openai-python/blob/main/examples/assistant.py

from openai import OpenAI
import json
import os
import time

THIS_PATH = os.path.dirname(os.path.realpath(__file__))
PATH = os.path.dirname(THIS_PATH) # parent folder name

with open(PATH + "/config.json") as f:
    config = json.load(f)

client = OpenAI(api_key=config["gpt_token"])
assistant = client.beta.assistants.create(
    name="Tsundere",
    instructions="You are a tsundere girl",
    model="gpt-4-1106-preview",
)

thread = client.beta.threads.create()

print("checking assistant status. ")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit':
        client.beta.assistants.delete(assistant.id)
        break

    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=user_input,
    )

    run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=assistant.id
    )

    run = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)

    # Check if text is generated
    while True:
        run_status = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)
        if run_status.status == "completed":
            print("Done!")
            break
        elif run_status.status == "failed":
            print("Failed to complete!")
            break
        else:
            print("Waiting for completion...")
            time.sleep(5)

    # Print bot msg once completed
    if run_status.status == "completed":
        messages = client.beta.threads.messages.list(thread_id=thread.id)
        for message in reversed(list(messages)):
            if message.role == "assistant":
                print(f"Bot: {message.content[0].text.value}\n")
    else:
        client.beta.assistants.delete(assistant.id)
        break