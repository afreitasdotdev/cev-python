# Faça um programa que leia um número inteiro e mostre na tela a sua tabuada

valor = int(input('Digite um numero e veja sua tabuada: '))

um = valor * 1
dois = valor * 2
tres = valor * 3
quatro = valor * 4 
cinco = valor * 5 
seis = valor * 6 
sete = valor * 7
oito = valor * 8
nove = valor * 9
dez = valor * 10 

print(
    '{0} x 1 = {1}\n'
    '{0} x 2 = {2}\n'
    '{0} x 3 = {3}\n'
    '{0} x 4 = {4}\n'
    '{0} x 5 = {5}\n'
    '{0} x 6 = {6}\n'
    '{0} x 7 = {7}\n'
    '{0} x 8 = {8}\n'
    '{0} x 9 = {9}\n'
    '{0} x 10 = {10}\n'
    .format(valor, um, dois, tres, quatro, cinco, seis, sete, oito, nove, dez)
)































