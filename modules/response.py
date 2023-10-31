import streamlit as st
import sys
from io import StringIO
from code_editor import code_editor

from .bdd import save_newcode, set_view

custom_btns = [{
    "name": "Run",
    "feather": "Play",
    "primary": True,
    "hasText": True,
    "showWithIcon": True,
    "commands": ["submit"],
    "style": {"bottom": "0.44rem", "right": "0.4rem"}
  }]

def show_code_edit(resp):

    if resp["code"] == '' :
        st.error('I’M SORRY DAVE, I’M AFRAID I CAN’T DO THAT')
    else :
        st.success(f'langage  :  {resp["lang"]}')

        ## gestion d’un code sauvegardé
        if resp['newcode'] != '' and resp['view'] == 'custom': 
            code_a_afficher = resp['newcode']
        else : 
            code_a_afficher = resp['code']

        ## EDITEUR
        editor = code_editor(code_a_afficher, resp['lang'], buttons=custom_btns, options={"wrap": True})
        # quand on execute
        if editor['type'] == "submit" and len(editor['id']) != 0:
            
            old_stdout = sys.stdout
            new_stdout = StringIO(newline='\n')
            sys.stdout = new_stdout

            try:
                # Exécutez le code
                exec(editor['text'])
                
                # Récupérez la sortie du code
                result = new_stdout.getvalue()
                col1, col2 = st.columns([1,15])
                with col1: st.text('>>>')
                with col2: st.text(result)
            except Exception as e:
                st.error(f"Une erreur s'est produite : {e}")
            finally:
                # Restaurer
                sys.stdout = old_stdout

        ## BOUTONS
        st.divider()
        def save_code():
            save_newcode(resp['_id'], editor['text'])
            set_view(resp['_id'], 'custom')

        col1, col2 = st.columns(2)
        with col1:
            if editor['type'] == "submit" : 
                st.button('Sauvegarder mes changements', on_click=save_code)
            else :
                st.button('Executez le code pour sauvegarder', disabled=True)
        with col2:
            if resp['newcode'] != '':
                if resp['view'] == 'custom':
                    if st.button('revenir au code de gpt') :
                        set_view(resp['_id'], 'gpt')
                        st.rerun()
                else :
                    if st.button('charger le code enregistré') :
                        set_view(resp['_id'], 'custom')
                        st.rerun()



        

