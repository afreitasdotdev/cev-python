# Escreva um programa que faça o computador pensar em um numero de 0 a 5 
# e peça para o usuario tentar adivinhar qual o numero escolhido.
# O programa deverá escrever na tela se o usuario acertou ou nao.

import random 

geraNum = (random.randint(0,5))

userNum = int(input('Digite um numero e veja sua sorte: '))

if userNum == geraNum:
    print('Voce digitou {} e o numero escolhido foi {}! Parabéns, acertou.'.format(userNum, geraNum))
else:
    print('Voce digitou {} e o numero escolhido foi {}! Vc errou.'.format(userNum, geraNum))

print('Tente novamente')