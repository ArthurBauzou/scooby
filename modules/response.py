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
collection = db.requests


 
def get_response(req):
    st.write("Votre demande : ")
    st.write(req)
    
    # Filtrez les documents avec l'ID égal à req
    documents = collection.find({"_id": req}, {"request": 1, "raw.choices.message.content": 1}) 
    doc_list = list(documents)  # Convertissez le curseur en une liste

    if doc_list:
        # Obtenez le contenu brut de la première ligne
        raw_content = doc_list[0].get("raw", {}).get("choices", [])[0].get("message", {}).get("content", "")

        # Affichez le contenu
        st.text(raw_content)
    else:
        st.write("Aucun document trouvé dans la collection pour l'ID donné.")

    # Utilisez une expression régulière pour extraire le contenu entre ''' '''
    prog = re.search(r"'''(.*?)'''", raw_content, re.DOTALL)

    if prog:
        prog_content = prog.group(1)  # Récupérez le contenu entre les triplets de guillemets simples
        st.subheader("Éditeur de Code :")
        code = st_ace(height=200, value=prog_content, language='python', theme='pastel_on_dark', key="ace_editor")
    else:
        st.warning("Aucun contenu entre ''' ''' trouvé.")

        
