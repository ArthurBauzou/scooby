import streamlit as st

from modules.history import get_user_history
from modules.response import get_response
from modules.request import openai_request
from modules.bdd import write_request

#fonctions
def submit_request(value, user):
    response = openai_request(value)
    inserted_id = write_request(value, response, user)
    st.session_state.request = inserted_id

#config de la page
st.set_page_config(
        page_title="AWESOME O",
        initial_sidebar_state="collapsed"
)


if 'user' not in st.session_state:
    st.session_state.user = 'anonyme'

## SIDEBAR : CONNEXION ET HISTORIQUE ##
login = st.sidebar.container()
with login:
    user = st.text_input('Entrez votre nom', st.session_state.user)
    if user:
        st.header('Historique')
        get_user_history(user)


## PAGE DES REQUETES (ACCUEIL) ##
if 'request' not in st.session_state:

    header = st.container()
    with header:
        col1, col2, col3 = st.columns([1,3,1])

        with col1:
            st.image("./static/rob_left.jpg")

        with col2:
            #génération du titre
            title_text = 'Mon Copain Robot'
            title_html = f'''
            <h1 style="
                text-align: center; 
                margin-top: 80px; 
                vertical-align: bottom;
            ">{title_text}</h1>'''

            st.write(title_html, unsafe_allow_html=True)

        with col3:
            st.image("./static/rob_right.jpg")

    request_frame = st.container()
    with request_frame:

        # génération de l’en-tête
        req_text = "Demandez à notre super robot de créer le programme de vos rêves !"
        req_html = f'''
            <p style="
                margin-top: 64px;
                margin-bottom: 32px; 
                ext-align: center; 
                ont-size: 22px;
            ">{req_text}</p>'''
        
        st.write(req_html, unsafe_allow_html=True)

        # text-area pour entrer la requête
        request = st.text_area('powered by openapi')

        # bouton de confirmation
        col1, col2, col3 = st.columns(3)
        with col2:
            if request : 
                st.button('AU TRAVAIL, ESCLAVE ROBOT', on_click=submit_request(request, st.session_state.user)) # activation du bouton submit
            else :  
                st.button('AU TRAVAIL, ESCLAVE ROBOT', disabled=True) # sinon le bouton est inactif

## PAGE DES REPONSES ##
elif st.session_state.request is not None :

    header = st.container()
    with header:
        col1, col2, col3 = st.columns([1,3,1])
        with col2:
            # génération de l’en-tête
            req_text = "Demandez à notre super robot de créer le programme de vos rêves !"
            req_html = f'''
            <p style="
                margin-top: 64px;
                margin-bottom: 32px; 
                ext-align: center; 
                ont-size: 22px;
            ">{req_text}</p>'''

    get_response(st.session_state.request)

    def reset_request():
        del(st.session_state.request)
    st.button('nouvelle demande', on_click=reset_request())



