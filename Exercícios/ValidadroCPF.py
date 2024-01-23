
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




# cpf_enviado_usuario = '74682489070'
# nove_digitos = cpf_enviado_usuario[:9]
# contador_regressivo_1 = 10

# resultado_digito_1 = 0
# for digito in nove_digitos:
#     resultado_digito_1 += int(digito) * contador_regressivo_1
#     contador_regressivo_1 -= 1
# digito_1 = (resultado_digito_1 * 10) % 11
# digito_1 = digito_1 if digito_1 <= 9 else 0

# dez_digitos = nove_digitos + str(digito_1)
# contador_regressivo_2 = 11

# resultado_digito_2 = 0
# for digito in dez_digitos:
#     resultado_digito_2 += int(digito) * contador_regressivo_2
#     contador_regressivo_2 -= 1
# digito_2 = (resultado_digito_2 * 10) % 11
# digito_2 = digito_2 if digito_2 <= 9 else 0

# cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'

# if cpf_enviado_usuario == cpf_gerado_pelo_calculo:
#     print(f'{cpf_enviado_usuario} é válido')
# else:
#     print('CPF inválido')