

def celcius_a_farenheit(gradoscelcius):    #busco el codgio de un ejercicio anterior para definir mi funcion de grados celcius a ferenheit
    gradosFarenheit=float((9/5)*gradoscelcius+32)
    return gradosFarenheit



#programa principal

celcius=float(input("Ingrese grados Celcius: "))  #solicito al usuario los grados
farengheit=celcius_a_farenheit(celcius)         #traigo mi funcion

print(f"{celcius} grados Celcius equivalen a {farengheit} grados Farenheit")