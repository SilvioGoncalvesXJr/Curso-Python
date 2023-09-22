"""Faça um jogo para o usuário adivinhar qual a palavra secreta.
Você irá propor uma palavra secreta qualquer e vai dar a 
possibilidade para o usuário digitar apenas 1 letra.
-Quando o usuário digitar uma letra, você irá conferir se a mesma está na palavra secreta.
-Se estiver, exiba a letra
-Se não estiver, exiba *
Faça a contagem de tentativas do seu usuário"""

# palavraSecreta = "CEARA"
# contador = 0
# inicio = 0

# while inicio == 0:
    
#     escolha = int(input("Deseja chutar uma letra (1) ou tentar acertar a palavra (2)?"))
    
#     if escolha == 1:
#         tentativa = input("Informe uma letra da palavra secreta: ").upper
        
#         if tentativa in palavraSecreta:
#             print(f"A letra que escolheu {tentativa} está na palavra secreta")
#         else:
#             print("Errado '*'")
            
#     if escolha == 2:
#         tentativa_palavra = input("Qual é a palavra secreta?").upper
#         if tentativa_palavra == palavraSecreta:
#             print(f"Você acretrou! A palavra secreta é {palavraSecreta}")
#             inicio += 1
#         else:
#             print(f"{tentativa_palavra} não é a palavra secreta")
    
#     contador += 1       

import os #lib que permite acionar um comando no terminal. Aqui, está para usar o clear

palavra_secreta = 'perfume'
letras_acertadas = ''
numero_tentativas = 0

while True:
    letra_digitada = input('Digite uma letra: ')
    numero_tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print('Palavra formada:', palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('cls')
        print('VOCÊ GANHOU!! PARABÉNS!')
        print('A palavra era', palavra_secreta)
        print('Tentativas:', numero_tentativas)
        letras_acertadas = ''
        numero_tentativas = 0