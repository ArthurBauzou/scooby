import streamlit as st
from pymongo import MongoClient
from bson.objectid import ObjectId

from config.key import MONGODB_URL

client = MongoClient(MONGODB_URL)
db = client.scoobyDB
collection = db.requests

def get_response(id):

    resp = collection.find_one({"_id": ObjectId(id)})
    st.header(resp['request'])

    if len(resp["code"]) == 0 : st.error('aucun code n’a pu être généré')
    else :
        joined_code = "\n####\n".join(resp["code"])
        codeblock = f'```{resp["lang"]}\n{joined_code}```'

        st.success(f'langage : {resp["lang"]}')
        st.write(codeblock)

