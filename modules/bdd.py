from pymongo import MongoClient, DESCENDING
from bson.objectid import ObjectId

from config.key import MONGODB_URL
from .commons import parsecode
import datetime

client = MongoClient(MONGODB_URL)
db = client.scoobyDB
collection = db.requests


# ECRITURE NOUVEL OBJET DANS LA BASE
def write_request(req, res, user):

    language, code = parsecode(res)

    data = {
        "date": datetime.datetime.now(),
        "user": user,
        "request": req,
        "lang": language,
        "code": code,
        "raw": res,
        "newcode": ''
    }

    insert = collection.insert_one(data)

    return insert.inserted_id


# RECUPERER LES ID ET REQUEST D’UN UTILISATEUR SPECIFIQUE
def get_user_posts(user):
    res = collection.find({"user": user},{'request': 1, 'date':1}).sort('date', DESCENDING)
    return res

def get_response(id):
    resp = collection.find_one({"_id": ObjectId(id)})
    return resp

def save_newcode(id, newcode):
    if newcode == '' : return
    query = {'_id': id}
    insert = {'$set': {'newcode': newcode}}
    collection.update_one(query, insert)