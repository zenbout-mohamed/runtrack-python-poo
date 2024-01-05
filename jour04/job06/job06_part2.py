class Vehicule:
    def __init__(self, marque, modele, annee, prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix

    def informationsVehicule(self):
        print(f"Marque: {self.marque}\nModèle: {self.modele}\nAnnée: {self.annee}\nPrix: {self.prix}")

    def demarrer(self):
        print("Attention, 3, 2, 1 Partez !")


class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)
        self.portes = 4

    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de portes: {self.portes}")

    def demarrer(self):
        print("Attention, je m'apprete à démarrer. Vroum vroum!")


class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)
        self.roues = 2

    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de roues: {self.roues}")


# Instanciation d'un objet Moto
moto1 = Moto(marque="Yamaha", modele="1200 Vmax", annee=1987, prix=4500)

# Appel de la méthode informationsVehicule pour afficher les informations de la moto
moto1.informationsVehicule()

# Appel de la méthode demarrer pour la moto
moto1.demarrer()

# Instanciation d'un objet Voiture
voiture1 = Voiture(marque="Mercedes", modele="Classe A", annee=2020, prix=18500)

# Appel de la méthode demarrer pour la voiture
voiture1.demarrer()

