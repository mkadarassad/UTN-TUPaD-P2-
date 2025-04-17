##tp4ej02

##solicito al usuario un numero entero

print("Ingrese un numero entero")
num=input()

Contador_digitos=0

for i in range (1,(len(num)+1)):
    Contador_digitos+=1

print(f"El numero ingresado tiene {Contador_digitos} digitos")