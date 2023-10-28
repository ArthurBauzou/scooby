#from config.key import API_KEY , MONGODB_URL
from pymongo import MongoClient
from pprint import pprint
import streamlit as st

import openai

##########################################
import sys
import os
playground_dir = os.path.dirname(os.path.abspath(__file__))
config_dir = os.path.join(playground_dir, "../config")
sys.path.append(config_dir)
##########################################""
from key import API_KEY, MONGODB_URL

def main():

    openai.api_key = API_KEY

    prompt = 'code moi une fonction qui reconnait le string "coucou" en python'

    client = MongoClient(MONGODB_URL)
    db = client.scoobyDB
    my_collection = db.requests


    
    # Titre de la page
    st.title("lecture collection MongoDB")

    # parcer
    documents = my_collection.find()

    print("\n")
    #doc = documents[0]["choices"][0]["message"]["content"]
    doc = documents[30]["raw"]

    pprint("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!",doc)
    print("\n")
    Splited_list= doc.split("```")
    for i in range(len(Splited_list)):
        if ("python" in Splited_list[i]):
            st.write("```"+Splited_list[i]+"```")



main()



