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
    st.write(resp['raw']['choices'][0]['message']['content'])