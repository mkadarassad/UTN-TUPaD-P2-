#TP3EJ05

#solicito al usuario una contraseña

contraseña=str(input("Ingrese una contraseña entre 8 y 14 caracteres."))

#aplico condicion

if (len(contraseña)>=8 and len(contraseña)<=14):
    print("Ha ingresado una contraseña correcta.")
else:
    print("Por favor ingrese una contraseña entre 8 y 14 caracteres")