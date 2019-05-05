# Criei um programa que leia o nome e o preço de varios
# produtos. O programa deverá perguntar se o usuário vai 
# continuar. No final mostre: 

# a) Qual é o total gasto na compra
# b) Quantos produtos custam mais de R$ 1000
# c) Qual é o nome do produto mais barato.

totalGasto = 0
mais1000 = 0
nomeProdBarato = ' '
precoProdBarato = 0
contador = 0

while True:

    produto = input('Qual o nome do produto: ')
    preco = float(input('Digite o valor do produto: '))
    continua = ' '
    while continua not in 'SN':
        continua = input('Continuar S/N?: ').upper()
        totalGasto += preco
        if preco > 999:
            mais1000 += 1
        if contador == 0:
            nomeProdBarato = produto
            precoProdBarato = preco
            contador += 1
        if contador != 0:
            if preco < precoProdBarato:
                nomeProdBarato = produto
                precoProdBarato = preco
    if continua == 'N':
        break

print(f'O total gasto foi de R$ {totalGasto}')
print(f'{mais1000} produtos custam mais de R$ 1000.00')
print(f'{nomeProdBarato} foi o produto mais barato. Custando R$ {precoProdBarato}')