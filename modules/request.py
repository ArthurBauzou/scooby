import openai

from config.key import API_KEY

openai.api_key = API_KEY

def openai_request(prompt, max_t=600):

    response = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        messages = [
            # {'role': 'system', 'content': preprompt },
            {'role': 'user', 'content': prompt}
            ],
        temperature=1,
        stream=True,
        max_tokens= max_t
    )

    return response