import streamlit as st
from pymongo import MongoClient
import sys
import os
from config.key import MONGODB_URL

client = MongoClient(MONGODB_URL)
db = client.scoobyDB
collection = db.pierre



def get_user_history(user):
    st.write(f"voici l’histo de {user}")
    pass

    # champ_a_afficher = "user_input"
    # valeurs_distinctes = collection.distinct(champ_a_afficher)
    
    # for valeur in valeurs_distinctes:
    #     st.write(valeurs_distinctes)

    documents = collection.find({"utilisateur": user})
    st.write("Liste de documents dans la collection 1 :")
    for doc in documents:
        st.write(doc["user_input"])