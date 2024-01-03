class Personnage:
    # Constructeur __init__:
    # x et y représentent les coordonnées initiales du personnage.
    # plateau représente la matrice du plateau de jeu.
    def __init__(self, x, y, plateau):
        self.x = x
        self.y = y
        self.plateau = plateau

    def gauche(self):
        if self.x > 0:
            self.x -= 1

    def droite(self):
        if self.x < len(self.plateau[0]) - 1:
            self.x += 1

    def haut(self):
        if self.y > 0:
            self.y -= 1

    def bas(self):
        if self.y < len(self.plateau) - 1:
            self.y += 1

    def position(self):
        return (self.x, self.y)

#  la classe Personnage avec un plateau de jeu 5x5
plateau_jeu = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

personnage = Personnage(2, 3, plateau_jeu)

# Afficher la position initiale du personnage
print(f"Position initiale : {personnage.position()}")

# Déplacer le personnage vers la droite et vers le bas
personnage.droite()
personnage.bas()

# Afficher la nouvelle position du personnage
print(f"Nouvelle position : {personnage.position()}")

