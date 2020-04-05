import random

def tirar_dado(numero_de_tiros):
    secuencia_de_tiros = []

    for _ in range(numero_de_tiros):
        tiro1 = random.choice([1,2,3,4,5,6])
        tiro2 = random.choice([1,2,3,4,5,6])
        sumaDetiros= tiro1 + tiro2 
        secuencia_de_tiros.append(sumaDetiros)
    

    return secuencia_de_tiros

def main(numero_de_tiros, numero_de_intentos):
    tiros = []
    for _ in range(numero_de_intentos):
        secuencia_de_tiros = tirar_dado(numero_de_tiros)
        tiros.append(secuencia_de_tiros)

    tiros_con_12 = 0
    for tiro in tiros:
        if 12 in tiro:
            tiros_con_12 +=1

    probabilidad_tiros_con_1 = tiros_con_1 / numero_de_intentos
    print(f'Probalidad de obtener por lo menos 1 en {numero_de_intentos} tiros = {probabilidad_tiros_con_1}')

if __name__ == '__main__':
    numero_de_tiros = int(input('Cuantas veces tiramos del dado:'))
    numero_de_intentos =  int(input('Cuantas veces correra la simulacion:'))
     
    main(numero_de_tiros, numero_de_intentos)