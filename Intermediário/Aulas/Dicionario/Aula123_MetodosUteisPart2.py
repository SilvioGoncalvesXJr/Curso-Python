p1 ={
    'nome': 'Silvio',
    'sobrenome': 'Gonçalves',
}
#Get retorna o valor existente da chave. Se não existir valor, retorna None, evitando um erro de exceção
#print(p1.get('nome'))

#Pop - Apaga um item com a chave especificada, só que de forma um pouco diferente do del
#Aqui ele apagada da lista, mas é possível pegar o valor apagado e transferi-lo para uma variável
#nome = p1.pop('nome')
#print(nome)
#print(p1)

#PopItem - Elimina a última chave do dicionário, fncionando da mesma forma do pop
# ultima_chave = p1.popitem()
# print(ultima_chave)
# print(p1)

#Update - Atualiza um dicionário com outro, de forma parecida com a atualização de um BD
# p1.update({
#     'nome': 'Novo valor',
#     'idade': 28,
# })
#OU
# p1.update(nome='Novo valor', idade=28)
#OU
# tupla = ('nome', 'Novo Valor'), ('idade', 28)
# p1.update(tupla)
#Ou
lista = [['nome', 'Novo Valor'], ['idade', 28]]
p1.update(lista)
print(p1)