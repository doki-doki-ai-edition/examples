# Info

This is legacy code for how the PaLM model was used. **Gemini** is now recommended.


## Old Info
The `text-bison-001` model in `palm-test.py` is less robotic sounding compared to the other chat model, so I'd recommend experimenting with `palm-test.py`


# Old Setup Info

## pip install
`pip install google-generativeai`

## config.json
```json
{
    "palm_token": "your api key"
}
```


## Get your PaLM token

- Go to https://developers.generativeai.google/products/palm and click "Get your API key"
<img src="..\assets\setup_imgs\legacy-palm\step1.png" alt="step 1">

- If you're signed into a google account you'll be taken to this page (If you're not signed in, simply sign in and you'll be taken here). Click Create API key.
<img src="..\assets\setup_imgs\legacy-palm\step2.png" alt="step 2">

- If you see this screen then the API might not be available in your region (or you're not signed in), check if it is here: https://developers.generativeai.google/available_regions

<img src="..\assets\setup_imgs\legacy-palm\step.png" alt="missing access">

- Copy your API key (Do not expose this, if you believe it has been leaked you can generate a new one)
<img src="..\assets\setup_imgs\legacy-palm\step3.png" alt="step 3">
