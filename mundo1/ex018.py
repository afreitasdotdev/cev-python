# Faça um programa que leia um ângulo qualquer e mostre na tela
# o valor do seno, cosseno e tangente desse angulo

from math import cos, sin, tan, radians

ang = int(input('Digite o angulo: '))
angCos = cos(radians(ang))
angSen = sin(radians(ang))
angTan = tan(radians(ang))

print('Para o angulo {}, os valores são: \n'
'\n'
'Cosseno: {:.2f}\n'
'Seno: {:.2f}\n'
'Tangente: {:.2f}\n'.format(ang, angCos, angSen, angTan))
