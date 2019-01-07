# Faça um programa que leia o nome completo de uma pessoa, mostrando
# em seguida o primeiro e o ultimo nome separadamente
# Ex: Nome: Ana Maria de Souza
# Primeiro: Ana
# Ultima: Souza

nome = input('Digite o nome: ').strip()

separa = nome.split()

print('O nome ficará: {} {}'.format(separa[0], separa[-1]))