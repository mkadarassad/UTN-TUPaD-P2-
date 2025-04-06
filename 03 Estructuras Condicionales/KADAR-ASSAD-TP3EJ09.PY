#TP3EJ09

#Solicito al usuario la magnitud segun escala richter

categoria=float(input("Ingrese magnitud del 2 al 8 segun escala richter: "))

#aplico condiciones

if categoria<3 :
    print("Muy leve")
elif (categoria>=3 and categoria<4) :
    print("Leve")
elif (categoria>=4 and categoria<5) :
    print("Moderado")
elif (categoria>=5 and categoria<6) :
    print("Fuerte")
elif (categoria>=6 and categoria<7) :
    print("Muy Fuerte")
elif (categoria>=7):
    print("Extremo")