import streamlit as st
from pymongo import MongoClient

from config.key import MONGODB_URL

client = MongoClient(MONGODB_URL)
db = client.scoobyDB
collection = db.requests

def get_post(id):
    print('id sent: ', id)
    st.session_state.response = id
    st.session_state.page = 'response'

def get_user_history(user):
    st.write(f"Historique de {user}")

    documents = collection.find({"user": user})

    for i,doc in enumerate(documents):
        if st.button(doc["request"][:28]+'…', key=i):
            get_post(doc['_id'])
