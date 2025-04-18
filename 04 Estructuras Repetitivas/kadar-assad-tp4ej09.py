#tp4ej09

#defino la cantidad de numeros a ingresar (aplico 10 para hacer pruebas)  y defino un acumulador

cantidad=100
suma=0

#solicito al usuario los valores y acumulo los valores en suma

for i in range (1,cantidad+1):
    num=int(input(f"Ingrese numero {i}: "))
    suma+=num


#aplico la media

print(f"La media de los valores ingresados es {suma/i}")
    

