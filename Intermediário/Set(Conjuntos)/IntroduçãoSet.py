'''
Sets - São estruturas de dados estruturados em conjuntos matemáticos em Python
Representados graficamente pelo diagrama de Venn
Sets em python são mutáveis, porém aceitam apenas tipos imutáveis como valor interno
'''
#Criando um set
s1 = set() # um set vazio
s1 = {'Luiz', 1, 2, 3} # set com dados
print(s1)
#OBS: Quando dá um print no set, ele mostrará os itens de forma aleatória, não seguinda a ordem alocada ou padrão de crescente ou decrescente, p.ex.

'''
Sets são eficientes para remover valores duplicados de iteráveis
Seus valores sempre serão únicos
Não aceitam valores mutáveis, como listas
Não tem índexes
Como falei na observação, eles não garantem ordem
são iteráveis (for, in, not in)
'''

#Podemos pegar uma lista com valores repetidos e utilizar o set para remover os valores iguais
l1 = [ 1, 2, 3, 3, 4, 5, 5, 1]
l1 = set(l1)
l2 = list(l1)
print(l2)
#Sendo que esse não é o melhor modo