#defino la variable radio como numero decimal
radio=float(input("Ingrese el radio "))
#importo la biblioteca math para traer el numero pi
import math
#defino el calculo del perimetro
perimetro=float(2*(math.pi)*radio)
#defino el calculo del area
area=float((math.pi)*radio*radio)
print(f"El area es {area} y su perimetro es {perimetro}")