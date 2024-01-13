import google.generativeai as genai
import os
import json

THIS_PATH = os.path.dirname(os.path.realpath(__file__))
PATH = os.path.dirname(THIS_PATH) # parent folder names

with open(PATH + "/config.json") as f:
    config = json.load(f)

genai.configure(api_key=config["gemini_token"])

# Set up the model
generation_config = {
    "temperature": 0.25,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 150,
    'stop_sequences': ['input:']
}

safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    }
]


with open(PATH + "/characters.json") as f:
    examples = json.load(f)['natsuki_geminipro'] # Change to the name of doki you want to interact with

try:
    with open(THIS_PATH + "/chat_history.json") as f:
        msgs = json.load(f) # Loads previous chat history if it exists
                            # (which means u have to delete the old 1 if u want to test a new doki)
except FileNotFoundError:
    with open(THIS_PATH + "/chat_history.json", 'w') as f:
        json.dump(examples, f, indent=2)

    with open(THIS_PATH + "/chat_history.json") as f:
        msgs = json.load(f)


model = genai.GenerativeModel(model_name="gemini-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

system_message = examples[0]
chat_history = examples


while True:
    userinput = input("Start talking: ")

    prompt = system_message + "\n ".join(chat_history) + f"input: {userinput}\n output: "

    if userinput == 'exc':
        print(f"**CURRENT HISTORY**\n {chat_history}")
        continue

    response = model.generate_content(prompt)
    chat_history.append(f"input: {userinput}\n output: {response.text}")
    print(response.text)