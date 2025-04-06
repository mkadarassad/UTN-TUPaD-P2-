#TP03EJ07

#Solicito al usuario una frase

frase=str(input("Ingrese una frase: "))

#convierto la frase en minuscula

frase_minuscula=frase.lower()

#busco el ultimo caracter de la frase

ultimo_caracter= frase_minuscula[-1]


#aplico condicion

if (ultimo_caracter=="a" or ultimo_caracter=="e" or ultimo_caracter=="i" or ultimo_caracter=="o" or ultimo_caracter=="u") :
    print(f"{frase}!")
else:
    print(frase)
