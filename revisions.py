from pymongo import MongoClient
import pprint
#attention a bien utiliser vos paramètres de connexion
client = MongoClient("mongodb://root:pass12345@127.0.0.1:27017")
db = client["food"]
fruits = db["fruits"]
documents = fruits.find({})
for document_lu in documents:
    pprint.pprint(document_lu)
mangue = fruits.find_one({"name":"mango"})
pprint.pprint(mangue)