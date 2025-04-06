#TP3EJ06

#importo las funciones que necesito
from statistics import mode, median, mean

#defino mi lista aleatoria de numeros

import random

numeros_aleatorios=[random.randint(1,100) for i in range (50)]

#defino la variable moda mediana y media de los numeros aleatorios

moda= mode(numeros_aleatorios)
mediana=median(numeros_aleatorios)
media=mean(numeros_aleatorios)

print(moda,mediana,media)

#aplico condicion para determinar el sesgo

if (media>mediana and mediana>moda):
    print("Sesgo positivo")
elif (media<mediana and mediana<moda):
    print("Sesgo negativo")
elif (media==moda and media==mediana):
    print("Sin sesgo")

