# Faça um programa que leia nome e peso de varias pessoas, guardando tudo em 
# uma lista. No final, mostre:
# a) Quantas pessoas foram cadastradas
# b) Uma listagem com as pessoas mais pesadas.
# c) Uma listagem com as pessoas mais leves.

cadastros = list()
pessoas = list()
qtdePessoas = 0
maisLeve = []
maisPesado = []

while True:
    nome = str(input('Digite o nome: '))
    peso = float(input('Digite o peso: '))
    pessoas.append(nome)
    pessoas.append(peso)
    cadastros.append(pessoas[:])
    pessoas.clear()
    qtdePessoas += 1

    continua = input('Deseja continuar? S/N ').upper()
    if continua == 'N':
        break

for pessoa,peso in cadastros:
    print(pessoa, peso)
    if len(maisLeve) == 0:
        maisLeve.append(nome)
        maisLeve.append(peso)


print(maisLeve)
#print(f'Foram cadastradas {qtdePessoas} pessoas.')
#print(f'{leves} foram os mais leves com {pesoLeve}')