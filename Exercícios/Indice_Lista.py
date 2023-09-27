# Exiba os índices da lista

lista = ['Maira', 'Helena', 'Luiz']
indice = 0
for i in lista:
    print(f'O nome {i}, está na posição {indice} da lista')
    indice += 1
#OU
lista = ['Maira', 'Helena', 'Luiz']
indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))