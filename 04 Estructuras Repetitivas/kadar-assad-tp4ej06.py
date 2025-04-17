#tp4ej06

#aplico un bucle que muestre el iterador con rango menos 2 y empiece desde 100 hasta 0

for i in range(100,-1,-2):
    print(i)



print("////////////////)")

#otra forma seria aplicando un bucle entre 0 y 100 y que muestre solo los numeros pares


#defino la variable num

num=100

while (num<=100 and num>=0):
    if num%2==0:
        print(num)
        num-=1
    else:
        num-=1