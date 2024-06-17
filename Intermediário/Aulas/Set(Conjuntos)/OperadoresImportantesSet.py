#Operadores importantes aplicados aos conjuntos
s1 = {1, 2, 3}
s2 = {2, 3, 4}
#União | União -> Une os sets
s3 = s1 | s2
print(s3)

#Intersecção & Intersecção -> Mostra os itens presentes em ambos os Sets
s3 = s1 & s2
print(s3)

#Diferença - Diferença -> Apresenta os itens presentes apenas no primeiro set (esquerda), por isso, importa a ordem
s3 = s1 - s2
s4 = s2 - s1
print(s3, s4)

#Diferença Simétrica ^ -> Mostra os itens que não estão na interseccção, não importando a ordem dos sets
s3 = s1 ^ s2
print(s3)