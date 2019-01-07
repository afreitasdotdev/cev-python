# Faça um programa que leia um numero e mostre na tela seu sucessor e seu antecessor

entrada = int(input('Digite um número: '))

ant = entrada - 1
suc = entrada + 1

print('O número digitado {}, tem como seu sucessor {} e antecessor {}'.format(entrada, suc, ant))
