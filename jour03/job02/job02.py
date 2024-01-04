class CompteBancaire:
    def __init__(self, numero_compte, nom, prenom, solde, decouvert=False):
        self._numero_compte = numero_compte #_numero_compte: Numéro de compte (privé)
        self._nom = nom #_nom: Nom du titulaire du compte (privé)
        self._prenom = prenom #_prenom: Prénom du titulaire du compte (privé)
        self._solde = solde #_solde: Solde du compte (privé)
        self._decouvert = decouvert #_decouvert: Attribut booléen indiquant si
        # le compte autorise le découvert (par défaut, False)
        
#  ------------------------------------------------------------------------------       
# afficher: Affiche les détails du compte.
    def afficher(self):
        print(f"Compte n°{self._numero_compte} - {self._prenom} {self._nom}")
# afficherSolde: Affiche le solde du compte.
    def afficherSolde(self):
        print(f"Solde du compte : {self._solde} euros")
# versement: Ajoute un montant au solde du compte.
    def versement(self, montant):
        self._solde += montant
        print(f"Versement de {montant} euros effectué. Nouveau solde : {self._solde} euros")
# retrait: Retire un montant du solde du compte (avec gestion du découvert).
    def retrait(self, montant):
        if not self._decouvert and montant > self._solde:
            print("Opération impossible : solde insuffisant.")
        else:
            self._solde -= montant
            print(f"Retrait de {montant} euros effectué. Nouveau solde : {self._solde} euros")
# agios: Applique des agios au solde du compte si celui-ci est négatif.
    def agios(self, taux_agios):
        if self._solde < 0:
            agios = abs(self._solde) * taux_agios
            self._solde -= agios
            print(f"Des agios de {agios} euros ont été appliqués. Nouveau solde : {self._solde} euros")
# virement: Effectue un virement vers un autre compte.
    def virement(self, compte_destinataire, montant):
        if self._solde >= montant:
            self._solde -= montant
            compte_destinataire.versement(montant)
            print(f"Virement de {montant} euros effectué avec succès.")
        else:
            print("Virement impossible : solde insuffisant.")

# Deux comptes (compte1 et compte2) sont créés avec des valeurs initiales.
# Les méthodes de la classe sont appelées pour effectuer diverses opérations.
# Création d'une première instance de la classe CompteBancaire
compte1 = CompteBancaire(numero_compte="123456", nom="Doe", prenom="John", solde=1000)
# Affichage des détails du compte.
compte1.afficher()
# Affichage du solde du compte.
compte1.afficherSolde()



# Versement de 500 euros.
compte1.versement(500)

# Retrait du compte1
# Retrait de 200 euros.
compte1.retrait(200)

# Création d'une deuxième instance de la classe CompteBancaire à découvert
compte2 = CompteBancaire(numero_compte="789012", nom="Fever", prenom="Tatiana", solde=-500, decouvert=True)
compte2.afficher()
compte2.afficherSolde()

# Virement du compte1 vers le compte2
# Virement de 300 euros vers le deuxième compte (compte2).
compte1.virement(compte_destinataire=compte2, montant=300)

# Application d'agios sur le compte2
compte2.agios(taux_agios=0.05)
