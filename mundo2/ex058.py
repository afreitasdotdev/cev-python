# Melhore o jogo do Desafio 028 onde o computador
# vai pensar em um numero entre 0 e 10. Só que agora
# o jogador vai tentar adivinhar até acertar, mostrando
# no final quantos palpites foram necessarios para vencer.

import random 

geraNum = (random.randint(0,10))
userNum = ''
vezes = 0
while not userNum == geraNum:
    userNum = int(input('Digite um numero e veja sua sorte: '))
    if userNum == geraNum:
        vezes += 1
        print('Você acertou. O Numero pensado foi {}. Voce precisou de {} tentativas'.format(geraNum, vezes))
    elif userNum != geraNum:
        vezes += 1
        print('Você errou. Tente de novo!')

