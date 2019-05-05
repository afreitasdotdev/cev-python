# Faça um programa que leia o sexo de uma pessoa,
# mas só aceite os valores M ou F. Caso esteja errado,
# peça a digitação novamente até ter um valor correto

sexo = '1'

while not sexo in 'MmFf':
    sexo = input('Digite o seu Sexo [M/F]: ')

print('Acabou')