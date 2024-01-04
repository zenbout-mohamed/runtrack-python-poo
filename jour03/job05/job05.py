import random

class Personnage:
    # __init__: Le constructeur initialise le nom et les points de vie du personnage.
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie
    # attaquer: La méthode simule une attaque avec des dégâts aléatoires.
    def attaquer(self, adversaire):
        degats = random.randint(5, 15)
        print(f"{self.nom} attaque {adversaire.nom} et lui inflige {degats} points de dégâts.")
        adversaire.vie -= degats
        
class Jeu:
    # __init__: Le constructeur initialise le niveau à 1.
    def __init__(self):
        self.niveau = 1
# choisirNiveau: Demande au joueur de choisir le niveau de difficulté.
    def choisirNiveau(self):
        self.niveau = int(input("Choisissez le niveau de difficulté (1, 2, 3) : "))
# lancerJeu: Lance le jeu en instanciant deux objets Personnage (joueur et ennemi),2
# avec des points de vie différents selon le niveau.

    def lancerJeu(self):
        print(f"Vous avez choisi le niveau de difficulté : {self.niveau}. Que le combat commence!")

        joueur = Personnage("Joueur", 100 * self.niveau)
        ennemi = Personnage("Ennemi", 50 * self.niveau)
# La boucle de jeu continue jusqu'à ce que l'un des personnages ait une vie nulle.
        while joueur.vie > 0 and ennemi.vie > 0:
            joueur.attaquer(ennemi)
            if ennemi.vie <= 0:
                print(f"{ennemi.nom} a été vaincu!")
                break

            ennemi.attaquer(joueur)
            if joueur.vie <= 0:
                print(f"{joueur.nom} a été vaincu. Vous avez perdu.")
                break

            print(f"{joueur.nom} - Points de vie restants: {joueur.vie}")
            print(f"{ennemi.nom} - Points de vie restants: {ennemi.vie}\n")

        if joueur.vie > 0:
            print("Félicitations! Vous avez remporté la victoire!.")
        elif ennemi.vie > 0:
            print("Game Over! Vous avez été vaincu.")

# Création d'une instance de la classe Jeu.
jeu = Jeu()

# Choix du niveau par le joueur.
jeu.choisirNiveau()

# Lancement du jeu.
jeu.lancerJeu()
