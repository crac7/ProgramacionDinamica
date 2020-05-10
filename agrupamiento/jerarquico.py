import random
import math
def crearPuntos(nPuntos):
    puntosXY = []

    for i in range(nPuntos):
        puntosXY.append(generatePuntosXY())
    
    return puntosXY

def comparaPuntosCercanos(coleccionPuntos):
    agrupamiento = []
    for actualXY in coleccionPuntos:
        distanciaXY = []   

        for nextXY in coleccionPuntos:
            if(actualXY != nextXY):
                distancia = disntanciaEcuclidiana(actualXY ,nextXY)
                distanciaXY.append(distancia)


        lastPosition = coleccionPuntos[len(coleccionPuntos)-1]
        if(actualXY != lastPosition):
            positionMin = distanciaXY.index(min(distanciaXY))
            nextPunto =  coleccionPuntos[positionMin+1]
            agrupamiento.append([actualXY,nextPunto]) 

            

    return agrupamiento         


def disntanciaEcuclidiana(actualXY , nextXY):
    x1, y1 = actualXY
    x2, y2 = nextXY

    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
     

def generatePuntosXY():
        puntosXY = []
        x = random.randint(0,5)
        y = random.randint(0,5)
        puntosXY.append(x)
        puntosXY.append(y)

        return puntosXY

if __name__ == '__main__':
        nPuntos = int(input('Cuantos puntos deseas generar :'))
        collection = crearPuntos(nPuntos)
        print(f'puntos ==> {collection}')
        print(comparaPuntosCercanos(collection))

