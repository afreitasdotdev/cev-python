# Crie um programa que leia um numero inteiro e mostre na tela se
# ele é PAR ou IMPAR

num = int(input('Digite um numero: '))

if num % 2 == 0:
    print('O numero {} é par'.format(num))
else:
    print('O número {} é impar'.format(num))
