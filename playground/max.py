#import openai
from pymongo import MongoClient
import sys
import os
playground_dir = os.path.dirname(os.path.abspath(__file__))
config_dir = os.path.join(playground_dir, "../config")
sys.path.append(config_dir)
from key import API_KEY2, MONGODB_URL

client = MongoClient(MONGODB_URL)
db = client.scoobyDB
my_collection = db.pierre



# document JSON test
data_to_insert = {
    'user_input': "ceci est un tes3",
    'conclusion': "ceci est une réponse de test",
    'utilisateur': "pierre"
}

# Insérer le document
insert_result = my_collection.insert_one(data_to_insert)

# Vérifier
if insert_result.inserted_id:
    print(f'Données insérées avec succès. ID du document inséré : {insert_result.inserted_id}')
else:
    print('Échec insertion des données')
          
client.close()