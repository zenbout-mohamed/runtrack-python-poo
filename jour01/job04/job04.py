class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def SePresenter(self):
        return f"Je m'appelle {self.nom} {self.prenom}"

# Instanciation de plusieurs personnes
personne1 = Personne("Jhon", "Doe")
personne2 = Personne("Jean", "Dupond")

# Appel de la méthode SePresenter pour chaque personne
print(personne1.SePresenter())
print(personne2.SePresenter())

