import streamlit as st
import sys
from io import StringIO
from code_editor import code_editor

from .bdd import save_newcode

custom_btns = [{
    "name": "Copy",
    "feather": "Copy",
    "hasText": True,
    "alwaysOn": True,
    "commands": ["copyAll", 
                 ["infoMessage", 
                  {
                   "text":"Copied to clipboard!",
                   "timeout": 2500, 
                   "classToggle": "show"
                  }
                 ]
                ],
    "style": {"top": "0rem", "right": "0.4rem"}
  },{
    "name": "Run",
    "feather": "Play",
    "primary": True,
    "hasText": True,
    "showWithIcon": True,
    "commands": ["submit"],
    "style": {"bottom": "0.44rem", "right": "0.4rem"}
  }]

def show_code_edit(resp):

    if len(resp["code"]) == 0 :
        st.error('I’M SORRY DAVE, I’M AFRAID I CAN’T DO THAT')
    else :
        st.success(f'langage  :  {resp["lang"]}')
        ## EDITEUR


        if resp['newcode'] != '' : 
            code_a_afficher = resp['newcode']
            print('ya un newcode')
        else : 
            code_a_afficher = resp['code']

        edit_window = st.container()
        with edit_window:
            editor = code_editor(code_a_afficher, lang=resp['lang'], buttons=custom_btns)
            if editor['type'] == "submit" and len(editor['id']) != 0:

                    old_stdout = sys.stdout
                    new_stdout = StringIO()
                    sys.stdout = new_stdout

                    try:
                        # Exécutez le code
                        exec(editor['text'])
                        
                        # Récupérez la sortie du code
                        result = new_stdout.getvalue()
                        st.text(f'>>> {result}')
                    except Exception as e:
                        st.error(f"Une erreur s'est produite : {e}")
                    finally:
                        # Restaurer
                        sys.stdout = old_stdout

        ## BOUTONS
        col1, col2 = st.columns(2)
        with col1:
            if editor['type'] == "submit" : 
                if st.button('Sauvegarder mes changements') :
                    print(f'saved {editor["text"]} on {resp["_id"]}')
                    save_newcode(resp['_id'], editor['text'])
            else : st.write(':red[executez pour sauvegarder]')
        with col2:
            if st.button('reset', disabled=True) :
                print('reset code')
                edit_window.empty()


