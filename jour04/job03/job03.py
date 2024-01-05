class Rectangle:
    # Le constructeur de la classe Rectangle initialise les attributs longueur et largeur avec les valeurs fournies lors
    # de la création d'une instance de la classe.
    def __init__(self, longueur, largeur):
        self._longueur = longueur
        self._largeur = largeur

    def longueur(self):
        return self._longueur

    def longueur(self, value):
        self._longueur = value

    def largeur(self):
        return self._largeur

    def largeur(self, value):
        self._largeur = value
# perimetre et surface: Ces méthodes calculent le périmètre et la surface du rectangle
# en utilisant les valeurs des attributs longueur et largeur.
    def perimetre(self):
        return 2 * (self._longueur + self._largeur)

    def surface(self):
        return self._longueur * self._largeur

# La classe Parallelepipede hérite de la classe Rectangle,
# ce qui signifie qu'elle a tous les attributs et méthodes de la classe Rectangle.
class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self._hauteur = hauteur
# Propriété et Mutateur pour hauteur: Ces méthodes permettent d'accéder à l'attribut hauteur de manière contrôlée.
    def hauteur(self):
        return self._hauteur

    def hauteur(self, value):
        self._hauteur = value
# Cette méthode calcule le volume du parallélépipède en utilisant les valeurs des attributs longueur, largeur et hauteur.
    def volume(self):
        return self._longueur * self._largeur * self._hauteur


# On crée une instance de la classe Rectangle avec une longueur de 5 et une largeur de 3,
# puis on affiche la surface et le périmètre du rectangle.
rectangle1 = Rectangle(longueur=5, largeur=3)

# Affichage de la surface et du périmètre du rectangle
print("Rectangle - Surface:", rectangle1.surface())
print("Rectangle - Périmètre:", rectangle1.perimetre())

# Modification des dimensions du rectangle à l'aide des mutateurs
rectangle1.longueur = 7
rectangle1.largeur = 4

# Affichage des nouvelles dimensions, surface et périmètre du rectangle
print("Nouvelles dimensions du rectangle:")
print("Longueur:", rectangle1.longueur)
print("Largeur:", rectangle1.largeur)
print("Rectangle - Surface:", rectangle1.surface())
print("Rectangle - Périmètre:", rectangle1.perimetre())

# On crée une instance de la classe Parallelepipede avec une longueur de 3,
# une largeur de 2 et une hauteur de 4, puis on affiche le volume du parallélépipède.
parallelepipede1 = Parallelepipede(longueur=3, largeur=2, hauteur=4)

# Affichage de la surface, du périmètre et du volume du parallélépipède
print("\nParallélépipède - Volume:", parallelepipede1.volume())
