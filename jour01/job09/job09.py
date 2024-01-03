class Produit:
    # Constructeur __init__:Initialise les attributs nom, prixHT et TVA du produit lors de sa création.
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA / 100  # Convertir le pourcentage de TVA en fraction
        
# Méthode calculerPrixTTC:Calcule et retourne le prix TTC du produit.
    def calculerPrixTTC(self):
        return self.prixHT * (1 + self.TVA)
# Méthode afficher:Affiche toutes les informations du produit.
    def afficher(self):
        infos_produit = f"Produit : {self.nom}\nPrix HT : {self.prixHT} €\nTVA : {self.TVA * 100}%"
        print(infos_produit)
# Méthodes modifierNom et modifierPrixHT:Permettent de modifier le nom et le prix HT du produit respectivement.
    def modifierNom(self, nouveau_nom):
        self.nom = nouveau_nom

    def modifierPrixHT(self, nouveau_prixHT):
        self.prixHT = nouveau_prixHT
# Méthodes obtenirNom, obtenirPrixHT et obtenirTVA:Permettent de retourner chaque information du produit.
    def obtenirNom(self):
        return self.nom

    def obtenirPrixHT(self):
        return self.prixHT

    def obtenirTVA(self):
        return self.TVA

# Création de plusieurs produits et calcul de leurs TVA
produit1 = Produit("Réfrigérateur", 800, 20)
produit2 = Produit("Télévision", 500, 15)

# Afficher les informations initiales des produits
print("Informations initiales des produits :")
produit1.afficher()
produit2.afficher()

# Modifier le nom et le prix de chaque produit
produit1.modifierNom("Réfrigérateur")
produit2.modifierPrixHT(550)

# Afficher les nouvelles informations des produits
print("Nouvelles informations des produits :")
produit1.afficher()
produit2.afficher()

# Afficher les prix TTC des produits
print("Prix TTC des produits :")
print(f"{produit1.obtenirNom()} : {produit1.calculerPrixTTC()} €")
print(f"{produit2.obtenirNom()} : {produit2.calculerPrixTTC()} €")
