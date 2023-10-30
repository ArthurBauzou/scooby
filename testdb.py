from pymongo import MongoClient, DESCENDING
from pprint import pprint

from config.key import MONGODB_URL
import datetime

client = MongoClient(MONGODB_URL)
db = client.scoobyDB
collection = db.requests


def get_user_posts(user):
    res = collection.find({"user": user},{'request': 1}).sort('date', DESCENDING)
    return res

hist = get_user_posts('anonyme')

# print(len(hist))

for a in hist:
    pprint(a)