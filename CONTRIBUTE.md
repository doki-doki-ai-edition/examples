## Tutorials
Below are some tutorials you can follow to get an understanding of how contributions are made (You only need to follow one but more are listed if 1 is too confusing).
1. https://www.youtube.com/watch?v=LuWAw-RBPys
2. https://docs.github.com/en/get-started/exploring-projects-on-github/contributing-to-a-project

# What to Contribute

Right now I'm only accepting prompts. So you're only meant to contribute in the `characters.json` for each model.

## Contribution Guidelines

Before you submit your contribution, **please ensure the following:**

The `characters.json` file follows this format: 
```json
"characterName_modelName_customName"
```

eg.

```json
"natsuki_gpt4_whatever"
```

Currently the `characters.json` look something like this:

```json
...

"natsuki_gpt4":
[
    {
        "role": "system",
        "content": ...
    },
    {
        "role": "user",
        "content": ...
    }
]
```


This is one of the default prompts. You would write your own version of whichever ddlc member(s) you want to change UNDER the last model in the json file you want to add a prompt to.

So for example if you were in the GPT section you would write under the last GPT model in the json.

```json

"natsuki_gpt4":
[
    {
        "role": "system",
        "content": ...
    },
    {
        "role": "user",
        "content": ...
    }
],

"natsuki_gpt4_LessMoody":
[
    {
        "role": "system",
        "content": ...
    },
    {
        "role": "user",
        "content": ...
    }
]
```

**DO NOT do something like this:**


```json

"natsuki_gpt4":
[
    {
        "role": "system",
        "content": ...
    },
    {
        "role": "user",
        "content": ...
    }
],

"natsuki_textbison001":
[
    "You will act as 'Natsuki'\n",
    "input: hey natsuki \noutput: Hmph, what is it? Hope you're not here to bother me or something...\n",
]
```

the `textbison` model already has a section above the gpt section and therefore your prompt should be positioned under the last `textbison` model.

#### Testing:
- If using GPT prompts it is recommended you do not use chatGPT to test your prompts, instead use the API directly.


#### Commit Messages

- Pull request descriptions should try to provide some context of what your prompt does (If it's something really minor then this isnt necessary).
