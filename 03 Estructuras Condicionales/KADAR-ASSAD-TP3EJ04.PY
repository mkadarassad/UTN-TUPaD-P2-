#TP3EJ04

##Solicito que ingrese su edad

edad=int(input("Ingrese su edad: "))
         
#Aplico condiciones

if (edad<12) :
    print("Sos un niño/a")
elif (edad<=12 and edad<18) :
    print("Sos un adolecente.")
elif (edad>=18 and edad<30) :
    print("Sos un adulto/a joven")
elif (edad>=30) :
    print("Sos un adulto/a.")