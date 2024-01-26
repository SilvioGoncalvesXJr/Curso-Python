# Meu código
# inicio = True

# while inicio:
#     nome = input("Olá, Qual o seu nome? ")
#     numero1 = int(input(f"Olá {nome}, este é um prototipo de calculadora. {nome}, por gentileza, informe 1 número: "))
#     numero2 = int(input(f"{nome}, agora diga outro número que deseje: "))
#     opcao = input(f"""Você escolheu {numero1} e {numero2}. Agora, qual operação deseja realizar?
#                     1 = Soma
#                     2 = Subtração
#                     3 = Multiplicação
#                     4 = Divisão por inteiro
#                     Escolha: """)
#     # Posso escrever frases inteiras ou comando inteiros em um único print, sem usar o comando de quebra de linhas
#     # apenas colocando 3 " no começo e 3 no final
#     if opcao == "1":
#             soma = numero1 + numero2
#             print(soma)
#             inicio = False
#             # break
#             # Pode parar tanto trocando o boolean quanto usando o break
#     elif opcao == "2":
#             subtracao = numero1 - numero2
#             print(subtracao)
#             inicio = False
#             # break
#     elif opcao == "3":
#             multiplicao = numero1 * numero2
#             print(multiplicao)
#             inicio = False
#             # break
#     elif opcao == "4":
#             divisao = numero1 / numero2
#             print(divisao)
#             inicio = False
#             # break
#     else:
#            print("Escolha a opção correta")
# ___________________________________________________________________________________________

while True:
    numero_1 = input("Digite um número: ")
    numero_2 = input("Digite outro número: ")
    operador = input("Digite o operador (=-/*): ")

    numeros_validos = None

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None
    
    if numeros_validos is None:
        print("Um ou ambos os números digitados são inválidos")
        continue

    operadores_permitidos = "=-/*"

    if operador not in operadores_permitidos:
        print("Operador inválido")
        continue

    print("Realizando sua conta. Confira o resultado abaixo: ")

    if operador == '+':
        print(num_1_float + num_2_float)
    elif operador == '-':
        print(num_1_float - num_2_float)
    elif operador == '/':
        print(num_1_float/num_2_float)
    elif operador == '*':
        print(num_1_float*num_2_float)
    else:
        print("Nunca deveria chegar aqui")
        
    sair = input("Quer sair? [s]im: ").lower().startswith('s')

    if sair is True:
        break
    