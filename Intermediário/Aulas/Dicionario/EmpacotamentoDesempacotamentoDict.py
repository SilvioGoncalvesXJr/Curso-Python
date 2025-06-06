# Empacotamento e desempacotamento de dicionários
a, b = 1, 2
a, b = b, a
# print(a, b)


# (a1, a2), (b1, b2) = pessoa.items()
# print(a1, a2)
# print(b1, b2)

# for chave, valor in pessoa.items():
#     print(chave, valor)

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}

pessoas_completa = {**pessoa, **dados_pessoa}
#Esses dois '*' faz com que seja realizado o desempacotamento, permitindo extrair as chaves/valor existentes e passar para outro dicionário
# print(pessoas_completa)

'''
args e kwargs
args - argumentos não nomeados variáveis
kwargs = keyword arguments - Argumentos Nomeados
'''

def mostro_argumentos_nomeados(*args, **kwargs):#No kwargs, se usa os dois '*'
    print('Não nomeados', args)

    for chave, valor in kwargs.items():
        print(chave, valor)

mostro_argumentos_nomeados(1, 2, nome='Joana', qualquer_coisa= 123)
mostro_argumentos_nomeados(**pessoas_completa)

configuracoes = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
}
mostro_argumentos_nomeados(**configuracoes)