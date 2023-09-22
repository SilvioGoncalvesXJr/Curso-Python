"""
Faça um programa que peça ao usuário para digitar um número inteiro, 
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, indorme que não é um número insteiro

Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
exiba a saudação apropriada. Ex.: Bom dia, boa tarde ou boa noite

Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras
ou menos escrita, dizer "Seu nome é curto", mas se tiver entre 5 e 6 letras,
escrever "Seu nome é normal", ou se for maior que 6, escreva "Seu nome é muito grande".
"""

# numero = int(input("Favor, informe um número inteiro: "))
# par_ou_impar = numero % 2
# inteiro = type(numero)
# print(inteiro)

# if par_ou_impar == 0:
#     print("Sei número é par")
# else:
#     print("Seu númro é impar")

# if inteiro == int:
#     print("É inteiro")
# else:
#     print("Não é inteiro")


"""
try:
    numero = int(input("Favor, informe um número inteiro: "))
    par_ou_impar = int(numero) % 2
    inteiro = type(numero)
    print(inteiro)

    if par_ou_impar == 0:
        print(f"O seu número {numero} é par")
    else:
        print(f"Seu número {numero} é impar")

    if inteiro == int:
        print("É inteiro")
    else:
        print("Não é inteiro")
except:
   print("Favor, usar números inteiros")


ou

entrada = input("Digite um número: ")

if entrada.isdigit():
    entrada_int = int(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = "impar"

    if par_impar:
        par_impar_texto = "par"
    print(f"O número {entrada_int} é {par_impar_texto}")
else:
    print("Você não digitou um número inteiro")
__________________________________________________________________________________________________
"""
# nome = input("Olá, qual o seu nome?")
# horario = float(input("Que horas são?"))

# if horario >= 0 and horario < 12:
#     print(f"Olá, {nome}. Bom dia!")
# elif horario >= 12 and horario < 18:
#     print(f"Olá, {nome}. Boa tarde!")
# else:
#     print(f"Olá, {nome}. Boa noite")

# ou

# entrada = input("Digite a hora em números inteiros: ")

# try:
#     hora = int(entrada)

#     if hora >= 0 and hora <= 11:
#         print("Bom dia")
#     elif hora >= 12 and hora <= 17:
#         print("Boa tarde")
#     elif hora >= 18 and hora <= 23:
#         print("Boa noite")

# except:
#     print("Por favor, digite apneas números inteiros")
# ___________________________________________________________________________________________________
nome = input("Qual o seu nome?")
tamanho_nome = len(nome)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print(f"{nome}, seu nome é muito pequeno")
    elif tamanho_nome > 4 and tamanho_nome <7:
        print(f"{nome}, seu nome é normal")
    else:
        print(f"{nome}, seu nome é muito grande")
else:
    print("Digite mais de uma letra")