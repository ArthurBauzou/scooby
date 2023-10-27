import streamlit as st
from pymongo import MongoClient
import sys
import os
from config.key import API_KEY, MONGODB_URL

client = MongoClient(MONGODB_URL)
db = client.scoobyDB
collection = db.requests

# def get_user_history(user):
#     st.write(f"Historique de {user}")
#     pass

#     # champ_a_afficher = "user_input"
#     # valeurs_distinctes = collection.distinct(champ_a_afficher)
    
#     # for valeur in valeurs_distinctes:
#     #     st.write(valeurs_distinctes)

#     documents = collection.find({"utilisateur": user})
#     st.write()
#     for doc in documents:
#         st.write(doc["user_input"])

def get_user_history(user):
    st.write(f"Historique de {user}")

    documents = collection.find({"user": user})

    for doc in documents:
        if st.checkbox(f"Afficher ligne {doc['_id']}"):
            request = doc["request"]
            st.write(request)


# def get_user_history(user):
#     st.write(f"Historique de {user}")

#     documents = collection.find({"utilisateur": user})

#     for i,doc in enumerate(documents):
#         user_input = doc["user_input"]
#         if st.checkbox(
#             label = f"c{i}",
#             value = f"Afficher ligne '{doc['user_input']}'",
#             ):
#             st.write(user_input)