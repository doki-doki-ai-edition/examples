# using the text-bison-001 model ( which sounds less robotic )

import google.generativeai as palm
import os
import json
from pprint import pprint

THIS_PATH = os.path.dirname(os.path.realpath(__file__))
PATH = os.path.dirname(THIS_PATH) # parent folder name
with open(PATH + "/config.json") as f:
    config = json.load(f)

palm.configure(api_key=config["palm_token"])
defaults = {
  'model': 'models/text-bison-001',
  'temperature': 0.7,
  'candidate_count': 1,
  'top_k': 40,
  'top_p': 0.95,
  'max_output_tokens': 250,
  'stop_sequences': []
}

with open(THIS_PATH + "/characters.json") as f:
    context = json.load(f)['yuri'] # Change to the name of doki you want to interact with

system = context[0]
chat_history = context


while True:

    userinput = input("Start talking: ")

    prompt = system + "\n ".join(chat_history) + f"input: {userinput}\n output: "

    if userinput == 'exc':
        pprint(f"**CURRENT HISTORY**\n {chat_history}")
        continue

    response = palm.generate_text(
    **defaults,
    prompt=prompt
    )
    chat_history.append(f"input: {userinput}\n output: {response.result}")
    print(response.result)