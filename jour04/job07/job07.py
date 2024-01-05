import random

class Carte:
# Cette classe représente une carte dans le jeu de Blackjack.
# Elle a deux attributs : valeur (par exemple, 'As', 'Vallée', '4') et couleur (par exemple, 'Cœur', 'Carreau', 'Trèfle', 'Pique').

    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur
# La méthode __str__ permet d'afficher la carte sous forme de chaîne.
    def __str__(self):
        return f"{self.valeur} de {self.couleur}"
# Cette classe représente le jeu de Blackjack.
class Jeu:
    
    def __init__(self):
        self.paquet = self.initialiser_paquet()
# L'initialisation crée un paquet de cartes mélangé pour le jeu.
    def initialiser_paquet(self):
        valeurs = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi', 'As']
        couleurs = ['Cœur', 'Carreau', 'Trèfle', 'Pique']
        paquet = [Carte(valeur, couleur) for valeur in valeurs for couleur in couleurs]
        random.shuffle(paquet)
        return paquet
# La méthode calculer_total prend une main de cartes et calcule le total des valeurs en tenant compte des règles du Blackjack
# (As peut valoir 1 ou 11).
    def calculer_total(self, main):
        total = 0
        as_count = 0




# La première partie (la boucle for) parcourt chaque carte dans la main du joueur.
        for carte in main:
            # Si la carte est une figure (Valet, Dame, Roi), 10 points sont ajoutés à la valeur totale de la main.
            if carte.valeur in ['Valet', 'Dame', 'Roi']:
                total += 10
            # Si la carte est un As, la variable as_count est incrémentée de 1, et 11 points sont ajoutés à la valeur totale de la main.
            elif carte.valeur == 'As':
                as_count += 1
                total += 11
            else:
                total += int(carte.valeur)

        while total > 21 and as_count:
            total -= 10
            as_count -= 1

        return total
# La méthode distribuer_cartes donne deux cartes à chaque joueur (le joueur et le croupier) au début du jeu.
    def distribuer_cartes(self):
        return [self.paquet.pop(), self.paquet.pop()]
# La méthode joueur_gagne compare les totaux du joueur et du croupier pour déterminer le gagnant.
    def joueur_gagne(self, main_joueur, main_croupier):
        total_joueur = self.calculer_total(main_joueur)
        total_croupier = self.calculer_total(main_croupier)

        return (total_joueur <= 21 and (total_joueur > total_croupier or total_croupier > 21))
# La méthode jouer représente le déroulement d'une partie complète de Blackjack.
    def jouer(self):
        print("Nouvelle partie de Blackjack!\n")

        main_joueur = self.distribuer_cartes()
        main_croupier = self.distribuer_cartes()

        while True:
            print(f"Main du joueur: {', '.join(map(str, main_joueur))} (Total: {self.calculer_total(main_joueur)})")
            print(f"Cartes visible de L'IA: {main_croupier[0]}\n")

            choix = input("Voulez-vous piocher ? (P) ou passer votre tour ?(Q) ").lower()

            if choix == 'p':
                main_joueur.append(self.paquet.pop())
                if self.calculer_total(main_joueur) > 21:
                    print(f"\nMain du joueur: {', '.join(map(str, main_joueur))} (Total: {self.calculer_total(main_joueur)})")
                    print("Vous avez dépassé 21. Vous avez perdu!")
                    return
            elif choix == 'q':
                break

        while self.calculer_total(main_croupier) < 17:
            main_croupier.append(self.paquet.pop())

        print("\nRésultats:")
        print(f"Main du joueur: {', '.join(map(str, main_joueur))} (Total: {self.calculer_total(main_joueur)})")
        print(f"Cartes en jeu de l'IA: {', '.join(map(str, main_croupier))} (Total: {self.calculer_total(main_croupier)})")

        if self.joueur_gagne(main_joueur, main_croupier):
            print("Vous avez remporté la victoire !")
        else:
            print("L'IA a remporté la victoire !")

# Instanciation de la classe Jeu et lancement de la partie
jeu = Jeu()
jeu.jouer()
