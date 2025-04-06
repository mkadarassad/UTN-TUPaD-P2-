#TP3EJ10

#Solicito al usuario la informacion requerida y defino las variables 

hemisferio=str(input("Ingrese N si se encuentra en el hemosferio norte.\nIngrese S si se encuentra en el hemisferio sur."))
dia=int(input("Ingrese nro de día de hoy (del 1 al 31): "))
mes=int(input("Ingrese nro de mes actual (del 1 al 12): "))
#convierto 
hemisferio=hemisferio.upper()



#aplico condiciones

if ((hemisferio=="N") and ((dia>=21 and mes==12) or (mes==1) or (mes==2) or (dia<=20 and mes==3))):
    print("Es invierno.")
elif((hemisferio=="S") and ((dia>=21 and mes==12) or (mes==1) or (mes==2) or (dia<=20 and mes==3))):
    print("Es verano.")
elif((hemisferio=="N") and ((dia>=21 and mes==3) or (mes==4) or (mes==5) or (dia<=20 and mes==6))):
    print("Es primavera.")
elif((hemisferio=="S") and ((dia>=21 and mes==3) or (mes==4) or (mes==5) or (dia<=20 and mes==6))):
    print("Es otoño")
elif((hemisferio=="N") and ((dia>=21 and mes==6) or (mes==7) or (mes==8) or (dia<=20 and mes==9))):
    print("Es verano")
elif((hemisferio=="S") and ((dia>=21 and mes==6) or (mes==7) or (mes==8) or (dia<=20 and mes==9))):
    print("Es invierno.")
elif((hemisferio=="N") and ((dia>=21 and mes==9) or (mes==10) or (mes==11) or (dia<=20 and mes==12))):
    print("Es otoño.")
elif((hemisferio=="S") and ((dia>=21 and mes==9) or (mes==10) or (mes==11) or (dia<=20 and mes==12))):
    print("Es primavera.")
else:
    print("Los datos no son correctos.")

