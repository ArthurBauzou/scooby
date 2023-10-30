import streamlit as st
from pymongo import MongoClient
from bson.objectid import ObjectId
from streamlit_ace import st_ace
import sys
from io import StringIO
from config.key import MONGODB_URL

client = MongoClient(MONGODB_URL)
db = client.scoobyDB
collection = db.requests

def get_response(id):

    resp = collection.find_one({"_id": ObjectId(id)})
    st.header(resp['request'])
    st.write(resp['raw']['choices'][0]['message']['content'])
    
    
    
    # Affichez le contenu du champ 'content' dans un éditeur de code
    prog = "```" + resp['raw']['choices'][0]['message']['content'] + "```"
    
    st.subheader("Éditeur de Code :")
    
    code = st_ace(height=200, value=prog, language='python', theme='pastel_on_dark', key="ace_editor", readonly=True)
    
    # Rediriger la sortie standard vers une variable
    original_stdout = sys.stdout
    sys.stdout = StringIO()

    program = 'a = 5\nb=10\nprint("Sum =", a+b)'

    exec(program)

    # Capturer la sortie dans une variable
    captured_output = sys.stdout.getvalue()

    # Rétablir la sortie standard d'origine
    sys.stdout = original_stdout

    # Afficher la sortie capturée
    st.write("Résultat de l'exécution du code :")
    st.code(captured_output)
        