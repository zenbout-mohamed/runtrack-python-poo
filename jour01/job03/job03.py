# En nous aidant de la classe précedente, ce code est dévloppé d'avantage pour ajouter de nouvelles focntions :
class Operation:
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def addition(self):
        total = self.number1 + self.number2
        print(f"Le résultat de l'addition est : {total}")

# Exemple d'utilisation
number1 = 9
number2 = 6

op_instance = Operation(number1, number2)
op_instance.addition()
