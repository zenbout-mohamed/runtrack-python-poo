class Commande:
    # Initialise les attributs de la commande : numéro de commande,
    # plats commandés (représentés sous forme de dictionnaire)
    # et statut de la commande.
    def __init__(self, numero_commande):
        self._numero_commande = numero_commande
        self._plats_commandes = {}  # Utilisation d'un dictionnaire pour représenter les plats
        self._statut_commande = "en cours"
# Ajoute un plat à la commande avec son nom, son prix et son statut initial.
    def ajouter_plat(self, nom_plat, prix_plat):
        if nom_plat not in self._plats_commandes:
            self._plats_commandes[nom_plat] = {'prix': prix_plat, 'statut': 'en cours'}
            print(f"Plat '{nom_plat}' ajouté à la commande.")
# Annule la commande en mettant à jour le statut.
    def annuler_commande(self):
        self._statut_commande = "annulée"
        print("La commande a été annulée.")
# Méthode privé : Calcule le total de la commande en prenant en compte
# uniquement les plats dont le statut est "en cours".
    def _calculer_total(self):
        total = sum(plat['prix'] for plat in self._plats_commandes.values() if plat['statut'] == 'en cours')
        return total
# Affiche les détails de la commande, y compris chaque plat avec son prix et son statut,
# ainsi que le total à payer.
    def afficher_commande(self):
        print(f"Commande #{self._numero_commande}")
        for plat, details in self._plats_commandes.items():
            print(f"{plat}: {details['prix']} € ({details['statut']})")
        total = self._calculer_total()
        print(f"Total à payer : {total} € (TVA incluse)")
# Calcule la TVA sur le total de la commande avec un taux de TVA par défaut de 0.2 (20%).
    def calculer_tva(self, taux_tva=0.2):
        total = self._calculer_total()
        tva = total * taux_tva
        return tva

# Exemple d'utilisation de la classe Commande
commande1 = Commande(101)

# Crée une commande, ajoute des plats, affiche la commande,
# calcule la TVA, annule la commande, et réaffiche la commande annulée.
commande1.ajouter_plat("Pizza", 12.5)
commande1.ajouter_plat("Salade", 7.2)
commande1.ajouter_plat("Pâtes", 9.0)

# Affichage de la commande
commande1.afficher_commande()

# Calcul de la TVA
tva_commande1 = commande1.calculer_tva()
print(f"TVA à payer : {tva_commande1} €")

# Annulation de la commande
commande1.annuler_commande()

# Affichage de la commande annulée
commande1.afficher_commande()
