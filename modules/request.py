import openai
from config.key import API_KEY

openai.api_key = API_KEY

pre = 'You are a programmer assistant, you will only write clear and clean code'

def openai_request(prompt, preprompt=pre):

    response = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        messages = [
            {'role': 'system', 'content': preprompt },
            {'role': 'user', 'content': prompt}
            ]
    )

    return response