#TP3EJ03ALTERNATIVO

#Solicito al usuario que ingrese un numero par

numero=int(input("Ingrese un numero par: "))


#puedo aplicar un bucle para si ingresa un numero impar, me vuelva a solicitar un valor

while (numero%2!=0):
       numero=int(input("Por favor ingrese un numero par: "))


print(f"El numero ingresado, {numero} es un numero par")