# Minha resolução

nome = input("Qual o seu nome?").upper()

tamanho_nome = len(nome)
print(tamanho_nome)

i = 0
nome_iteravel = []

while i < tamanho_nome:
    nome_iteravel += nome[i] + '*'
    i += 1
print(nome_iteravel)


# Resolução Aula
"""
nome = 'Luiz Otávio'

indice = 0
novo_nome = ''

while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1
novo_nome += '*'
print(novo_nome)
"""