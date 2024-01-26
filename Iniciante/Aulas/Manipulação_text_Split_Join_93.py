"""
split - divide uma string
strip - retira os espaços
join - une uma string
"""

frase = '  Olha só que    , coisa interessante'
lista_frases_cruas = frase.split(',')
print(lista_frases_cruas)

#É uma boa prática não alterar a informação raiz, para caso deseja acessá-la posteriormente
#então associamos a outra variável, por mais que deixe o código um pouco mais extenso 

lista_frases = []
for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip())

print(lista_frases)

frases_unidas = ', '.join(lista_frases)
print(frases_unidas)