# Escreva um programa que leia um numero N inteiro qualquer e mostre na tela os N
# primeiros elementos de uma sequencia de Fibonacci.
# Ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8

qtde = int(input('Quantos termos vc quer mostrar?'))

contador = 0 
termo1 = 0
termo2 = 1

print('{} -> {}'.format(termo1,termo2), end='')

contador = 3 
while contador <= qtde:
    termo3 = termo1 + termo2
    termo1 = termo2
    termo2 = termo3
    print(' -> {}'.format(termo3), end='')
    contador += 1
