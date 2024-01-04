class Ville:
    # La classe Ville a un constructeur __init__ 
    # qui initialise les attributs privés _nom et _nombre_habitants.
    def __init__(self, nom, nombre_habitants):
        self._nom = nom
        self._nombre_habitants = nombre_habitants
# Elle a une méthode get_population qui renvoie le nombre d'habitants.
    def get_population(self):
        return self._nombre_habitants
# Elle a une méthode augmenter_population qui permet d'augmenter la population de la ville d'un certain nombre.
    def augmenter_population(self, nombre):
        self._nombre_habitants += nombre

# La classe Personne a un constructeur __init__ qui initialise les attributs privés _nom, _age et _ville.
class Personne:
    def __init__(self, nom, age, ville):
        self._nom = nom
        self._age = age
        self._ville = ville
        self._ville.augmenter_population(1) 
# Elle a une méthode ajouter_population qui appelle la méthode augmenter_population de la ville de la personne pour ajouter 1 à la population.
    def ajouter_population(self):
        self._ville.augmenter_population(1)


# Créer un objet Ville avec comme arguments “Paris” et 1000000.
paris = Ville("Paris", 1000000)
# Afficher en console le nombre d’habitants de la ville de Paris.
print(f"Population de la ville de Paris : {paris.get_population()} habitants")

# Créer un autre objet Ville avec comme arguments “Marseille” et 861635.
marseille = Ville("Marseille", 861635)
# Afficher en console le nombre d’habitants de la ville de Marseille.
print(f"Population de la ville de Marseille : {marseille.get_population()} habitants")

# Créer les objets suivants :
# - John, 45 ans, habitant à Paris
john = Personne("John", 45, paris)
# - Myrtille, 4 ans, habitant à Paris.
myrtille = Personne("Myrtille", 4, paris)
# - Chloé, 18 ans, habitant à Marseille.
chloe = Personne("Chloé", 18, marseille)

# Afficher le nombre d’habitants de Paris et de Marseille après l’arrivée de ces nouvelles personnes.
print(f"Mise à jour de la population de la ville de Paris : {paris.get_population()} habitants")
print(f"Mise à jour de la population de la ville de Marseille : {marseille.get_population()} habitants")
