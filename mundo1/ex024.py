# Crie um programa que leia o nome de uma cidade e diga se ela
# começa ou nao com o nome "SANTO"

nome = str(input('Digite o nome da cidade:')).strip()

padroniza = nome.lower()

resultado = 'santo' in padroniza

print('O nome começa com Santo? {}'.format(resultado))