""" No for, como é uma estrutura de repetição que nem o while,
é possível aplicar/utilizar algumas mecanicas/ferramentas que 
vimos anteriormente"""

for i in range(10):
    if i == 2:
        print('i é 2, pulando...')
        continue
    
    if i == 8:
        print('i é 8, seu else não executará')
        break
    
    for j in range(1,3): # Este for funciona como acrescentando a segunda cu=oluna, outro nível ao loop
        print(i,j)
        
else:
    print('For completo com sucesso')