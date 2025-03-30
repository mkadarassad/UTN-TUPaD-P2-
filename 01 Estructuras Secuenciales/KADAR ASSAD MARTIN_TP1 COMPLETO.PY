#TP1EJ01

print("Hola Mundo!")

#TP1EJO2

nombre=input("Ingrese su nombre ")
print(f"Hola {nombre}!")

#TP1EJO3

nombre=input("Ingrese su Nombre ")
apellido=input("Ingrese su apellido ")  
edad=int(input("Ingrese su edad "))
residencia=input("Ingrese su lugar de residencia ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

#TP1EJO4
#defino la variable radio como numero decimal
radio=float(input("Ingrese el radio "))
#importo la biblioteca math para traer el numero pi
import math
#defino el calculo del perimetro
perimetro=float(2*(math.pi)*radio)
#defino el calculo del area
area=float((math.pi)*radio*radio)
print(f"El area es {area} y su perimetro es {perimetro}")


#TP1EJO5
#una hora tiene 3600 segundos
#defino la variable segundos como entero, y solicito su ingreso
segundos=int(input("Ingrese segundos "))
#defino el calculo de las horas, uso el doble divisor para que me traiga su numero entero
hora=int(segundos//3600)
#lo muestro por consola
print(f"Los segundos ingresados equivalen a {hora} hora/s")

#TP1EJO6

#voy a usar una iteracion para que me muestre la tabla del numero ingresado.
numero=int(input("Ingrese un numero"))
for i in range(0,11):
    print(F"{numero} x {i} = {numero * i }")


#TP1EJO7

#Defino los numeros como enteros
numero1=int(input("Ingrese primer numero distinto de cero"))
numero2=int(input("Ingrese segundo numero distinto de cero"))
suma=numero1+numero2;
resta=numero1-numero2;
multiplicacion=numero1*numero2;
#defino la division como numero decimal
division=float(numero1/numero2);
print(f"La suma es {suma}")
print(f"La resta es {resta}")
print(f"La multiplicacion es {multiplicacion}")
print(f"La division es {division}")


#TP1EJO8

#defino altura y peso como nro decimal y solicito su ingreso
altura=float(input("Ingrese su altura en metros "))
peso=float(input("Ingrese su peso en kg "))
#defino el IMC y su calculo
IMC=float(peso/(altura*altura))
print("Su IMC es ",IMC)

#TP1EJO9

#solicito al usuario los grados celcius y lo defino como nro real
gradosCelcius=float(input("Ingrese Grados Celcius "))
#defino los grados farenheit como real y su conversion
gradosFarenheit=float((9/5)*gradosCelcius+32)
print(f"El valor ingresado equivale a {gradosFarenheit} grados Farenheit")

#TP1EJ10

#Solicito al usuario 3 numeros
print("Ingrese numeros")
Numero1=float(input("Primer numero "))
Numero2=float(input("Segundo numero "))
Numero3=float(input("Tercer numero "))
#imprimo el promedio
print("El promedio es ",((Numero1 + Numero2 + Numero3)/3))
