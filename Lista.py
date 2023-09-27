"""
Lista em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - Índices e fatiamento
Métodos úteis: 
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido (índice, posição)
    pop - Remove do final ou do índice escolhido
    del - Apaga um índice
    clear - Limpa a lista
    extend - Estende a lista
    + - Concatena listas 
Create Read Update Delete
Criar, Ler, Alterar, Apagar = lista[i] (CRUD)
"""

lista = [123, True, 'Luiz Otávio', 1.2, []]
lista[-3] = 'Maria'
print(lista)
print(lista[2], type(lista[2]))

lista2 = [10, 20, 30, 40]
lista2.append(50)
lista2.pop() #Remove o último valor da lista
lista2.append(60)
lista2.append(70)
ultimo_valor = lista2.pop(3)
print(f'Na {lista2}, o último valor removido foi {ultimo_valor}')
"""
Nas listas, é interessante que realize alterações nos valores, como adicionar ou retirar, apenas no final das listas.
Se fizer no começo ou meio, fará com que o pyhton tenha qu reorganizar as posições de todos os demais, gastando muita
capacidade de processamento, deixando o sistema lento. Isso, principalmente, em listas muito grandes
"""

lista3 = [10, 20, 30, 40]

lista3.append('Silvio')
nome = lista3.pop()
lista3.append(1233)
del lista3[-1] #Remover o último elemento da lista
lista3.insert(4, 5)
lista3.insert(100000, 29)
print(lista3) #No método insert, nesse caso não dará erro, por ele analisar a posição em si, mas qual valor é maior e anexar
print(lista3[5])