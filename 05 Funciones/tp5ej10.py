#tp5ej10

def calcular_promedio( a , b , c ):    #defino una funcion que pida 3 numeros y calcule su promedio
    promedio=float((a+b+c)/3)
    return promedio




#funcion principal

num1=float(input("Ingrese numero 1: "))
num2=float(input("Ingrese numero 2: "))
num3=float(input("Ingrese numero 3: "))

promedio=calcular_promedio(num1,num2,num3)

print(f"El promedio es {promedio}")