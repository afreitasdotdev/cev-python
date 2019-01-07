# Faça um programa que leia um numero de 0 a 9999  e mostre na tela cada
# um dos seus separadores
# EX: Digite 1834
# unidade: 4
# dezena: 3
# centena: 8
# milhar: 1

numero = input('Digite um numero:')

print("""
Unidade: {}
Dezena: {}
Centena: {}
Milhar: {}
""".format(numero[3], numero[2], numero[1], numero[0]))