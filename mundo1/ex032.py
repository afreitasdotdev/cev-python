# Faça um programa que leia um ano qualquer e diga se ele é um ano bissexto.

ano = int(input('Informe um ano: '))

div4 = (ano % 4 == 0)
div100 = (ano % 100 == 0)
div400 = (ano % 400 == 0)

if div4 == True and div100 == False: # sim
    print('O ano {} é bissexto'.format(ano))
if div4 == True and div100 == True: #nao
    print('O ano {} não é bissexto'.format(ano))
if div100 == True: # nao
    print('O ano {} não é bissexto'.format(ano))
if div4 == False and div400 == True: # sim
    print('O ano {} é bissexto'.format(ano))
if div4 == False and div100 == False and div400 == False: # nao
    print('O ano {} não é bissexto'.format(ano))