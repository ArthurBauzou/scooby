import openai

from config.key import API_KEY

openai.api_key = API_KEY

def openai_request(prompt, max_tokens, temperature, system_prompt):

    response = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        messages = [
            {'role': 'system', 'content': system_prompt },
            {'role': 'user', 'content': prompt}
            ],
        temperature=temperature,
        stream=True,
        max_tokens= max_tokens
    )

    return response