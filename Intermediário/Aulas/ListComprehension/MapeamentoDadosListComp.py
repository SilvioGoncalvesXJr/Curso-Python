produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]

novos_produtos = [
    produto
    for produto in produtos
]

print(*novos_produtos, sep='\n')

novos_produtos2 = [
    {**produto, 'preco': produto['preco'] * 1.05}#Permite pegar os valores e colocar em nova lista, desempacotando, além de manipular valores específicos
    for produto in produtos
]
print(novos_produtos2)

novos_produtos3 = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}#É possível incluir um if/else statment aqui para manipular apenas valores específicos
    for produto in produtos
]
print(novos_produtos3)