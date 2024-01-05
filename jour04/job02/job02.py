class Personne:
    # La classe Personne a un attribut age incrémenté de 20,
    # et elle possède les méthodes afficherAge, bonjour, et modifierAge.
    def __init__(self, age=15):
        self.age = age

    def afficherAge(self):
        print(f"L'âge de la personne est de {self.age} ans.")

    def bonjour(self):
        print("Hello")

    def modifierAge(self, nouvel_age):
        self.age = nouvel_age

# La classe Eleve hérite de la classe Personne et a une méthode additionnelle
# allerEnCours. Elle redéfinit également la méthode afficherAge pour afficher
# un message spécifique.
class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")

    def afficherAge(self):
        print(f"J'ai {self.age} ans.")

# La classe Professeur hérite également de la classe Personne avec un attribut 
# supplémentaire matiereEnseignee. Elle a une méthode additionnelle enseigner.
class Professeur(Personne):
    def __init__(self, age=40, matiere_enseignee=""):
        super().__init__(age)
        self.matiereEnseignee = matiere_enseignee

    def enseigner(self):
        print(f"Le cours de {self.matiereEnseignee} va commencer.")


# Des instances des différentes classes sont créées et les méthodes sont appelées pour
# illustrer le fonctionnement du code.
# Instanciation Personne :
personne1 = Personne()
personne1.afficherAge()  
personne1.bonjour()     

# Instanciation Eleve :
eleve1 = Eleve()  
eleve1.allerEnCours()   

# Instanciation d'un Professeur
professeur1 = Professeur(age=40, matiere_enseignee="Physique")
professeur1.bonjour()    # Affiche "Hello"
professeur1.enseigner()   


 
