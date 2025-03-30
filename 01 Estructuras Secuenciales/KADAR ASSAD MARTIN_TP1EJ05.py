#una hora tiene 3600 segundos
#defino la variable segundos como entero, y solicito su ingreso
segundos=int(input("Ingrese segundos "))
#defino el calculo de las horas, uso el doble divisor para que me traiga su numero entero
hora=int(segundos//3600)
#lo muestro por consola
print(f"Los segundos ingresados equivalen a {hora} hora/s")