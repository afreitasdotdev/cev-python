# Escreva um programa que leia 2 numeros inteiros e compare-os, mostrando
# na tela, uma das mensagens: 
# O primeiro valor é maior
# O segundo valor é maior
# Não existe maior, os numeros são iguais

valor1 = int(input('Informe o primeiro valor: '))
valor2 = int(input('Informe o segundo valor: '))

if valor1 > valor2: 
    print('O primeiro valor ({}) é maior'.format(valor1))
elif valor2 > valor1: 
    print('O segundo valor ({}) é maior'.format(valor2))
elif valor2 == valor1:
    print('Não existe maior, ambos são iguais')
