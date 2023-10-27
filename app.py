import streamlit as st

from modules.history import get_user_history
from modules.response import get_response

st.set_page_config(
        page_title="AWESOME O",
        initial_sidebar_state="collapsed"
)

login = st.sidebar.container()
with login:
    st.header('Historique')
    user = st.text_input('login', "Anonyme")
    if user:
        get_user_history(user)

if 'request' not in st.session_state:

    header = st.container()
    with header:
        col1, col2, col3 = st.columns([1,3,1])

        with col1:
            st.image("./static/rob_left.jpg")
        with col2:
            title = '<h1 style="text-align: center; margin-top: 80px; vertical-align: bottom">Mon Copain Robot</h1>'
            st.write(title, unsafe_allow_html=True)
        with col3:
            st.image("./static/rob_right.jpg")

    request_frame = st.container()
    with request_frame:
        req_text = '<p style="margin-top: 64px; margin-bottom: 32px; text-align: center; font-size: 22px">demandez à notre super robot de créer le programme de vos rêves !</p>'
        st.write(req_text, unsafe_allow_html=True)
        request = st.text_area('powered by openapi')
        col1, col2, col3 = st.columns(3)
        with col2:
            def submit_request(value):
                if request : st.session_state.request = value
            if request : st.button('AU TRAVAIL, ESCLAVE ROBOT', on_click=submit_request(request))
            else :  st.button('AU TRAVAIL, ESCLAVE ROBOT', disabled=True)

elif st.session_state.request is not None :

    header = st.container()
    with header:
        request = st.session_state.request
        col1, col2, col3 = st.columns([1,3,1])

        with col2:
            title = '<h1 style="text-align: center; vertical-align: bottom">Mon Copain Robot</h1>'
            st.write(title, unsafe_allow_html=True)

    get_response(request)

    def reset_request():
        del(st.session_state.request)
    st.button('nouvelle demande', on_click=reset_request())



