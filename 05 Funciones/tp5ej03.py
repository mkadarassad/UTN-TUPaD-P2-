#tp5ej03

#defino la funcion

def informacion_personal(nombre,apellido,edad,residencia):
    return print(f"Soy {nombre.title()} {apellido.title()} tengo {edad} años y vivo en {residencia.title()}")

#programa principal

nombre_usuario=input("Ingrese su nombre: ")
apellido_usuario=input("Ingrese su apellido: ")
edad_usuario=int(input("Ingrese su edad: "))
residencia_usuario=input("Ingrese su residencia: ")

informacion_personal(nombre_usuario,apellido_usuario,edad_usuario,residencia_usuario)