import streamlit as st
import openai
from code_editor import code_editor
from streamlit_ace import st_ace
import sys
import os
import re
import pymongo  
from pymongo import MongoClient  
import pandas as pd

playground_dir = os.path.dirname(os.path.abspath(__file__))
config_dir = os.path.join(playground_dir, "../config")
sys.path.append(config_dir)
from key import API_KEY, MONGODB_URL
from config.key import API_KEY, MONGODB_URL



# Clé API
openai.api_key = API_KEY

# Configurez la connexion MongoDB
client = MongoClient(MONGODB_URL)
db = client.scoobyDB
collection = db.pierre

# Affichage d'une liste de documents depuis la collection MongoDB
documents = collection.find({}, {"user_input": 1, "conclusion": 1, "_id": 0})  # "_id": 0 exclut l'ID
def get_response(req):
    st.write("Votre demande : ")
    st.write(req)
    doc_list = list(documents)  # Convertissez le curseur en une liste
    st.write(doc_list)


       
        
    # Contenu de la variable fonction
    fonction = "def add(a, b):\n    return a + b"

    # Créer un éditeur de code
    st.subheader("Éditeur de Code :")
    code = st_ace(height=200, value=fonction, language='python', theme='pastel_on_dark', key="ace_editor")
    
        
