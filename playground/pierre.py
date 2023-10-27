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
from key import api_key, MONGODB_URL



# Clé API
openai.api_key = API_KEY

# Configurez la connexion MongoDB
client = MongoClient(MONGODB_URL)
db = client.scoobyDB
collection = db.pierre





def get_code(user_prompt):
    messages = [{"role": "user", "content": user_prompt}]
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    return completion['choices'][0]['message']['content']

st.title("Quel code voulez-vous Générer")

# Formulaire pour que l'utilisateur entre son texte
user_input = st.text_input("Entrez votre demande ici :")





# Bouton pour générer la conclusion
if st.button("Générer le code"):
    if user_input:
        conclusion = get_code(user_input)
        st.subheader("Code généré :")
        st.write(conclusion)
        
        # document JSON test
        data_to_insert = {
            'user_input': user_input,
            'conclusion': conclusion,
            'utilisateur': "pierre"
        }

        # Insérez le document dans la collection MongoDB
        insert_result = collection.insert_one(data_to_insert)

        # Vérifiez l'insertion
        if insert_result.inserted_id:
            st.success(f'Données insérées avec succès. ID du document inséré : {insert_result.inserted_id}')
        else:
            st.error("Échec de l'insertion des données")

    else:
        st.warning("Veuillez entrer du texte pour générer du texte.")
    


# Affichage d'une liste de documents depuis la collection MongoDB
documents = collection.find({}, {"user_input": 1, "conclusion": 1, "_id": 0})  # "_id": 0 exclut l'ID

st.write("Liste des questions et des réponses :")

doc_list = list(documents)  # Convertissez le curseur en une liste
if doc_list:
    import pandas as pd
    df = pd.DataFrame(doc_list)

    # Renommer les colonnes
    df = df.rename(columns={"user_input": "Question", "conclusion": "Reponse"})

    st.dataframe(df)  # Affichez les données sous forme de tableau
else:
    st.write("Aucun document trouvé dans la collection.")



# Contenu de la variable fonction
fonction = "def add(a, b):\n    return a + b"

# Créer un éditeur de code
st.subheader("Éditeur de Code :")
code = st_ace(height=200, value=fonction, language='python', theme='pastel_on_dark', key="ace_editor")

# N'oubliez pas de fermer la connexion à la base de données
client.close()
