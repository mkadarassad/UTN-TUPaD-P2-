import random
import timeit

# -------------------------------
# Funciones de búsqueda
# -------------------------------

# Búsqueda lineal: recorre la lista de principio a fin
def busqueda_lineal(base_de_datos, dato_buscado):
    for i, valor in enumerate(base_de_datos):       # enumerate obtiene el índice (i) y el valor. 
        if valor == dato_buscado:                   # Si el valor es igual al dato buscado trae la posición de la base de datos (i)
            return i
    return -1

# Búsqueda binaria recursiva: requiere lista ordenada
def busqueda_binaria_recursiva(base_de_datos, indice_min, indice_max, dato_buscado):
    # Devuelve el índice de dato_buscado en base_de_datos si está presente, sino -1

    # Caso base: corrobora que la lista tenga más de un valor
    if indice_max >= indice_min:

        indice_medio = (indice_max + indice_min) // 2       # Busca el valor que está en la mitad de la lista

        # Si el elemento está justo en el indice_medio
        if base_de_datos[indice_medio] == dato_buscado:
            return indice_medio

        # Si el elemento es menor, buscar en la mitad izquierda
        elif base_de_datos[indice_medio] > dato_buscado:
            return busqueda_binaria_recursiva(base_de_datos, indice_min, indice_medio - 1, dato_buscado)

        # Si el elemento es mayor, buscar en la mitad derecha
        else:
            return busqueda_binaria_recursiva(base_de_datos, indice_medio + 1, indice_max, dato_buscado)

    else:
        # El elemento no está presente en base_de_datos
        return -1

# Búsqueda binaria iterativa: requiere lista ordenada
def busqueda_binaria_iterativa(base_de_datos, dato_buscado):
    indice_min = 0
    indice_max = len(base_de_datos) - 1                     # Tamaño de la base de datos
    indice_medio = 0

    # Caso base: corrobora que la lista tenga más de un valor
    while indice_max >= indice_min:   

        indice_medio = (indice_max + indice_min) // 2   # Busca el valor que está en la mitad de la lista

        # Si dato_buscado es menor, buscar en la mitad izquierda
        if base_de_datos[indice_medio] > dato_buscado:
            indice_max = indice_medio - 1

        # Si dato_buscado es mayor, buscar en la mitad derecha
        elif base_de_datos[indice_medio] < dato_buscado:
            indice_min = indice_medio + 1

        # Significa que dato_buscado está en el indice_medio
        else:
            return indice_medio

    # Si llegamos hasta acá, el elemento no está presente
    return -1

# -------------------------------
# Programa principal
# -------------------------------

# Sample selecciona de una lista de valores una cantidad de valores random 
# base_de_datos = random.sample(range(1, 2000000), 1000001)
# Creo una base de datos con 1001 valores únicos entre 1 y 2000
base_de_datos = random.sample(range(1, 2001), 1001)

# Ordeno la base de datos para que sea válida para búsqueda binaria
base_de_datos.sort()

# Llamada a la función
# posicion_valor_a_buscar = random.randint(0, len(base_de_datos) - 1)
# valor_a_buscar = base_de_datos[posicion_valor_a_buscar] 

# Diccionario que asocia nombres de funciones con las funciones correspondientes
funciones = {
    "busqueda_lineal": busqueda_lineal,
    "busqueda_binaria_iterativa": busqueda_binaria_iterativa,
    "busqueda_binaria_recursiva": busqueda_binaria_recursiva
}

# Lista de posiciones en la base de datos que serán utilizadas como valores representativos a buscar
# valores_representativos = [0, 300000, 500000, 650000, 1000000]
valores_representativos = [0, 500, 1000]

# Itero sobre los valores representativos para evaluar cada algoritmo de búsqueda
for posicion_valor_a_buscar in valores_representativos:
    valor_a_buscar = base_de_datos[posicion_valor_a_buscar]
    print(f"Se buscará el valor {valor_a_buscar} que se encuentra en la posición {posicion_valor_a_buscar}\n")

    # Pruebo cada función de búsqueda
    for nombre_funcion, funcion in funciones.items():   # items() devuelve un valor en base al diccionario

        # La búsqueda binaria recursiva requiere argumentos adicionales
        if nombre_funcion == "busqueda_binaria_recursiva":
            tiempo_inicio = timeit.default_timer()
            resultado = funcion(base_de_datos, 0, len(base_de_datos), valor_a_buscar)
            tiempo_final = timeit.default_timer() - tiempo_inicio
        else:
            tiempo_inicio = timeit.default_timer()
            resultado = funcion(base_de_datos, valor_a_buscar)
            tiempo_final = timeit.default_timer() - tiempo_inicio

        # Muestro resultados de cada función
        print("------------------------------")
        print(f"Resultado de la función {nombre_funcion}:\n")
        if resultado == -1:
            print("No se encontró el valor en la lista.")
        else:
            print(f"El valor {valor_a_buscar} se encuentra en la posición {resultado}.")
        print(f"El tiempo de respuesta fue de {tiempo_final * 1000} milisegundos\n")
