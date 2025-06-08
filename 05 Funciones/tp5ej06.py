#tp5ej06

def tabla_multiplicar(x):   #defino una funcion que muestre la tabla de un numero x.
    for i in range(1,11):
        print(f"{x}x{i}={x*i}")


#programa principal

numero=int(input("Ingrese numero: "))

print(f"La tabla del {numero} es: ")
tabla_multiplicar(numero)
