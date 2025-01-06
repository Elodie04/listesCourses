Listes_Courses = [
    "pates","sopalin","chocolats","bonbons","cafe","os","croquettes"
]

def ajouter_articles(article):
    Listes_Courses.append(article)
    print(f"L'article {article} a été rajoutés",Listes_Courses)

def supprimer_articles(article):
    if article in Listes_Courses:
        Listes_Courses.remove(article)
        print(f"L'article {article} a été supprimés",Listes_Courses)
    else:
        print(f"L'article {article} n'a pas été trouvé dans la liste")

def afficher_articles():
    print(Listes_Courses)

def quitter():
    print("Au revoir !")

while True:
    print("Choix : 1 - Ajouter articles || 2 - Supprimer articles || 3 - Afficher articles || 4 - Quitter \n")
    choix = (input("Veuillez saisir votre choix =  \n "))
    if choix == "1":
        article = input("Quel est l'article à ajouter = \n ")
        ajouter_articles(article)
    if choix == "2":
        article = input("Quel est l'article à supprimer = \n")
        supprimer_articles(article)
    if choix == "3":
        afficher_articles()
    if choix == "4":
        quitter()

    Listes_Courses.sort()



