import openai
from pymongo import MongoClient

from pprint import pprint

from config.key import API_KEY2, MONGODB_URL

def main():

    openai.api_key = API_KEY2

    prompt = 'J’essaie de savoir combien coûte l’accès à l’API d’openAI. Sois bref par ce que je suis pauvre, s’il te plait'

    client = MongoClient(MONGODB_URL)
    db = client.scoobyDB
    my_collection = db.arthur

    resp = my_collection.find()

    # print(resp['choices'][0]['message']['content'])
    for r in resp:
        pprint(r)

    # response = openai.ChatCompletion.create(
    #     model = 'gpt-3.5-turbo',
    #     messages = [{'role': 'user', 'content': prompt}]
    # )

    # my_collection.insert_one(response)