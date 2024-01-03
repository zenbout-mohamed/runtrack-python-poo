class Livre:
# Le constructeur initialise les attributs de la classe tels que le titre (__titre),
# l'auteur (__auteur), le nombre de pages (__nb_pages), et l'indicateur de
# disponibilité (__disponible).
# L'indicateur de disponibilité est initialisé à True par défaut.
    def __init__(self, titre, auteur, nb_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nb_pages = nb_pages
        self.__disponible = True

# Des méthodes get_ sont fournies pour obtenir les valeurs des attributs.

    def get_titre(self):
        return self.__titre

    def get_auteur(self):
        return self.__auteur

    def get_nb_pages(self):
        return self.__nb_pages

    def get_disponible(self):
        return self.__disponible

# Des méthodes set_ sont fournies pour modifier les valeurs des attributs sous certaines
# conditions. Par exemple, la méthode set_nb_pages vérifie que le nouveau nombre de
# pages est un entier positif.
    def set_titre(self, nouveau_titre):
        self.__titre = nouveau_titre

    def set_auteur(self, nouvel_auteur):
        self.__auteur = nouvel_auteur

    def set_nb_pages(self, nouveau_nb_pages):
        if isinstance(nouveau_nb_pages, int) and nouveau_nb_pages > 0:
            self.__nb_pages = nouveau_nb_pages
        else:
            print("Erreur : Le nombre de pages doit être un nombre entier positif.")

# Méthode verification:
# Cette méthode renvoie l'indicateur de disponibilité du livre.
    def verification(self):
        return self.__disponible

# Méthodes emprunter et rendre:
# La méthode emprunter modifie l'indicateur de disponibilité à False si le livre est disponible, sinon, elle affiche un message d'indisponibilité.
# La méthode rendre modifie l'indicateur de disponibilité à True si le livre n'est pas disponible, sinon, elle affiche un message indiquant que le livre n'a pas été emprunté.
    def emprunter(self):
        if self.verification():
            self.__disponible = False
            print("Le livre a été emprunté avec succès.")
        else:
            print("Le livre n'est pas disponible pour l'emprunt.")
# Les attributs de la classe sont définis comme privés en utilisant le double underscore
# (__) comme préfixe, ce qui signifie qu'ils ne devraient normalement pas être accédés
# directement depuis l'extérieur de la classe. Les méthodes d'assesseurs et de mutateurs
# sont fournies pour permettre un accès contrôlé à ces attributs.
    # Méthode pour rendre le livre
    def rendre(self):
        if not self.verification():
            self.__disponible = True
            print("Livre rendu avec succès.")
        else:
            print("Livre non emprunté précédemment.")

# Exemple d'utilisation
mon_livre = Livre("Titre du Livre", "Auteur du Livre", 200)

# Vérifier si le livre est disponible
print("Le livre est disponible:", mon_livre.verification())

# Emprunter le livre
mon_livre.emprunter()

# Essayer d'emprunter à nouveau (devrait afficher un message d'indisponibilité)
mon_livre.emprunter()

# Rendre le livre
mon_livre.rendre()

# Essayer de rendre à nouveau (devrait afficher un message de non-emprunt)
mon_livre.rendre()
