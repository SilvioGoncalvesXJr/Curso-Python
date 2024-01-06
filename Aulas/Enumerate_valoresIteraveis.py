#"É possível realizar a enumeração da lista através do comando inumerate, junto do loop for"

lista = ['Maria', 'Helenna', 'Luiz']
lista.append('João')

lista_enumerada = enumerate(lista)

for item in lista_enumerada:
    print(item)

print('-' * 30)
#Porém, depois de usado o enumerate, a variável é 'zerado', impedindo que seja utilizado novamente. Para isso, ou usa dentro do loop 
# (sempre fica criando um novo interator impedido que esgote) ou converte para lista ou tupla

for item in lista_enumerada:
    print(f"Não tem resultado {item}") #nem entra no loop

lista_enumerada1 = list(enumerate(lista))
print(lista_enumerada1)

print('-' * 30)

for item in enumerate(lista):
    print(item)

print('-' * 30)

#Se quiser, pode fazer o desempacotamento

for indice, nome in enumerate(lista):
    print(f"O indice é {indice}\n \t e o nome é {nome}")
    #\n quebra linha e \t da um tab