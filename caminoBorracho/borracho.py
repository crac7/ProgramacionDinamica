import random


class Borracho:

    def __init__(self, nombre):
        self.nombre=nombre;

# difrentes boorachos
class BorrachoTradicional(Borracho):

    def __init__(self, nombre):
        super().__init__(nombre) #refrencia a clases Borreacho

    def camina(self):
        return random.choice([(0,1), (0,-1), (1,0), (-1,0)])