from pymongo import MongoClient

from config.key import MONGODB_URL
import datetime

client = MongoClient(MONGODB_URL)
db = client.scoobyDB
collection = db.requests


def parsecode(raw:str) -> (str, list):
    languages = [
        'python', 
        'javascript',
        'c',
        'c++',
        'c#',
        'php',
        'java',
        'sql'
    ]

    raw_list = raw.split('```')

    language = ''
    lang_found = False
    code = []
    for i, text in enumerate(raw_list):
        
        if i%2 == 0 : continue  # Recupérer uniquement les blocs de code (donc les elements impairs)

        words = text.split()

        if words[0] not in languages: continue  # vérifier que le langage est connu
        if lang_found and words[0] != language : continue # verifier que c’est bien le même langage

        lang_found = True
        language = words[0]
        code.append(text[len(language)+1:])

    return language, code

def write_request(req, res, user):

    language, code = parsecode(res)

    data = {
        "date": datetime.datetime.now(),
        "user": user,
        "request": req,
        "lang": language,
        "code": code,
        "raw": res
    }

    insert = collection.insert_one(data)

    return insert.inserted_id