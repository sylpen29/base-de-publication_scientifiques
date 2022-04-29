from pymongo import MongoClient
import pprint

user = "root"
mdp = "pass12345"

client = MongoClient(f"mongodb://{user}:{mdp}@localhost:27017")
db = client['test']
collection = db['professeurs']

rogue = collection.find_one({"nom":"Rogue"})

pprint.pprint(rogue)

collection.insert_one({"nom":"Dumbledore", "prenom":"Albus", "titre":"directeur"})

professeurs = collection.find()

for prof in professeurs :
    pprint.pprint(prof)

client.close()
