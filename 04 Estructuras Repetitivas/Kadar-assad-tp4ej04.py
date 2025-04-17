#tp4ej04



#solicito al usuario un numero

num=int(input("Ingrese un valor a sumar, para terminar la suma ingrese un cero: "))

#defino la variable suma que va a mostrar el acumulado de los numeros ingresados

suma=num

#aplico un bucle que solicite los numeros a sumar, hasta que se cargue un cero

while num!=0:
    num=int(input("Ingrese un valor a sumar, para terminar la suma ingrese un cero: "))
    suma+=num


print(f"La suma de los valores ingresados es {suma}")