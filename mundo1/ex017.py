# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um 
# triangulo retangulo, calcule o mostre o comprimento da hipotenusa

from math import hypot

catOp = float(input('Digite o valor do cateto oposto: '))
catAd = float(input('Digite o valor do cateto adjacente: '))
hipo = hypot(catOp, catAd)

print('A hipotenusa dos triangulo é {:.2f}. Considerando:\n'
'\n'
'Cateto oposto: {}\n'
'Cateto adjacente: {}\n'.format(hipo, catOp, catAd))
