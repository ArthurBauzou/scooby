import openai
from pymongo import MongoClient

from config.key import API_KEY, MONGODB_URL

openai.api_key = API_KEY

prompt = 'Quelle version de GPT est en train de tourner ?'

client = MongoClient(MONGODB_URL)
db = client.scoobyDB
my_collection = db.arthur

# dummy = {
#     "user": "arthur",
#     "role": "programmer"
# }

# my_collection.insert_one(dummy)

print(my_collection.find()[0])


# response = openai.ChatCompletion.create(
#     model = 'gpt-3.5-turbo',
#     messages = [{'role': 'user', 'content': prompt}]
# )

# print(response)