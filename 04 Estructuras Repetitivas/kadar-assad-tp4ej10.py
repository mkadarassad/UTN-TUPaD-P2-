#tp4ej10

#defino la variable numero invertido

num_inv=str()

#solicito al usuario un numero entero

num=str(input("Ingrese un numero: "))


#aplico bucle para que me traiga los valores del numero al reves

for i in range(len(num)-1,-1,-1):
    num_inv+=num[i]


print(num_inv)