import streamlit as st
from pymongo import MongoClient
from config.key import API_KEY2, MONGODB_URL

client = MongoClient(MONGODB_URL)
db = client.scoobyDB
collection = db.max

# Titre de la page
st.title("lecture collection MongoDB")

# Affichage d'une liste de documents depuis la collection MongoDB
documents = collection.find()
st.write("Liste de documents dans la collection :")
for doc in documents:
    st.write(doc)