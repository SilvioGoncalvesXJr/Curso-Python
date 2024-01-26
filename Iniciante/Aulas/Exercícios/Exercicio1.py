"""
Peça ao usuário para digitar seu nome e, depois, sua idade
Se nome e idade forem digitados, Exiba:
    Seu nome é {nome}
    Seu nome invertido é {nome invertido}
    Se nome contém ou não espaços
    Seu nome tem {n} letras
    A primeira letra do seu nome é {letra}
    A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade, exiba:
    "Desculpe, você deixou campos vazios"
"""

nome = input("Qual o seu nome? ")
idade = input("Qual a sua idade? ")
nome_invertido = nome[::-1]
print(len(nome), len(idade))


if len(nome) and len(idade) != 0:
    print(f"Seu nome é {nome}")
    print(f"Seu nome invertido é {nome_invertido}")
    if " " in nome:
        print("Seu nome contém espaços")
    else:
        print("Seu nome não tem espaços")
    print(f"Seu nome tem {len(nome)} letras")
    print(f"A primeira letra do seu nome é '{nome[0]}'")
    print(f"A última letra do seu nome é '{nome_invertido[0]}'")
else:
    print("Desculpe, você deixou campos vazios")

"""Gabarito
nome = input("Qual o seu nome? ")
idade = input("Qual a sua idade? ")

if nome and idade:(Aqui poderia deixar assim, visto que se não tiver nada, estaria como False, e só passa se for True, quando tem)
    print(f"Seu nome é {nome}")
    print(f"Seu nome invertido é {nome::-1}")
    if " " in nome:
        print("Seu nome contém espaços")
    else:
        print("Seu nome não tem espaços")
    print(f"Seu nome tem {len(nome)} letras")
    print(f"A primeira letra do seu nome é '{nome[0]}'")
    print(f"A última letra do seu nome é '{nome[-1]}'")
else:
    print("Desculpe, você deixou campos vazios")
"""