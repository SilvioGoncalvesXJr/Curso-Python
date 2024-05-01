#Manipulação de chaves e valores em dicionário
pessoa = {}

chave = 'nome'
#Isso é chamado de chave dinâmica

pessoa[chave] = 'Luiz Otávio'
pessoa['sobrenome'] = 'Miranda'
print(pessoa)

print(pessoa[chave])

pessoa[chave] = 'Maria'

del pessoa['sobrenome']
print(pessoa)
print(pessoa['nome'])

#Se por acaso eu queira acessar uma chave inexistente, como a sobrenome apagada, dara erro de exceção e não executa o resto do codigo
#Para reverter isso, posso usar o try except ou através do método .get() padrão dos dicionarios, que retorna None como padrão.
#Como por ex.:
print(pessoa.get('sobrenome', 'Inexistente'))#Por padrão, o .get retorna um valor None se a chave não existir, mas posso alterar o output, colcando o inexistente, p.ex.
#ou
if pessoa.get('sobrenome') is None:
    print('Não existe')
else:
    print(pessoa['sobrenome'])