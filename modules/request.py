import openai
from config.key import API_KEY

openai.api_key = API_KEY

def openai_request(prompt):

    response = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        messages = [
            # {'role': 'system', 'content': preprompt },
            {'role': 'user', 'content': prompt}
            ]
    )

    return response