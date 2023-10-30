import streamlit as st
import random as rd

from modules.history import get_user_history
from modules.response import show_code_edit
from modules.request import openai_request
from modules.bdd import write_request, get_response

#fonctions
def confirm_prompt():
    if request:
        st.session_state.request = request
        set_page('loading')
    else:
        print('no prompt')

def reset_response():
    print('fire reset')
    del(st.session_state.response)
    set_page('prompt')

def submit_request(request, user, chunks_counter):
    stream = openai_request(request)

    collected_messages = []
    for chunk in stream:
        chunk_message = chunk['choices'][0]['delta']
        collected_messages.append(chunk_message)
        chunks_counter.write(f'tokens reçus : {len(collected_messages)}')
    response = ''.join([m.get('content', '') for m in collected_messages])

    inserted_id = write_request(request, response, user)
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
        st.header(f'Historique de {st.session_state.user}')
        get_user_history(user)

#TITLE
st.title('Mon Copain Robot 💖')
st.divider()

## PAGE DES REQUETES (ACCUEIL) ##
if st.session_state.page == 'prompt' :

    request = st.text_area('Entrez la description d’un programme')
    if st.button('AU TRAVAIL, ESCLAVE ROBOT'):
        confirm_prompt()
        st.rerun()

##PAGE LOADING
elif st.session_state.page == 'loading':
    
    st.header(st.session_state.request)
    with st.spinner('Wait for it...'):
        token_count = st.empty()
        st.image(f'./static/copain ({rd.choice(range(1,9))}).gif')
        st.session_state.response = submit_request(st.session_state.request, st.session_state.user, token_count)
        set_page('response')
    st.rerun()
    
## PAGE DES REPONSES ##

elif st.session_state.page == 'response':

    resp = get_response(st.session_state.response)
    st.header(resp['request'])

    editor, raw = st.tabs(['Éditeur de code', 'Réponse de GPT'])
    with editor: show_code_edit(resp)
    with raw: st.write(resp['raw'])

    st.divider()
    if st.button('NOUVELLE REQUÊTE'):
        reset_response()
        st.rerun()

print('PAGE: ', st.session_state.page, ', USER: ', st.session_state.user)



