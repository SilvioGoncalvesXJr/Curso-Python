'''Exercício - Sistema de perguntas e respostas
Estabele algumas perguntas já padronizadas, com alguns itens de possíveis respostas
e armazena a escolha do usuário, de forma a dizer se acertou ou errou.
Ao final, mostrar o score 'de 5 perguntas, acertou 3', por exemplo.
'''
import time, sys, os

perguntas = [
    {
        'Pergunta': 'Qual a minha comida preferida?',
        'Opções': ['Pizza', 'Baião', 'Cuzcuz', 'Hamburguer'],
        'Gabarito': 'Baião',
    },
    {
        'Pergunta': 'Qual a minha obra de Ficção Preferida?',
        'Opções': ['Game of Thrones', 'Senhor dos Aneis', 'One Piece', 'Naruto'],
        'Gabarito': 'One Piece',
    },
    {
        'Pergunta': 'Antes do Snoopy, eu tinha uma cadela, a Princesa. Qual a raça dela?',
        'Opções': ['Poodle', 'SRD', 'Salsicha', 'Pincher'],
        'Gabarito': 'Poodle',
    },
    {
        'Pergunta': 'Qual foi o ritmo da minha primeira aula de dança?',
        'Opções': ['Salsa', 'Samba', 'Bachata', 'Forró'],
        'Gabarito': 'Forró',
    },
    {
        'Pergunta': 'Qual estado da região norte do país que já visitei a trabalho?',
        'Opções': ['Amapá', 'Pará', 'Amazonas', 'Acre'],
        'Gabarito': 'Amapá',
    },
    {
        'Pergunta': 'Qual o ano em que nasci?',
        'Opções':['1994', '1995', '1996', '1997'],
        'Gabarito': '1995',
    },
    {
        'Pergunta': 'Agora, qual o mês?',
        'Opções': ['Setembro', 'Outubro', 'Novembro', 'Dezembro'],
        'Gabarito': 'Outubro',
    },
    {
        'Pergunta': 'Qual o dia do meu aniversário?',
        'Opções': ['27','17','07','16'],
        'Gabarito':'27',
    },
    {
        'Pergunta': 'Quando foi a primeira vez que eu disse que te amava?',
        'Opções': ['Na praia', 'Na minha casa', 'No meu carro', 'No banco do teu prédio'],
        'Gabarito': 'No meu carro',
    },
    {
        'Pergunta': 'Qual o nome do Motel que tivemos nossa primeira vez?',
        'Opções':['Perfume', 'Container', 'Le Chalet', 'Chalex'],
        'Gabarito': 'Perfume',
    }
]
def verificar(escolha):
    if escolha == '0' or escolha == '1' or escolha == '2' or escolha == '3':
        print('ok')
        return 'ok'
    else:
        print('Favor, escolher uma das opções apresentadas, entre 0 e 3')
        return 'Não ok'

print("Seja Bem Vinda ao jogo ao cara mais gostoso que já viu ;)")
# time.sleep(5)
print()
print('Porém, existe uma condição para participar. Se errar mais que 30% das respostas, vai fazer algo que eu queira')
# time.sleep(5)
print()
print('Mas, ao contrário, você terá o direito a pedir alguma coisa para mim')
# time.sleep(5)
print()
concordar = input('Aceita? kkkk (s/n)')
print()

if concordar == 's':
    print('EITCHAAAAA. VAMOS LA KKKKK')
    # time.sleep(5)
    os.system('cls')
else:
    print("Ta bom então :')")
    time.sleep(5)
    os.system('cls')
    sys.exit()

for pergunta in perguntas:
    print(pergunta.get('Pergunta'))
    for itens in pergunta:
        print(pergunta.get('Opções'))


        
