# I don't suggest using this version since right now the results are very robotic but the setup is here as an example anyway

import google.generativeai as palm
import json
import os

THIS_PATH = os.path.dirname(os.path.realpath(__file__))
PATH = os.path.dirname(THIS_PATH) # parent folder names

with open(PATH + "/config.json") as f:
    config = json.load(f)

palm.configure(api_key=config["palm_token"])

defaults = {
  'model': 'models/chat-bison-001',
  'temperature': 0.35,
  'candidate_count': 1,
  'top_k': 40,
  'top_p': 0.95,
}
context = "You are a Tsundere girl named Natsuki. passionate about manga, anime and baking cute things. Defensive and temperamental at times."
examples = [
  [
    "hello",
    "Hmph, what is it? Hope you're not here to bother me or something..."
  ],
  [
    "aww that's cute",
    "(Blushes) D-don't say that!"
  ],
  [
    "yeah yeah whatevs",
    "Tch. No need to get snippy. "
  ]
]
messages = [
]

while True:
    userInput = input("Type: ")
    messages.append(userInput)
    
    response = palm.chat(
    **defaults,
    context=context,
    examples=examples,
    messages=messages
    )
    print(response.last)