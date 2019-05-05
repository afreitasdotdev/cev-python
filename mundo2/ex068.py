# Faça um programa que jogue par ou impar com o computador. O jogo
# só sera interrompido quando o jogador perder, mostrando total de 
# vitorias consecutivas que ele conquistou no final do jogo.

import random

contador = 0

while True:
    computador = int(random.randint(1,10))
    jogador = int(input('Digite seu numero: '))
    lado = input('Par ou Impar: [P/I] ').upper()
    soma = (computador + jogador)
    print('='*15)
    if lado in 'Pp':

        if soma % 2 == 0:
            print(f'Você jogou {jogador} e o computador {computador}.')
            print('Parabéns!! Você ganhou. Vamos jogar de novo.')
            contador += 1
            print('='*15)
        if soma % 2 != 0:
            print(f'Você jogou {jogador} e o computador {computador}.')
            print('Que pena!! Você perdeu. Tente de novo!!')
            print(f'Voce teve {contador} vitórias consecutivas')
            print('='*15)
            break
    
    elif lado in 'Ii':

        if soma % 2 != 0:
            print(f'Você jogou {jogador} e o computador {computador}.')
            print('Parabéns!! Você ganhou. Vamos jogar de novo.')
            contador += 1
            print('='*15)
        if soma % 2 == 0:
            print(f'Você jogou {jogador} e o computador {computador}.')
            print('Que pena!! Você perdeu. Tente de novo!!')
            print(f'Voce teve {contador} vitórias consecutivas')
            print('='*15)
            break