#tp4ej07

#solicito al usuario que ingrese un numero entero positivo

num=int(input("Ingrese un numero entero positivo: "))

#defino un acumulador

suma=0

#aplico un bucle que sume los valores 

for i in range (0,num+1):
    suma+=i


print(f"La suma de los numeros comprendidos entre 0 y {num} es {suma}")