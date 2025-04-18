#tp5ej05


def validacion_variable(mensaje, min = float("-inf") , max = float("inf")):  #funcion que solicita el ingreso de una variable si la variable a analizar no cumple con el rango de valores ingresados, emite un error
    variable=int(input(f"{mensaje}: ")) 
    while variable<min or variable>max:
        variable=int(input(f"Error.{mensaje}: ")) 
    return variable

def segundos_a_horas(segundos, horas=3600):  #funcion que segun la cantidad de segundos ingresada devuelve su equivalente en horas.
    return segundos/horas



#programa principal

segundos= validacion_variable("Ingrese los segundos que desea convertir en horas",0) #defino la cantidad de segundos, uso la funcion validacion de variable para que no pueda tomar numeros negativos
horas=segundos_a_horas(segundos)
print(f"{segundos} segundos equivalen a {segundos_a_horas(segundos)} hora/s")
