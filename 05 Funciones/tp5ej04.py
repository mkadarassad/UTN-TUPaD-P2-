#tp5ej04

#defino mis funciones

def validacion_variable(mensaje, min = float("-inf") , max = float("inf")):  #funcion que solicita el ingreso de una variable si la variable a analizar no cumple con el rango de valores ingresados, emite un error
    variable=int(input(f"{mensaje}: ")) 
    while variable<min or variable>max:
        variable=int(input(f"Error.{mensaje}: ")) 
    return variable

from math import pi #importo el numero pi para poder calcular el area y el perimetro

def calcular_area_circulo(radio): #funcion que con el paramtreo radio calcula el area
    return (pi*(radio**2))

def calcular_perimetro_circulo(radio): #funcion que con el parametro radio calcula el perimetro
    return (2*pi*radio)



#programa principál


radio=validacion_variable("Ingrese el radio", 1)
print(f"El area del circulo es {calcular_area_circulo(radio)} , y su perimetro es {calcular_perimetro_circulo(radio)}")

