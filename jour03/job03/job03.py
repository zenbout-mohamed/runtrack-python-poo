class Tache:
    def __init__(self, titre, description, statut="À Réaliser !"):
        self.titre = titre
        self.description = description
        self.statut = statut
# La méthode __str__ est définie pour permettre une représentation sous forme
# de chaîne de caractères de l'objet Tache.
    def __str__(self):
        return f"{self.titre} - {self.description} - Statut: {self.statut}"


class ListeDeTaches:
    def __init__(self):
        self.taches = []

    def ajouterTache(self, tache):
        self.taches.append(tache)

    def supprimerTache(self, titre):
        self.taches = [tache for tache in self.taches if tache.titre != titre]

    def marquerCommeFinie(self, titre):
        for tache in self.taches:
            if tache.titre == titre:
                tache.statut = "Terminée"

    def afficherListe(self):
        for tache in self.taches:
            print(tache)

    def filterListe(self, statut):
        return [tache for tache in self.taches if tache.statut == statut]


# Test du code
tache1 = Tache("Faire du sport", "Musculation")
tache2 = Tache("Travailler", "Voyager")
tache3 = Tache("Regler mes loyers", "Sommes à payer")

liste_taches = ListeDeTaches()

liste_taches.ajouterTache(tache1)
liste_taches.ajouterTache(tache2)
liste_taches.ajouterTache(tache3)

# Afficher la liste des tâches
print("Liste des tâches:")
liste_taches.afficherListe()


# Une tâche est marquée comme terminée.
liste_taches.marquerCommeFinie("Faire du sport")

# La liste mise à jour est affichée.
print("Liste des tâches après marquerCommeFinie:")
liste_taches.afficherListe()

# Une tâche est supprimée.
liste_taches.supprimerTache("Faire les courses")

# Afficher la liste mise à jour
print("Liste des tâches après supprimerTache:")
liste_taches.afficherListe()

# Filtrer les tâches par statut
taches_a_faire = liste_taches.filterListe("À faire")
print("Liste des tâches à faire:")
for tache in taches_a_faire:
    print(tache)
