#tp5ej07

def operaciones_basicas(a,b):                                                       #defino una funcion que pueda dividir sumar restar y multiplicar 2 numeros
    while b==0:
        b=int(input(f"No se puede dividir por cero. Ingrese un nuevo valor: "))
    
    suma=int(a+b)
    resta=int(a-b)
    multiplicacion=int(a*b)
    division=float(a/b)
    
    print(f"La suma es {suma}\nLa resta es {resta}\nLa multiplicacion es {multiplicacion}\nLa division es {division} ")    



#Programa principal        


num1=int(input("Ingrese numero 1: "))
num2=int(input("Ingrese numero 2: "))

operaciones_basicas(num1,num2)