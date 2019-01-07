# Crie um programa que faça o computador jogar Jokenpo com vc
# tentar colocar emojis :P

import emoji
import random

computador = random.randint(1,3)

usuario = int(input(emoji.emojize("""
Vamos jogar Jokenpo?

Escolha sua "arma"

1) Pedra :chestnut:
2) Papel :page_facing_up:
3) Tesoura :scissors:
 
""")))

if usuario == 1 and computador == 1: 
    print(emoji.emojize(" Voce jogou :chestnut: e o computador :chestnut:"))
    print(emoji.emojize(" :raised_hand: HOUVE EMPATE"))
elif usuario == 1 and computador == 2:
    print(emoji.emojize(" Voce jogou :chestnut: e o computador :page_facing_up:"))
    print(emoji.emojize(" :thumbsdown: VOCE PERDEU"))
elif usuario == 1 and computador == 3:
    print(emoji.emojize(" Voce jogou :chestnut: e o computador :scissors:"))
    print(emoji.emojize(" :thumbsup: VOCE VENCEU"))

elif usuario == 2 and computador == 1: 
    print(emoji.emojize(" Voce jogou :page_facing_up: e o computador :chestnut:"))
    print(emoji.emojize(" :thumbsup: VOCE VENCEU"))
elif usuario == 2 and computador == 2:
    print(emoji.emojize(" Voce jogou :page_facing_up: e o computador :page_facing_up:"))
    print(emoji.emojize(" :raised_hand: HOUVE EMPATE"))
elif usuario == 2 and computador == 3:
    print(emoji.emojize(" Voce jogou :page_facing_up: e o computador :scissors:"))
    print(emoji.emojize(" :thumbsdown: VOCE PERDEU"))

elif  usuario == 3 and computador == 1: 
    print(emoji.emojize(" Voce jogou :scissors: e o computador :chestnut:"))
    print(emoji.emojize(" :thumbsdown: VOCE PERDEU"))
elif usuario == 3 and computador == 2:
    print(emoji.emojize(" Voce jogou :scissors: e o computador :page_facing_up:"))
    print(emoji.emojize(" :thumbsup: VOCE VENCEU"))
elif usuario == 3 and computador == 3:
    print(emoji.emojize(" Voce jogou :scissors: e o computador :scissors:"))
    print(emoji.emojize(" :raised_hand: HOUVE EMPATE"))


