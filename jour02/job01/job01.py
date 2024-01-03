# Définition de la classe Rectangle:
# La classe Rectangle est créée avec un constructeur __init__ qui prend deux paramètres (longueur et largeur).
# Dans ce constructeur, les attributs privés __longueur et __largeur sont initialisés avec les valeurs passées en paramètres.

class Rectangle:
    
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

# Assesseurs (Getters) :
# Deux méthodes, get_longueur et get_largeur, sont définies pour obtenir respectivement les valeurs de la longueur et de la largeur.
# Ces méthodes permettent d'accéder aux valeurs des attributs privés depuis l'extérieur de la classe.
    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height


# Mutateurs (Setters) :
# Deux méthodes, set_longueur et set_largeur, sont définies pour modifier respectivement les valeurs de la longueur et de la largeur.
# Ces méthodes permettent de changer les valeurs des attributs privés depuis l'extérieur de la classe.
    def set_width(self, new_width):
        self.__width = new_width

    def set_height(self, new_largeur):
        self.__height = new_largeur


# Création d'un objet mon_rectangle :
# Un objet mon_rectangle est créé en instanciant la classe Rectangle avec les valeurs initiales de longueur 10 et largeur 5.
mon_rectangle = Rectangle(10, 5)

# Affichage des valeurs initiales :
# Les valeurs initiales de longueur et de largeur de l'objet mon_rectangle sont affichées à l'aide des méthodes get_longueur et get_largeur.
print("Longueur initiale:", mon_rectangle.get_width())
print("Largeur initiale:", mon_rectangle.get_height())

# Modification des valeurs :
# Les méthodes set_longueur et set_largeur sont utilisées pour changer les valeurs de la longueur à 15 et de la largeur à 7.
mon_rectangle.set_width(15)
mon_rectangle.set_height(7)

# Affichage des valeurs modifiées :
# Les valeurs modifiées de longueur et de largeur de l'objet mon_rectangle,
# sont affichées à l'aide des méthodes get_longueur et get_largeur.
print("Nouvelle Longueur:", mon_rectangle.get_width())
print("Nouvelle largeur:", mon_rectangle.get_height())

