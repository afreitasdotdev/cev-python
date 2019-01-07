# Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome

nome = str(input('Digite o nome completo: ')).strip()

padroniza = nome.lower()
verifica = padroniza.find('silva')

checa = 'silva' in padroniza

print('O nome digitado possui Silva? {}'.format(checa))