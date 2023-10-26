#import openai
from pymongo import MongoClient

#openai.api_key = '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'

prompt = 'Quelle version de GPT est en train de tourner ?'

client = MongoClient("mongodb://mongoscooby.ownedge.fr:17027/")
db = client.scoobyDB
my_collection = db.arthur
print(my_collection.find()[0])