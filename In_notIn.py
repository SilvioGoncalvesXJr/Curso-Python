nome = input("Diga o seu nome: ").upper()
encontrar = input("O que deseja encontrar? ").upper()

if encontrar in nome:
    print(f"{encontrar} está em {nome}")
else:
    print(f"{encontrar} não está em {nome}")