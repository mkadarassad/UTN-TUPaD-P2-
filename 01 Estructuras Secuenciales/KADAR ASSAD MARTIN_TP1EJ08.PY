#defino altura y peso como nro decimal y solicito su ingreso
altura=float(input("Ingrese su altura en metros "))
peso=float(input("Ingrese su peso en kg "))
#defino el IMC y su calculo
IMC=float(peso/(altura*altura))
print("Su IMC es ",IMC)