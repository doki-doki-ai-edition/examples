Boiled down examples of how to use certain AI models.

Feel free to contribute better prompts for the characters.


# Setup

`pip install google-generativeai`

`pip install openai`


If you're using the APIs you need your own API key.

- Create a `config.json` file setup in the main folder
- Enter the token for the API you plan on using

`config.json`
```json
{
    "gemini_token": "your api key",
    "gpt_token": "your api key"
}
```

Note: You don't need to get both tokens if you're only going to use one.

## Get your Gemini token

- Go to https://ai.google.dev/pricing and click "Get API key"
<img src=".\assets\setup_imgs\gemini\step1.png" alt="step 1">

- If you're signed into a google account you'll be taken to this page https://makersuite.google.com/app/apikey (If you're not signed in, simply sign in and you'll be taken here). Click Create API key.
<img src=".\assets\setup_imgs\gemini\step2.png" alt="step 2">

- If you see this screen then the API might not be available in your region (or you're not signed in), check if it is here: https://developers.generativeai.google/available_regions

<img src=".\assets\setup_imgs\gemini\step.png" alt="missing access">

- Copy your API key (Do not expose this, if you believe it has been leaked you can generate a new one)
<img src=".\assets\setup_imgs\gemini\step3.png" alt="step 3">

## Get your GPT token

- Go to https://platform.openai.com/api-keys and login/sign up 
<img src=".\assets\setup_imgs\gpt\step1.png" alt="step 1">

- Click "Create new secret key"
<img src=".\assets\setup_imgs\gpt\step2.png" alt="step 2">

- Enter a name and click create
<img src=".\assets\setup_imgs\gpt\step3.png" alt="step 3">

- Copy your token (Do not expose this, if you believe it has been leaked you can generate a new one)
<img src=".\assets\setup_imgs\gpt\step4.png" alt="step 4">