# Funciones

def leer_entero_validado(mensaje, min = float("-Inf"), max = float("Inf")):
    n = int(input(f"{mensaje} "))
    while n < min or n > max:
        n = int(input(f"ERROR. {mensaje} "))
    return n

def leer_positivo_decimal_validado(mensaje, min = float("-Inf"), max = float("Inf")):
    n = float(input(f"{mensaje} "))
    while n < min or n > max:
        n = int(input(f"ERROR. {mensaje} "))
    return n

# Ejercicio 1

def fact(num):
    return 1 if num == 0 else num * fact(num - 1)

def fact_nums_anteriores(num):
    for i in range(1,num+1):
        print( fact(i) )

# Ejercicio 2

def fibonacci_recursivo(posicion):
    if posicion == 0:
        return 0
    elif posicion == 1:
        return 1
    else:
        return fibonacci_recursivo(posicion - 1) + fibonacci_recursivo(posicion - 2)

def fibonacci_nums_anteriores(num):
    for i in range(1,num+1):
        print( fibonacci_recursivo(i) )

# Ejercicio 3
def potencia_base(base,exponente):
    if exponente == 0:
        return 1
    else:
        return base * (potencia_base(base, exponente - 1))
         
# Ejercicio 4

def decimal_binario(num):
    if num == 0:
        return "0"
    else: 
        resto = num % 2
        num //= 2
        binario =  decimal_binario(num) + str(resto) 
    return binario

# Ejercicio 5

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    elif palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

# Ejercicio 6

def suma_digitos(n):
    if n < 10:
        return n
    return (n % 10) + suma_digitos(n // 10)

# Ejercicio 7

def contar_bloques(n):
    if n == 1:
        return n
    return n + contar_bloques(n-1)

# Ejercicio 8

def contar_digito(num,n):
    if num < 10:
        return 1 if num == n else 0
    ultimo = num % 10
    resto = num // 10
    if ultimo == n:
        return 1 + contar_digito(resto, n)
    else:
        return contar_digito(resto, n)
    


# Programa principal
'''
'''
# Ejercicio 1

num = int(input("Ingrese un número: "))
fact_nums_anteriores(num)

# Ejercicio 2

num = int(input("Ingrese un número: "))
fibonacci_nums_anteriores(num)

# Ejercicio 3
base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))
print(potencia_base(base,exponente))

# Ejercicio 4

decimal = int(input("Ingrese un número decimal para convertirlo en binario: "))
print(f"El número {decimal} es el número {decimal_binario(decimal)} en binario.")

# Ejercicio 5

palabra = str(input("Ingrese una palabra para saber si es palíndromo: "))
print(es_palindromo(palabra))

# Ejercicio 6

suma_dig = int(input("Ingrese un número para saber la suma de sus dígitos: "))
print(suma_digitos(suma_dig))

# Ejercicio 7

contador_bloques = int(input("Ingrese la cantidad de bloques de la base de la pirámide: "))
print(contar_bloques(contador_bloques))

#Ejercicio 8

numero = int(input("Ingrese un número: "))
numero2 = int(input("Ingrese el segundo número: "))

print(f"El numero {numero2} aparece {contar_digito(numero,numero2)} veces en el número {numero}")