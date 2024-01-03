class Voiture:
    # Le constructeur initialise les attributs de la classe lorsqu'un objet Voiture
    # est créé. Les paramètres marque, modele, annee, kilometrage,
    # et en_marche sont utilisés pour initialiser les attributs correspondants.
    # L'attribut _reservoir est ajouté avec une valeur par défaut de 50.
    def __init__(self, marque, modele, annee, kilometrage, en_marche=False):
        self._marque = marque
        self._modele = modele
        self._annee = annee
        self._kilometrage = kilometrage
        self._en_marche = en_marche
        self._reservoir = 50  # Ajout de l'attribut reservoir avec une valeur par défaut

    # Getters et Setters pour chaque attribut :
    # Pour chaque attribut, il y a des paires de mutateurs (setters) et
    # assesseurs (getters) qui permettent de modifier et d'obtenir les
    # valeurs respectives des attributs.
    # Par exemple, set_marque, get_marque, set_modele, get_modele, etc.
    def set_marque(self, nouvelle_marque):
        self._marque = nouvelle_marque

    def get_marque(self):
        return self._marque

    def set_modele(self, nouveau_modele):
        self._modele = nouveau_modele

    def get_modele(self):
        return self._modele

    def set_annee(self, nouvelle_annee):
        self._annee = nouvelle_annee

    def get_annee(self):
        return self._annee

    def set_kilometrage(self, nouveau_kilometrage):
        self._kilometrage = nouveau_kilometrage

    def get_kilometrage(self):
        return self._kilometrage

    def set_en_marche(self, nouvel_etat):
        self._en_marche = nouvel_etat

    def get_en_marche(self):
        return self._en_marche

    def set_reservoir(self, nouveau_reservoir):
        self._reservoir = nouveau_reservoir

    def get_reservoir(self):
        return self._reservoir
# Cette méthode vérifie si le réservoir est suffisamment plein 
# (appel à la méthode privée _verifier_plein). Si le réservoir est suffisant,
# elle met l'attribut _en_marche à True, ce qui signifie que la voiture est en marche.
    def demarrer(self):
        if self._verifier_plein():
            self._en_marche = True
            print("La voiture a démarré.")
        else:
            print("Impossible de démarrer. Le réservoir est trop bas.")
# Cette méthode arrête la voiture en mettant l'attribut _en_marche à False.
    def arreter(self):
        self._en_marche = False
        print("La voiture s'est arrêtée.")
# Cette méthode privée est utilisée dans la méthode demarrer pour vérifier
# si le réservoir a suffisamment d'essence (supérieur à 5 unités)
# pour permettre le démarrage.
    def _verifier_plein(self):
        return self._reservoir > 5

# Exemple d'utilisation de la classe Voiture
ma_voiture = Voiture("Toyota", "Camry", 2022, 15000)

# Affichage des informations avant le démarrage
print(f"En marche : {ma_voiture.get_en_marche()}")
print(f"Reservoir : {ma_voiture.get_reservoir()}")

# Démarrage de la voiture
ma_voiture.demarrer()

# Affichage des informations après le démarrage
print(f"En marche : {ma_voiture.get_en_marche()}")
print(f"Reservoir : {ma_voiture.get_reservoir()}")

# Arrêt de la voiture
ma_voiture.arreter()
