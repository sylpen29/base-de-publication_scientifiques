from pymongo import MongoClient
import pprint
#attention a bien utiliser vos paramètres de connexion
client = MongoClient("mongodb://root:pass12345@127.0.0.1:27017")

db = client["DBLP"]
publis = db["publis"]


# 1) nombre de documents de la collection publis
nbr_doc = db.publis.count_documents({})
pprint.pprint(nbr_doc)


# 2) liste de livres par titre
# livres = publis.find({"type":"Book"})
# print("liste de livres par titre")
# for livre in livres : 
#     pprint.pprint(livre['title'])


# 3) liste de livres depuis 2014
# livres_2014 = publis.find({"year" : {"$gte": 2014}})
# print("liste de livres depuis 2014 : ")
# for de_2014 in livres_2014 :
#     pprint.pprint(de_2014['title'])


# 4) liste des publications de Toru Ishida
# toru_ishida = publis.find({"authors" : "Toru Ishida"})
# print("liste des publications de Toru-ishida : ")
# for auteur in toru_ishida:
#     pprint.pprint(auteur['title'])


# 5) liste des auteurs distincts
# nom_auteur = publis.distinct("authors")
# print("liste des auteurs distincts : ")
# for nom in nom_auteur : 
#    pprint.pprint(nom_auteur)


# 6) publications de toru ishida par titre
# publi_ishida = publis.find(filter = {"authors" : "Toru Ishida"}, sort = [('title', 1)])
# print("publications par titre :")
# for titre in publi_ishida:
#     pprint.pprint(titre['title'])


# 7) nombre de puplications de Toru Ishida
# qui = {"authors" : "Toru Ishida"}
# total = publis.count_documents(qui)
# print("nombre de puplications de Toru Ishida :\n", total)


# 8) nombre de publications depuis 2011 et par type
# annee = {"$match" : {"year" : {"$gte":2011}}}
# type = {"$group": {"_id" :"$type", "count": { "$sum" :1}}}
# total = publis.aggregate([annee,type])
# for nb in total:
#     print("nombre de publications depuis 2011 et par type : \n", nb)

# 9) le nombre de publications par auteur par ordre croissant
# nbr_publi_auteur = publis.aggregate([{"$unwind" : "$authors"}, {"$sortByCount" : "$authors"} ])

# for ordre_croissant in nbr_publi_auteur:
#     print("le nombre de publications par auteur par ordre croissant : \n", ordre_croissant)


client.close()