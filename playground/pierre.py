import streamlit as st
import openai

# Définissez votre clé API OpenAI
openai.api_key = "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"

# Fonction pour obtenir la conclusion en utilisant l'API ChatGPT
def get_conclusion(user_prompt):
    messages = [{"role": "user", "content": user_prompt}]
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    return completion['choices'][0]['message']['content']

# Page principale de l'application Streamlit
st.title("Générateur de Conclusions")

# Formulaire pour que l'utilisateur entre son texte
user_input = st.text_input("Entrez votre texte :")

# Bouton pour générer la conclusion
if st.button("Générer la Conclusion"):
    if user_input:
        conclusion = get_conclusion(user_input)
        st.subheader("Conclusion générée :")
        st.write(conclusion)
    else:
        st.warning("Veuillez entrer du texte pour générer une conclusion.")
