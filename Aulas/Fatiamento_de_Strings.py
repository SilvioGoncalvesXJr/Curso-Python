"""
Fatiamento de Strings
012345678
Olá Mundo
-987654321
Fatiamento [i:f:p] [::]
'i = inicio; onde quer começar a fazer o datiamento'
'f = é o fim; indica até onde ir. 
Se for até o final (indicando uma posição a mais, viso que não mostra a última), deixa o espaço vazio, da mesma forma que no i'
'p = indica de quantos em quantos caracteres ele irá pula'
Obs.: a função 'len' retorna a quantidade de caracteres da str
"""
variavel = "Olá Mundo"
print(len(variavel))
print(variavel[0:len(variavel):1])
print(variavel[0:len(variavel):2])
print(variavel[::-1])
# Ao colocar esse '-1' Faz com que eu inverta minha string
print(variavel[-1:-10:-1])
# Mesma coisa aqui, porém, se quiser utilizar os marcadores, precisa usar as posições em negativo
print(variavel[-1:-10:-2])


