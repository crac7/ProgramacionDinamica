import random
import math
from bokeh.plotting import figure, show

def crearPuntos(nPuntos):
    puntosXY = []
    xList = []
    yList = []
    for i in range(nPuntos):
        xyList = generatePuntosXY()
        puntosXY.append(xyList)
        x, y = xyList
        xList.append(x)
        yList.append(y)

    
    return (puntosXY, xList, yList)

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


def graficar(x, y):
    grafica = figure(title='Camino aletorio', 
                     x_axis_label='x', 
                     y_axis_label='y')

    grafica.circle(x,y, size=10,color="red")
    show(grafica)

if __name__ == '__main__':
        nPuntos = int(input('Cuantos puntos deseas generar :'))
        collection, xList, yList = crearPuntos(nPuntos)
        print(collection)
        print(comparaPuntosCercanos(collection))
        # print(xList, yList)
        graficar(xList, yList)

       


