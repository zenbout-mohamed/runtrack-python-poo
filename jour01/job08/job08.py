# Importation de la bibliothèque math
import math

class Cercle:
# Constructeur __init__:Initialise le rayon du cercle lors de sa création.
    def __init__(self, rayon):
        self.rayon = rayon

# Méthode changerRayon: Permet de modifier le rayon du cercle.
    def changerRayon(self, new_rayon):
        self.rayon = new_rayon
# Méthode afficherInfos:Affiche les informations du cercle, en l'occurrence, le rayon
    def afficherInfos(self):
        print(f"Rayon du cercle : {self.rayon}")
# Méthodes circonférence, aire et diametre:Ces méthodes calculent respectivement la circonférence, l'aire et le diamètre du cercle.
    def volume(self):
        return 2 * math.pi * self.rayon

    def aire(self):
        return math.pi * self.rayon**2

    def diametre(self):
        return 2 * self.rayon

# Nous créons 2 variables cercles avec des rayons 4 et 7
cercle1 = Cercle(4)
cercle2 = Cercle(7)

# Afficher les informations, circonférence, diamètre et aire pour chaque cercle
for cercle in [cercle1, cercle2]:
    print(f"Cercle avec un rayon de {cercle.rayon}:")
    cercle.afficherInfos()
    print(f"Volume : {cercle.volume()}")
    print(f"Diamètre : {cercle.diametre()}")
    print(f"Aire : {cercle.aire()}")
