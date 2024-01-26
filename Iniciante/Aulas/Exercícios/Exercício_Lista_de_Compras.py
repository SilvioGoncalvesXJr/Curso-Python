"""
Faça uma lista de compras com listas.
O usuário deve ter a possibilidade de inserir, apagar
e listar valores da sua lista.
Não permita que o programa quebre com erros de 
índices inexistentes na lista
"""

import time, os
lista = []

flag = True
while flag == True:
    opcao = input("Selecione uma opção:\n 1 - Inserir\n 2 - Apagar\n 3 - Listar\n 4 - Sair\n")
    
    if opcao == '1':
        item = input("O que deseja inserir?")
        lista.append(item)
        print("Item adicionado com sucesso")
        time.sleep(2)
        os.system('cls')
    
    elif opcao == '2':
        # print(lista)
        # valor = input("O que deseja pagar da lista?")
        # if valor in lista:
        #     lista.remove(valor)
        #     print("item apagado com sucessoAS")
        # else:
        #     print("Valor não encontrado")
        if len(lista) == 0:
            print("Lista vazia. Por favor, adicione itens antes")
            time.sleep(2)
            os.system('cls')
        else:    
            for item in enumerate(lista):
                print(item)
            indice = int(input("Qual o índice do item que deseja excluir? Ex. 1, 2, 3, por exemplo\n"))
            try:
                del lista[indice]
                #Aqui, tentei usar a função delete(), mas não deu certo pq ela só funciona por valor
                #Já o del remove por index propriamente
                print("Removido com sucesso")
            except:
                print("Valor não identificado. Por favor, tente novamente")
            time.sleep(2)
            os.system('cls')
    
    elif opcao == '3':
        for item in enumerate(lista):
            print(item)
        time.sleep(4)
        os.system('cls')
    
    elif opcao == '4':
        print('Obrigado')
        flag = False
        time.sleep(2)
        os.system('cls')
    else:
        print('Opção inválida. Escolha um valor válida.')
        time.sleep(2)