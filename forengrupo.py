diccionario = {'Ayax':7, 'Eric': 8, 'Kevin': 10, 'Diego': 5, 'Ricardo':9, 'Julio':6 }

for x,y in diccionario.items():
    print(x,y)
    

for x,y in diccionario.items():
    num = diccionario.values()
    lista = list(num)
    minimo = min(num)
    maximo = max(num)

print('maximo es '+ str(maximo) +' minimo es ' +str(minimo))
    