"""Faça um jogo para o usuário adivinhar qual a palavra secreta.
Você irá propor uma palavra secreta qualquer e vai dar a 
possibilidade para o usuário digitar apenas 1 letra.
-Quando o usuário digitar uma letra, você irá conferir se a mesma está na palavra secreta.
-Se estiver, exiba a letra
-Se não estiver, exiba *
Faça a contagem de tentativas do seu usuário"""

import os

palavra_secreta = "CEARA"
letras_acertadas = ''
numero_tentativas = 0

while True:
    letra_digitada = input("Informe uma letra que deseja verificar: ").upper()
    numero_tentativas += 1
    
    if len(letra_digitada) > 1:
        print("Favor, digite apenas uma letra, como solicitado")
        continue
    
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada
        
    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    
    print(f"Palavra formada: {palavra_formada}")
    
    if palavra_formada == palavra_secreta:
        os.system("cls")  
        print("Você ganhou! Parabéns!")
        print(f"A palavra secreta é {palavra_secreta}")
        print(f"Acertou em {numero_tentativas} tentativas")
        menu_final = input("escolha as opções:\n Deseja jogar novamente?(1)\n Deseja encerrar o jogo?(2) ")
        
          
        if menu_final == '1':
            letras_acertadas = ''
            numero_tentativas = 0            
        
        if menu_final == '2':
            break
        
        # while menu_final != str(1) or menu_final != str(2):
        #     print("-" * 10)
        #     print("Escolha as opções corretas")
        #     print("-" * 10)
        #     menu_final = input("escolha as opções:\n Deseja jogar novamente?(1)\n Deseja encerrar o jogo?(2) ")
        #     print(type(menu_final))
        # Fica dando pau, pq sempre cai no loop e não sai













    

# import os #lib que permite acionar um comando no terminal. Aqui, está para usar o clear

# palavra_secreta = 'perfume'
# letras_acertadas = ''
# numero_tentativas = 0

# while True:
    # letra_digitada = input('Digite uma letra: ')
#     numero_tentativas += 1

#     if len(letra_digitada) > 1:
#         print('Digite apenas uma letra.')
#         continue

#     if letra_digitada in palavra_secreta:
#         letras_acertadas += letra_digitada

#     palavra_formada = ''
#     for letra_secreta in palavra_secreta:
#         if letra_secreta in letras_acertadas:
#             palavra_formada += letra_secreta
#         else:
#             palavra_formada += '*'

#     print('Palavra formada:', palavra_formada)

#     if palavra_formada == palavra_secreta:
#         os.system('cls')
#         print('VOCÊ GANHOU!! PARABÉNS!')
#         print('A palavra era', palavra_secreta)
#         print('Tentativas:', numero_tentativas)
#         letras_acertadas = ''
#         numero_tentativas = 0