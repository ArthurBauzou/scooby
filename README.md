# COPAIN ROBOT

Il est super sympa il fait des programmes pour toi contre des fractions de centimes.

### utiliser docker-compose pour lancer le projet

windows :
- `set MY_KEY=<openai_api_key>`
- `set MY_URL=mongodb://<url>:<port>`
- `docker-compose up -d --build`

la set MY_URL= par defaut pour windows est la suivante :
- `set MY_URL=mongodb://scooby:scooby@scoobymongodb:27017/scoobyDB?tls=true^&tlsCertificateKeyFile=/etc/ssl/certs/ca.pem^&tlsAllowInvalidCertificates=true`


linux :
- `docker-compose up -d --build`
- `-e MY_KEY=<openai_api_key>`
- `-e MY_URL=mongodb://<url>:<port>`

la -e MY_URL= par defaut pour linux est la suivante :
- `-e MY_URL=mongodb://scooby:scooby@scoobymongodb:27017/scoobyDB?tls=true&tlsCertificateKeyFile=/etc/ssl/certs/ca.pem&tlsAllowInvalidCertificates=true`


ouvrez un navigateur vers http://localhost:8502


si vous souhaitez utiliser un certificat autre que celui par default, veuillez écraser les fichiers ca.pem et mongodb.pem par les vôtres.

si vous souhaitez changer le port externe de l'application scoobyapp veuillez éditer la port externe par defaut 8502 dans le fichier docker-compose.yml :
-    ports:
-      - "votreport:8501"

si vous souhaitez changer le port externe de la base mongodb, veuillez éditer le port externe par defaut 27017 dans le fichier docker-compose.yml (notez qu'il vous faudra
aussi le changer dans votre commande de variable d'environment MY_URL accordément avant de lancer docker-compose)
-    ports:
-      - "votreport:27017"

si vous souhaitez changer l'utilisateur root de votre mongoDB il vous faudra le changer dans le docker-compose par les vôtres :
-      - MONGO_INITDB_ROOT_USERNAME=votreloginroot
-      - MONGO_INITDB_ROOT_PASSWORD=votremotdepasseroot

il vous faudra aussi le changer dans le fichier install\init-mongo.js :
-      db.auth("votreloginroot", "votremotdepasseroot");

si vous souhaitez changer l'utilisateur par defaut de la basse scoobyDB, il vous faudra le changer dans le fichier install\init-mongo.js (notez qu'il vous faudra
aussi le changer dans votre commande de variable d'environment MY_URL accordément avant de lancer docker-compose)
 'user': "votrelogin",
 'pwd': "votremotdepasse",