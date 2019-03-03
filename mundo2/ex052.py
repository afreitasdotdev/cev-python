# Faça um programa que leia um numero inteiro e diga se ele é ou
# não um numero primo

numero = int(input('Insira um numero: '))
total = 0

for i in range(1, numero + 1):
    if numero % i == 0:
        total += 1

if total == 2: 
    print('NUMERO PRIMO')

else: 
    print('NAO PRIMO')
