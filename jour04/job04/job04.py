# La classe Forme a une méthode aire qui renvoie toujours 0 par défaut.
# Cela peut être considéré comme une classe de base générique pour différentes formes, où l'aire par défaut est 0.
class Forme:
    def aire(self):
        return 0
    
# La classe Rectangle hérite de la classe Forme, ce qui signifie qu'elle hérite de la méthode aire.
class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
# La méthode aire est surchargée pour calculer et renvoyer l'aire réelle du rectangle en multipliant largeur par hauteur.
    def aire(self):
        return self.largeur * self.hauteur

# Un objet rectangle1 de la classe Rectangle est créé avec une largeur de 5 et une hauteur de 3.
rectangle1 = Rectangle(largeur=5, hauteur=3)

# La méthode aire de rectangle1 est ensuite appelée et le résultat est affiché dans la console.
print("Aire du rectangle:", rectangle1.aire())
