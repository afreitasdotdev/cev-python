# Crie um programa que leia um numero real qualquer pelo teclado e mostre na tela sua porção inteira
# Ex: 6.127 tem a parte inteira 6

from math import trunc

num = float(input('Digite um numero: '))
print('O numero {}, tem {} na sua parte real'.format(num,trunc(num)))
