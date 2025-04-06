#TP3EJ08

#Solicito al usuario si nombre y opcion

nombre=str(input("Ingrese su nombre: "))
opcion=int(input("Si quiere su nombre en mayuscula ingrese 1.\nSi quiere su nombre en minuscula ingrese 2.\nSi quiere su nombre como titulo ingrese 3. \n"))
                 
#Aplico condicion

if opcion==1 :
    print(nombre.upper())
elif opcion==2 :
    print(nombre.lower())
elif opcion==3 :
    print(nombre.title())
else:
    print("Debe ingresar una opcion valida.")

    