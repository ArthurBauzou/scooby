def parsecode(raw:str) -> (str, str):
    languages = [
        'python', 
        'javascript',
        'c',
        'c++',
        'c#',
        'php',
        'java',
        'sql'
    ]

    comments = {
        'python': '####',
        'javascript': '////',
        'sql': '----'
    }

    raw_list = raw.split('```')

    language = ''
    lang_found = False
    code = []
    joined_code = ''
    for i, text in enumerate(raw_list):
        
        if i%2 == 0 : continue  # Recupérer uniquement les blocs de code (donc les elements impairs)

        words = text.split()

        if words[0] not in languages: continue  # vérifier que le langage est connu
        if lang_found and words[0] != language : continue # verifier que c’est bien le même langage

        lang_found = True
        language = words[0]
        code.append(text[len(language)+1:])

        joined_code = f"\n{comments[language]}\n\n".join(code)

    return language, joined_code