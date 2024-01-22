'''
Operação ternária (condicional de uma linha)
Estrutura => <valor> if <condição> else <outro valor>
'''

condicao = 10 == 10
variavel = 'Valor' if condicao else 'Outro Valor'
print(variavel)

condicao = 10 == 11
variavel = 'Valor' if condicao else 'Outro Valor'
print(variavel)

digito = 9
novo_digito = 0 if digito > 9 else digito
print(novo_digito)