# COPAIN ROBOT

Il est super sympa il fait des programmes pour toi contre des fractions de centimes.

### installer l’environnement
- faites un .venv et allez dedans. Si vous savez pas faire tant pis mourrez.
- `python venv ./.venv`
- `pip install -r requirements.txt`

### lancer le bouzin
- `streamlit run ./app.py`

### utiliser docker-compose pour lancer le projet

windows :
- `set MY_KEY=<openai_api_key>`
- `set MY_URL=mongodb://<url>:<port>`
- `docker-compose up -d --build`

linux :
- `docker-compose up -d --build`
- `-e MY_KEY=<openai_api_key>`
- `-e MY_URL=mongodb://<url>:<port>`


ouvrez un navigateur vers http://localhost:8502