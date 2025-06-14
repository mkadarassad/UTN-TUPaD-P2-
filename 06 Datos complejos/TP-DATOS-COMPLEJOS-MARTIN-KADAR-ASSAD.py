
# Ejercicio 1
'''
'''
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

print(precios_frutas)

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas)

# Ejercicio 2

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(precios_frutas)

# Ejercicio 3

frutas = precios_frutas.keys()

print(frutas)

# Ejercicio 4

def mi_lista_contactos(contactos):
    for i in range (1,6):
        nombre = input("Ingrese el nombre del contacto: ")
        telefono = int(input("Ingrese el teléfono: "))
        contactos [nombre] = telefono

contactos = {}


mi_lista_contactos(contactos)

busqueda_telefono = str(input('Ingrese el nombre del contacto para saber su teléfono: '))
if busqueda_telefono in contactos:
    print(contactos[busqueda_telefono])
else:
    print("No se encontró el contacto.")
# Ejercicio 5

entrada = str(input('Ingrese una frase: '))

palabras = entrada.split( )
palabras_unicas = set(palabras)
tupla_palabras = tuple(palabras)

print(f"Palabras únicas: {palabras_unicas}")

conteo_palabras = {}

for palabra in palabras_unicas:
    conteo_palabras[palabra] = tupla_palabras.count(palabra)

print(f"Recuento: {conteo_palabras}")

#Ejercicio 6

def ingreso_alumnos (cant_alumnos=1, cant_notas=1):
    dataset = {}
    for i in range(1, cant_alumnos+1):
        alumno = input(f"Ingrese el alumno número {i}: ")
        notas = []
        for h in range(1, cant_notas+1):
            nota = float(input(f"Ingrese la nota número {h} para {alumno}: "))
            notas.append(nota)
            dataset[alumno] = tuple(notas)
    return dataset

def calcular_promedios(dataset):
    promedios = {}
    for alumno, notas in dataset.items():
        promedio = sum(notas) / len(notas)
        promedios[alumno] = promedio
    return promedios


dataset = ingreso_alumnos(3,3)
print(dataset)

promedios = calcular_promedios(dataset)

print("Promedios:")
for alumno, promedio in promedios.items():
    print(f"{alumno}: {promedio:.2f}")


# Ejercicio 7

def aprobaron_ambos (parcial1, parcial2):
    return parcial1 & parcial2

def aprobaron_solo_uno (parcial1, parcial2):
    return parcial1 ^ parcial2

def aprobaron_al_menos_uno(parcial1,parcial2):
    return parcial1 | parcial2

parcial1 = {"Jorge", "Adrián", "Pedro", "Agustina"}
parcial2 = {"Roberto", "Agustina", "Julián", "Adrián"}

ambos = aprobaron_ambos(parcial1, parcial2)
solo_uno = aprobaron_solo_uno(parcial1, parcial2)
al_menos_uno = aprobaron_al_menos_uno(parcial1, parcial2)

print(f"Aprobaron ambos parciales: {ambos}")
print(f"Aprobaron sólo un parcial: {solo_uno}")
print(f"Aprobaron al menos un parcial: {al_menos_uno}")

# Ejercicio 8
def consulta_stock():
    producto = input("Ingrese el nombre del producto: ").lower()
    if producto in stock:
        print(f"Stock de {producto}: {stock[producto]}")
    else:
        print(f"El producto {producto} no existe en la base de datos.")

def agrega_unidades():
    producto = input("Ingrese el nombre del producto: ").lower()
    if producto in stock:
        cantidad = input("Ingrese la cantidad de unidades a agregar: ")
        if cantidad.isdigit():
            stock[producto] += int(cantidad)
            print(f"El producto {producto} ahora tiene {stock[producto]} unidades.")
        else:
            print("No se pudo agregar ya que el formato es incorrecto.")
    else:
        print("El producto que ingresó no existe. Vuelva a intentar.")

def agrega_producto():
    producto = input("Ingrese el nombre del nuevo producto: ").lower()
    if producto in stock:
        print(f"El producto {producto} ya existe. Vuelva a intentar.")
    else:
        cantidad = input(f"Ingrese las cantidades de {producto}: ")
        if cantidad.isdigit():
            stock[producto] = int(cantidad)
            print(f"Se agregó el producto {producto} con {cantidad} unidad/es.")
        else:
            print("Ingresó un valor no válido. Debe ingresar un número entero. Vuelva a ejecutar.")

stock = {"notebooks": 15, "celulares": 20, "tablets": 40}
opciones = {"consultar stock": consulta_stock, 
            "agregar unidades": agrega_unidades, 
            "agregar un nuevo producto": agrega_producto}

def calculadora_stock():
    opcion = input("Seleccione la opción deseada:\n'consultar stock', 'agregar unidades' o 'agregar un nuevo producto':\n").lower()
    if opcion in opciones:
        opciones[opcion]() 
    else:
        print("Opción no válida, vuelva a ejecutar.")

calculadora_stock()

# Ejercicio 9

agenda = {
    ("lunes", "10:00"): "Programación 1",
    ("martes", "14:00"): "Matemática",
    ("miércoles", "16:00"): "Arquitectura y Sistemas Operativos",
    ("viernes", "08:00"): "Organización empresarial"
}

def consultar_agenda():
    dia = input("Ingresá el día (ej. lunes): ").lower()
    hora = input("Ingresá la hora (formato 24hs, ej. 10:00): ")

    clave = (dia, hora)
    if clave in agenda:
        print(f"A las {hora} del {dia} tenés: {agenda[clave]}")
    else:
        print(f"No hay actividades registradas el {dia} a las {hora}.")

def ejecutar_agenda():
    while True:
        print("1. Consultar actividad")
        print("2. Salir")

        opcion = input("Elegí una opción (1-2): ")

        if opcion == "1":
            consultar_agenda()
        elif opcion == "2":
            print("Saliendo de la agenda.")
            break
        else:
            print("Opción inválida. Ingresá 1 o 2.")

ejecutar_agenda()

# Ejercicio 10

paises_a_capitales = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Chile": "Santiago",
    "Uruguay": "Montevideo",
    "Paraguay": "Asunción"
}

capitales_a_paises = {}
for pais, capital in paises_a_capitales.items():
    capitales_a_paises[capital] = pais

print("Diccionario invertido (capitales ded países):")
print(capitales_a_paises)