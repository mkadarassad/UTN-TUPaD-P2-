##tp4ej03

##solicito al usuario 2 valores

num1=int(input("Ingrese el primer numero: "))
num2=int(input("Ingrese el segundo numero: "))

#defino la variable suma

suma=0

#aplico una condicion por si el primer valor es menor al segundo, indico que se haga la suma entre los numeros 

if num1<num2:
   for i in range( num1+1, num2,1):
    suma+=i
else:
  for i in range(num2+1,num1,1):
    suma+=i



print(f"La suma de los valores entre los numeros ingresados sin incluirlos es {suma}")