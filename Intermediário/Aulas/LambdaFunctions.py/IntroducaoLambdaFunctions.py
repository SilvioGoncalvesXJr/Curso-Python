'''
Função lambda em Python é uma função como qualquer outra. Porém, tem como particularidades, 
serem anônimas e serem estruturadas com apenas 1 linha. Ou seja, tude deva ser contido dentro
de uma única expressão.
'''
lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

#Normalmente, não daria para realizar um sort nessa lista pq possui dicionário nela. Uma saída é usar um 'guia'

# def ordenar(item):
#     return item['sobrenome']

# lista.sort(key=ordenar)
# for item in lista:
#     print(item)
#Porém, não é o melhor jeito de aplicar, mas sim usando a lambda

def exibir(lista):
    for item in lista:
        print(item)
    print()
#Pode ser o sort também, ai ficaria lista.sort(key...)
l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['sobrenome'])
#Aqui ele está pegando a função ordenar e desmbrembrando na lambda
#(key='nome da função - como é anonima, fica só lambda), não tem parenteses, coloca só os parametros com ':',
# e não tem o return, colocando o que retornar após os ':'

exibir(l1)
exibir(l2)
