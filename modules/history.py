import streamlit as st

from .bdd import get_user_posts

def get_post(id):
    print('id sent: ', id)
    st.session_state.response = id
    st.session_state.page = 'response'

def get_user_history(user):

    documents = get_user_posts(user)

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
        st.button(doc["request"], key=i, on_click=get_post,args=[doc['_id']])
            # get_post(doc['_id'])
