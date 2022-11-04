import os
import openai
openai.api_key = os.environ.get("OPENAI_KEY")

MODEL="text-davinci-002"

def ask_prompt(prompt, model=MODEL, num_results=1, max_tokens=250, stopSequences=["You:", "Zizek:"],
                  temperature=1.0, topP=1.0, topKReturn=2):
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=topP,
        frequency_penalty=2.0,
        presence_penalty=2.0,
        stop=stopSequences
    )
    if response != 0:
        for choice in response.choices:
            return choice.text
    return "[idk]"
