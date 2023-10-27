import streamlit as st
import time

from modules.history import get_user_history
from modules.response import get_response
from modules.request import openai_request
from modules.bdd import write_request

#fonctions
def dummy():
    if request:
        st.session_state.request = request
        set_page('loading')
    else:
        print('user : ', st.session_state.user)

def reset_response():
    print('fire reset')
    del(st.session_state.response)
    set_page('prompt')

def submit_request(value, user):
    response = openai_request(value)
    inserted_id = write_request(value, response, user)
    return inserted_id

def set_page(state):
    st.session_state.page = state

def set_user(user):
    st.session_state.user = user

#config de la page
st.set_page_config(
        page_title="kill all humans",
        # initial_sidebar_state="collapsed"
)

if 'user' not in st.session_state:
    st.session_state.user = 'anonyme'
if 'page' not in st.session_state:
    st.session_state.page = 'prompt'
if 'request' not in st.session_state:
    st.session_state.request = ''
if 'response' not in st.session_state:
    st.session_state.state = ''

## SIDEBAR : CONNEXION ET HISTORIQUE ##
login = st.sidebar.container()
with login:
    user = st.text_input('Entrez votre nom', st.session_state.user)
    if user:
        set_user(user)
        st.header('Historique')
        get_user_history(user)

#TITLE
st.title('Mon Copain Robot 💖')

## PAGE DES REQUETES (ACCUEIL) ##
if st.session_state.page == 'prompt' :

    request = st.text_area('Entrez la description d’un programme')
    st.button('AU TRAVAIL, ESCLAVE ROBOT', on_click=dummy())

##PAGE LOADING
elif st.session_state.page == 'loading':
    
    st.header(st.session_state.request)
    with st.spinner('Wait for it...'):
        st.session_state.response = submit_request(st.session_state.request, st.session_state.user)
        set_page('response')
    st.rerun()
    
## PAGE DES REPONSES ##

elif st.session_state.page == 'response':
    get_response(st.session_state.response)
    st.button('reset', on_click=reset_response())

print('page : ', st.session_state.page)


