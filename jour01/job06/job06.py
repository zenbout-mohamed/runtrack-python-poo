# Nous définissons la classe : 
class Animal:
    def __init__(self):
        # Le constructeur initialise les attributs age à zéro et prenom à une chaîne vide lors de la création d'une nouvelle instance
        # de la classe Animal.
        self.age = 0
        self.prenom = ""

    def vieillir(self):
        self.age += 1
        
    def nommer(self, nom):
        self.prenom = nom

# Instancier un objet Animal
mon_animal = Animal()

# Utiliser la méthode nommer pour donner un nom à l'animal
mon_animal.nommer("Luna")

# Afficher le nom de l'animal en console
print(f"Mon animal se nomme : {mon_animal.prenom}")

# Afficher l'âge initial en console
print(f"Âge initial de l'animal : {mon_animal.age}")

# Faire vieillir l'animal
mon_animal.vieillir()

# Affichage le nouvel âge en console
print(f"Nouvel âge de l'animal : {mon_animal.age}")
