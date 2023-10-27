from pymongo import MongoClient

from config.key import MONGODB_URL
import datetime

client = MongoClient(MONGODB_URL)
db = client.scoobyDB
collection = db.requests

def write_request(req, res, user):
    data = {
        "date": datetime.datetime.now(),
        "user": user,
        "request": req,
        "code": [
            "bloc code 1",
            "bloc code 2"
        ],
        "cost": {
            "tokens": "à calculer",
            "dollars": "à calculer"
        },
        "raw": res
    }

    insert = collection.insert_one(data)

    return insert.inserted_id