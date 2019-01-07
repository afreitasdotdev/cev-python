# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome, com tudo em MAIUSCULAS
# O nome, com tudo em minusculas
# Quantas letras ao todo (sem considerar espaços)
# Quantas letras tem o primeiro nome

nome = str(input('Digite o seu nome completo: ')).strip()

print('Analisando seu nome...')
print('Seu nome em maiusculas é {}'.format(nome.upper()))
print('Seu nome em minusculas é {}'.format(nome.lower()))
print('Seu nome tem {} letras'.format(len(nome) - nome.count(' ')))

separa = nome.split()

print('Seu primeiro nome tem {} letras'.format(len(separa[0])))