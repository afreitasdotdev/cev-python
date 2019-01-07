# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimitros

valor = float(input('Insira o valor em metros: '))

cent = valor * 100
mili = valor * 1000

print('{}m equivale a {} centimetros ou {} milimetros'.format(valor, cent, mili))
