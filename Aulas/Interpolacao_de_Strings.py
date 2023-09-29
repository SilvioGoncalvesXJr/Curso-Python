"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (0123456789ABCDEF)
"""
nome = "Silvio"
valor = 1000.95897643
variavel = '%s, o preço é de R$%.2f' % (nome, valor)
print(variavel)
print("O hexadecimal de %d é %04X" % (1500, 1500))
""" Nesse caso, ao inves de format, que colocamos as variáveis entre {}, na interpolação
as variáveis são indicadas por '%' e o tipo da mesma, associando-a a variável. 
Se tiver só uma, não precisa indicar entre (), apenas colocar o % ao final também"""
