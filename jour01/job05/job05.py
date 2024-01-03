class Point:
    # Le constructeur (__init__) est une méthode spéciale appelée lors de la création d'une nouvelle instance de la classe.
    # Il prend les coordonnées x et y en paramètres et initialise les attributs x et y de l'objet Point avec ces valeurs.
    def __init__(self, x, y):
        self.x = x
        self.y = y
    # Cette méthode affiche les coordonnées du point en utilisant la fonction print.
    # Les valeurs de x et y sont obtenues à partir des attributs de l'objet.
    def afficherLesPoints(self):
        print(f"Coordonnées du point : ({self.x}, {self.y})")
    # Ces méthodes affichent respectivement la coordonnée horizontale x et la coordonnée verticale y en utilisant la fonction print.
    def afficherX(self):
        print(f"Coordonnée de l'abcisse (x) : {self.x}")

    def afficherY(self):
        print(f"Coordonnée de l'ordonnée (y) : {self.y}")
# -------------------------------------------------------------------------------------------------------------------------#
# Ces méthodes permettent de changer les valeurs des attributs x et y de l'objet en leur assignant de nouvelles valeurs.
    def changerX(self, new_value_x):
        self.x = new_value_x

    def changerY(self, new_value_y):
        self.y = new_value_y
# Une instance de la classe Point est créée avec les coordonnées initiales (3, 4).
# Les coordonnées sont ensuite affichées, puis les méthodes pour afficher x et y sont appelées.
# Ensuite, les coordonnées sont changées à (7, 9) à l'aide des méthodes changerX et changerY,
# et les nouvelles coordonnées sont affichées à la fin.


point = Point(3, 4)

point.afficherLesPoints()
point.afficherX()
point.afficherY()
point.changerX(7)
point.changerY(9)
point.afficherLesPoints()

# Cela résume le fonctionnement de la classe Point et son utilisation dans cet exemple.
# La classe permet de représenter un point dans un espace bidimensionnel avec des coordonnées x et y.