#tp4ej05


import random

#defijo un numero aleatorio , solicito al usuario un numero y defino un contador de intentos

numero_aleatorio=random.randint(0,9)
num=int(input("Ingrese un numero del 0 al 9: "))
intentos=1


#armo un bucle que compare el numero con el numero aleatorio

while num!=numero_aleatorio:
    num=int(input("Ingrese un numero del 0 al 9: "))
    intentos+=1


print(f"Adivinaste! El numero correcto es {numero_aleatorio}, en {intentos} intentos.")