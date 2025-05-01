#tp5.1ej01


milista=[]   #creo una lista vacia

for i in range (1,101):   #aplico un bucle que itere todos los valores de 1 al 100 y si el iterador es multiplo de 4 lo agrego a mi lista
    if i%4==0 :
        milista.append(i)


print(milista)