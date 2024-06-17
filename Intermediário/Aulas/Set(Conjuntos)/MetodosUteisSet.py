s1 = set()
#Set - Adciona valores ao conjunto. Porém, só dá para acrescentar um de cada vez
s1.add('Silvio')
s1.add(1)

#Update = Atualiza os valores do conjunto
s1.update(('Olá mundo', 1, 2, 3, 4))
#Assim, dá para adicionar mais de 1 valor
#Porém, se tivessemos colocado so s1.update('Olá Mundo'), ao invés de pegar a frase toda,
#iria adicionar letra por letra, precisando das duas (())

#Clear - Limpa todo o conjunto
#s1.clear()

#Discard - Remove o item informado
s1.discard('Olá mundo')#Aqui não precisa dos dois (())
s1.discard(1)
print(s1)