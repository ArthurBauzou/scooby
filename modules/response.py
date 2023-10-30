import streamlit as st

def show_code_edit(resp):

    if len(resp["code"]) == 0 : st.error('I’M SORRY DAVE, I’M AFRAID I CAN’T DO THAT')
    else :
        joined_code = "\n####\n".join(resp["code"])

        st.success(f'langage  :  {resp["lang"]}')
        st.text_area('editor', value=joined_code, label_visibility='hidden')