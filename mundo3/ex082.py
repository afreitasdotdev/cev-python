# Crie um programa que vai ler varios numeros e colocar em uma lista
# Depois disso, crie duas listas extras que vão conter apenas os 
# valores pares e os valores impares, digitados respectivamente.
# No final, mostre o conteudo das tres listas geradas
# Separar os numeros no final, não no momento de inserção

numeros = list()

while True: 
    valor=int(input('Digite um número: '))
    numeros.append(valor)
    continua=input('Deseja continuar? S/N ').upper()

    if continua == 'N':
        break


pares = []
impares = []

for num in numeros:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print(f'Voce digitou os números: {numeros}')
print(f'Os valores impares foram {impares}')
print(f'Os valores pares foram {pares}')