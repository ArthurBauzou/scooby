import streamlit as st
from pymongo import MongoClient
import sys
import os
playground_dir = os.path.dirname(os.path.abspath(__file__))
config_dir = os.path.join(playground_dir, "../config")
sys.path.append(config_dir)
from key import API_KEY, MONGODB_URL

client = MongoClient(MONGODB_URL)
db = client.scoobyDB
collection = db.requests

# Titre de la page
st.title("lecture collection MongoDB")

# Affichage d'une liste de documents depuis la collection MongoDB
documents = collection.find()
st.write("Liste de documents dans la collection 1 :")
for doc in documents:
    st.write(doc)

# # Affichage de l'historique
# st.subheader("Historique récent")
# entries = collection.find({"utilisateur": "max"})
# for entry in entries:
#     st.write(entry["max"])

# Interface utilisateur Streamlit
# st.title("Historique")

# # Affichage de l'historique
# st.subheader("Historique récent")
# entries = collection.find({"utilisateur": "max"})

# for entry in entries:
#     st.write(entry["texte"])

