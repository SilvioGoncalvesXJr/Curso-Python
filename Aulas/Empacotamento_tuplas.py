"""
Existem casos em que é possível realizar a assciação e desassociação de elementos deuma lista a variáveis específicas,
através do desempacotamento
Nesse caso, é simples, como verá abaixo, mas tem alguns detalhes importantes
"""

lista = ['Silvio', 'João', 'Lucas']

nome1, nome2, nome3 = lista
print(f"""{nome1},
{nome2},
{nome3}""")
#Como pode-se perceber, cada valor da lista foi associada a variável posicional equivalente. Porém. existe outros jeitos...
#Caso eu só queira pegar 1 valor, posso fazer da seguinte forma:
nome1, *_ = lista
print(nome1, _)
#Aqui, o primeiro valor é armazenado na variável, e o resto fica em outra variável, utilizando o '*' antes do nome
# E, por convenção, quando tem uma variável que não irá utilizar, coloca como '_'
# ___________________________________________________________________________________________________________________
"""Porém, existem outras ferramentas no pyhton que lida com agrupamento de dados, como o caso das tuplas.
As tuplas, objetivamente, são listas, mas que não podem ser alteradas, são imultáveis. Caso queira adicionar ou remover
algum elemento, tem que converter para lista, realizar as operações, e depois converter novamente para tupla, a tornando estática.
As tuplas são representadas por ("valor1", "valor2","valor3"...) ou da mesma forma, mas em as ()"""
print('-'*15)
nomes = ('Maria', 'Helena','Luiz')
nomes = list(nomes)
nomes.append('Silvio')
nomes = tuple(nomes)
print(nomes)

