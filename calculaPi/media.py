import random
import math

def media(X):
    return sum(X) / len(X)

def varianza(X):
    mu = media(X)
    
    acumulador = 0
    for x in X:
        acumulador +=(x - mu)**2

    return acumulador / len(X)

def desvacionEstandar(X):
    return math.sqrt(varianza(X))

if __name__ == '__main__':
    X = [random.randint(9, 12) for  i in range(20)]
    mu = media(X)
    var =  varianza(X)
    sigma  =  desvacionEstandar(X)

    print(f'media del arreglo {X}')
    print(f'Media = {mu}')
    print(f'Varianza = {var}')
    print(f'desvacionEstandar = {sigma}')
