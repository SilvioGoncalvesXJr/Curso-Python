#Metodos úteis dos Dicionário

pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'sobrenome': 'Miranda 2'
}#Chaves iguais, só pega a ultima, como se apenas atualizasse


#1)Len - Retorna a quantidade de chaves presentes no dicionario
# print(len(pessoa))

#2)Keys - Mostra as keys do dicionario, mas sai como dictkeys. Para isso, podemos as converter em tuplas ou listas
"""print(list(pessoa.keys()))

for chave in pessoa.keys():
    print(chave)"""

#3)Values - Mostra os valores do dicionário
"""print(list(pessoa.values()))

for valor in pessoa.values():
    print(valor)"""

#4) Itens - Iteração com chave e valores
"""print(list(pessoa.items()))

for chave, valor in pessoa.items():
    print(chave, valor)"""

#5)setdefault - adiciona valor se a chave não existe. Se existir, o valor pardrão setado será desconsiderado
"""pessoa.setdefault('idade', None) Assim, deixar a idade em branco, será atribuído o valor 'None'(pode ser qualquer um que eu quiser), caso coloque, ficará o adicionado no cadastro
print(pessoa['idade'])"""

#6)Copy - Retorna uma cópia rasa (shallow copy)