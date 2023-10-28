import streamlit as st
from pymongo import MongoClient, DESCENDING

from config.key import MONGODB_URL

client = MongoClient(MONGODB_URL)
db = client.scoobyDB
collection = db.requests

def get_post(id):
    print('id sent: ', id)
    st.session_state.response = id
    st.session_state.page = 'response'

def get_user_history(user):

    documents = collection.find({"user": user}).sort('date', DESCENDING)

    buttonstyle = '''
    <style>
        div[data-testid="stSidebarUserContent"] .stButton > button {
            width: calc(100%);
            text-align: start;
            display: block;
            float:left;
        }
        div[data-testid="stSidebarUserContent"] .stButton > button p {
            font-size: 0.8rem;
        }
    </style>
    '''
    st.markdown(buttonstyle, unsafe_allow_html=True)

    date = ''
    for i,doc in enumerate(documents):
        if date != doc["date"].strftime('%d/%m/%Y'):
            date = doc["date"].strftime('%d/%m/%Y')
            st.write(date)
        if st.button(doc["request"], key=i):
            get_post(doc['_id'])
