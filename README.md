Boiled down examples of how to use certain AI models.

Feel free to contribute better prompts for the characters.


# Setup

If you're using the APIs you need your own API key.

- Create a `config.json` file setup in the main folder
- Enter the token for the API you plan on using

`config.json`
```json
{
    "palm_token": "your api key",
    "gpt_token": "your api key"
}
```

## Get your PaLM token

- Go to https://developers.generativeai.google/products/palm and click "Get your API key"
<img src=".\assets\setup_imgs\palm\step1.png" alt="step 1">

- If you're signed into a google account you'll be taken to this page (If you're not signed in, simply sign in and you'll be taken here). Click Create API key.
<img src=".\assets\setup_imgs\palm\step2.png" alt="step 2">

- If you see this screen then the API might not be available in your region (or you're not signed in), check if it is here: https://developers.generativeai.google/available_regions

<img src=".\assets\setup_imgs\palm\step.png" alt="missing access">

- Copy your API key (Do not expose this, if you believe it has been leaked you can generate a new one)
<img src=".\assets\setup_imgs\palm\step3.png" alt="step 3">

## Get your GPT token

- Go to https://platform.openai.com/api-keys and login/sign up 
<img src=".\assets\setup_imgs\gpt\step1.png" alt="step 1">

- Click "Create new secret key"
<img src=".\assets\setup_imgs\gpt\step2.png" alt="step 2">

- Enter a name and click create
<img src=".\assets\setup_imgs\gpt\step3.png" alt="step 3">

- Copy your token (Do not expose this, if you believe it has been leaked you can generate a new one)
<img src=".\assets\setup_imgs\gpt\step4.png" alt="step 4">