#tp4ej08

#defino la cantidad de numeros a ingresar (aplico 10 para hacer pruebas) y defino los contadores (pares impares positivos y negativos)

cantidad=100
num_pos=0
num_neg=0
num_par=0
num_impar=0

for i in range (1,cantidad+1):
    num=int(input(f"Ingrese numero {i}: "))

    if num>=0:
        num_pos+=1
    else:
        num_neg+=1

    if num%2==0:
        num_par+=1
    else:
        num_impar+=1


print(f"Numeros pares: {num_par}\n"
      f"Numeros impares: {num_impar}\n"
      f"Numeros positivos: {num_pos}\n"
      f"Numeros negativos: {num_neg}\n")


