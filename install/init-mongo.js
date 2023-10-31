db = db.getSiblingDB('admin');
db.auth("admin", "admin");

db = db.getSiblingDB('scoobyDB');

db.createUser({
 'user': "scooby",
 'pwd': "scooby",
 'roles': [{
     'role': 'dbOwner',
     'db': 'scoobyDB'}]});