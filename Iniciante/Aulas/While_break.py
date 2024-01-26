# condicao = True

# while condicao:
#     nome = input("Qual o seu nome?")
#     print(f"Seu nome é {nome}")

#     if nome == "sair":
#         break
# print("Programa Encerrado")

"""
Essa é uma boa forma de criar um menu, iniciando com uma condição
fixa e permitir sua alteração no decorrer do loop, como 
pode ser observado no exemplo a cima, na qual cada if seria uma opção.
"""
# ________________________________________________________________
"""Uma ferramenta muito utilizada, principalmente nos loops, são os operadores aritméticos
Temos: 
+= acrescenta pela quantidade indicada
-= diminui pela quantidade indicada
*= multiplica pela quantidade indicada
/= divide pela quantidade indicada
//= divisão inteira pela quantidade indicada
**= potenciação pela quantidade indicada
%= modulo pela quantidade indicada
"""
contador = 0

while contador < 10:
    contador += 1
    print(contador)
print("Acabou")