#tp5ej08

def calculadora_imc(peso,altura):     #defino mi calculadora de imc
    imc = float(peso/(altura**2))
    return  imc




#programa principal

peso=float(input("Ingrese su peso en kilogramos:"))
altura=float(input("Ingrese su altura en metros: "))

print(f"Su indice de masa corporal es: {calculadora_imc(peso,altura)}")