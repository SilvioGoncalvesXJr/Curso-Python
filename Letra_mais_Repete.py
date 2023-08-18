frase = "O Python é uma lingagem de programação" \
"multiparadigma. O Python foi criado por Guido van Rossum"
#Essa barra invertida'\' serve para quebrar a linha, da mesma forma dos """

# i = 0
# quebraLetras = []
# while i < len(frase):
#     quebraLetras += frase[i]
#     if frase[i] == " ":
#         quebraLetras.remove(" ")
#     i += 1

# print(quebraLetras)
# resultadoQuebra = max(quebraLetras, key=quebraLetras.count)
# print(f" Na frase, o elemento que mais repete é o '{resultadoQuebra}'")
# ___________________________________________________________________________
i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == " ":
        i += 1
        continue

    qtd_apareceu_mais_vezes_atual = frase.count(letra_atual)

    if qtd_apareceu_mais_vezes < qtd_apareceu_mais_vezes_atual:
        qtd_apareceu_mais_vezes = qtd_apareceu_mais_vezes_atual
        letra_apareceu_mais_vezes = letra_atual
    
    i += 1

print('A  letra que aprareceu mais vezes foi '
      f'"{letra_apareceu_mais_vezes}" que apareceu '
      f'{qtd_apareceu_mais_vezes}x')