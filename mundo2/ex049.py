# Refaça o desafio 9 mostrando a tabuada de um numero que o usuario
# escolher, só que agr utilizando um laço for

valor = int(input('Por favor, informe um numero:'))

for i in range(1,11):
    print('{} * {} = {}'.format(valor,i,(valor*i)))