import openai
from pymongo import MongoClient

openai.api_key = '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'

prompt = 'Quelle version de GPT est en train de tourner ?'

client = MongoClient("mongodb://mongoscooby.ownedge.fr:27017/")
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