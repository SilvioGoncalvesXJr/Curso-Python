
lista = []
listaLimpa = []
listaint = []
listaintAtt = []

cpf = input("Informe um cpf válido: ")

def gerarCpf(casa):

    for i in cpf:
            lista.append(i)
    # print(lista)

    for i in lista:
        if i == '.' or i == '-':
            lista.remove(i)
    listaLimpa = lista
    # print(listaLimpa)

    if casa == 1:
        listaLimpa.pop()
        listaLimpa.pop()
        
        for i in listaLimpa:
            listaint.append(int(i))
        # print(listaint)

        valor = 10
        for i in listaint:
            listaintAtt.append(i*valor)
            valor -= 1
        # print(listaintAtt)

        valores = 0
        for i in listaintAtt:
            valores += i
        # print(valores)

        valores = valores * 10
        # print(valores)

        valores = valores % 11
        # print(valores)

        primeiro_digito = 0 if valores > 9 else valores

        print(f'O primeiro dígito é {primeiro_digito}')

    elif casa == 2:
        
        listaLimpa.pop()
    
        for i in listaLimpa:
            listaint.append(int(i))
        # print(listaint)

        valor = 11
        for i in listaint:
            listaintAtt.append(i*valor)
            valor -= 1
        # print(listaintAtt)

        valores = 0
        for i in listaintAtt:
            valores += i
        # print(valores)

        valores = valores * 10
        # print(valores)

        valores = valores % 11
        # print(valores)

        segundo_digito = 0 if valores > 9 else valores

        print(f'O segundo dígito é {segundo_digito}')
        listaLimpa.append(segundo_digito)
        print('CPF válido' if lista == listaLimpa else 'CPF Inválido')
        
        

gerarCpf(1)
lista = []
listaint = []
listaintAtt = []
gerarCpf(2)




