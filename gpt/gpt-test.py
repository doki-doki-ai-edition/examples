from openai import OpenAI
import json
import os

THIS_PATH = os.path.dirname(os.path.realpath(__file__))
PATH = os.path.dirname(THIS_PATH) # parent folder name


with open(PATH + "/config.json") as f:
    config = json.load(f)

with open(PATH + "/characters.json") as f:
    characters = json.load(f)['sayori_gpt4'] # Change to the name of doki you want to interact with

try:
    with open(THIS_PATH + "/chat_history.json") as f:
        msgs = json.load(f) # Loads previous chat history if it exists
                            # (which means u have to delete the old 1 if u want to test a new doki)
except FileNotFoundError:
    with open(THIS_PATH + "/chat_history.json", 'w') as f:
        json.dump(characters, f, indent=2)

    with open(THIS_PATH + "/chat_history.json") as f:
        msgs = json.load(f)

client = OpenAI(api_key=config["gpt_token"])

while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit':
        exit()

    msgs.append({"role": "user", "content": user_input})
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-16k", # gpt-4-1106-preview, gpt-3.5-turbo-16k
        messages=msgs
    )
    bot_output = response.choices[0].message.content
    msgs.append({"role": "assistant", "content": bot_output})

    with open(THIS_PATH + "/chat_history.json", 'w') as f:
        json.dump(msgs, f, indent=2)

    print("Bot:", bot_output)
