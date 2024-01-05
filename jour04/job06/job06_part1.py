class Vehicule:
    def __init__(self, marque, modele, annee, prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix

    def informationsVehicule(self):
        print(f"Marque: {self.marque}\nModèle: {self.modele}\nAnnée: {self.annee}\nPrix: {self.prix}")


class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)
        self.portes = 4

    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de portes: {self.portes}")


# Instanciation d'un objet Voiture
voiture1 = Voiture(marque="Mercedes", modele="Classe A", annee=2020, prix=18500)

# Appel de la méthode informationsVehicule pour afficher les informations de la voiture
voiture1.informationsVehicule()
