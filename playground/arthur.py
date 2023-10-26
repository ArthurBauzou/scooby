import openai
from pymongo import MongoClient
from bson.objectid import ObjectId

from pprint import pprint
import streamlit as st

from config.key import MONGODB_URL, API_KEY2

# def main():

#     openai.api_key = API_KEY2

#     prompt = 'écris moi le code python d’un jeu SNAKE avec pygame'

#     response = openai.ChatCompletion.create(
#         model = 'gpt-3.5-turbo',
#         messages = [{'role': 'user', 'content': prompt}]
#     )

#     client = MongoClient(MONGODB_URL)
#     db = client.scoobyDB
#     my_collection = db.arthur

#     my_collection.insert_one(response)

#     resp = my_collection.find()

#     for r in resp:
#         pprint(r)

def main():
    
    client = MongoClient(MONGODB_URL)
    db = client.scoobyDB
    artable = db.arthur

    code = artable.find({"_id": ObjectId('653aa3dc8b5ef6fb42830417')})

    res = code[0]['choices'][0]['message']['content']

    st.write(res)