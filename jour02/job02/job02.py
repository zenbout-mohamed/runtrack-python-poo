class Livre:
# Le constructeur initialise un objet Livre avec un titre, un auteur et un nombre de pages.
    def __init__(self, titre, auteur, nb_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nb_pages = nb_pages

# Assesseurs (Getters :)
# Ces méthodes permettent d'obtenir les valeurs des attributs privés.
# Le double underscore (__) devant les noms d'attributs (__titre, __auteur, __nb_pages)
# indique qu'ils sont des attributs privés et ne devraient être accessibles que depuis l'intérieur de la classe.
# Les getters et setters sont utilisés pour accéder et modifier ces attributs de manière contrôlée.
    def get_titre(self):
        return self.__titre

    def get_auteur(self):
        return self.__auteur

    def get_nb_pages(self):
        return self.__nb_pages

# Mutateurs(Setters :)
# Ces méthodes permettent de modifier les valeurs des attributs privés.

    def set_titre(self, nouveau_titre):
        self.__titre = nouveau_titre

    def set_auteur(self, nouvel_auteur):
        self.__auteur = nouvel_auteur
# Pour set_nb_pages, il y a une vérification pour s'assurer que le nombre de pages est un entier positif.
    def set_nb_pages(self, nouveau_nb_pages):
        if isinstance(nouveau_nb_pages, int) and nouveau_nb_pages > 0:
            self.__nb_pages = nouveau_nb_pages
        else:
            print("Erreur : Le nombre de pages doit être un nombre entier positif.")

# Exemple d'utilisation
mon_livre = Livre("Titre du Livre", "Auteur du Livre", 200)

# Afficher les valeurs initiales
print("Titre:", mon_livre.get_titre())
print("Auteur:", mon_livre.get_auteur())
print("Nombre de pages:", mon_livre.get_nb_pages())

# Modifier les valeurs
mon_livre.set_titre("Nouveau Titre")
mon_livre.set_auteur("Nouvel Auteur")
mon_livre.set_nb_pages(260)

# Afficher les valeurs modifiées
print("Nouveau Titre:", mon_livre.get_titre())
print("Nouvel Auteur:", mon_livre.get_auteur())
print("Nouveau Nombre de pages:", mon_livre.get_nb_pages())

#---------------------- Tentative de modification avec un nombre de pages non valide-----------------------
mon_livre.set_nb_pages(-30)
