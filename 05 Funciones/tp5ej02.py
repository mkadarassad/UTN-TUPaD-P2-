#tp5ej02

#defino la funcion

def saludar_usuario(nombre , simbolo = "!"):
     return print(f"Hola {nombre}{simbolo}")

#programa principal

nombre_usuario=input("Ingrese su nombre: ")
saludar_usuario(nombre_usuario)