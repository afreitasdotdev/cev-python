# Crie um programa que vai ler varios numeros e colocar
# em uma lista. Depois disto, mostre: 
# A) Quantos numeros foram digitados
# B) A lista de valores ordenada de forma decrescente
# C) Se o valor 5 foi digitado e esta ou não na lista.

lista = []
contador = 0
tem5 = 0

while True:
    numero = int(input('Digite um valor: '))
    if numero != '':
        lista.append(numero)
        contador += 1
    if numero == 5:
        tem5 += 1
    continua = input('Deseja continuar [S/N]? ').upper()
    if continua == 'N':
        break

lista.sort(reverse=True)
print(f'Os valores inseridos em ordem decrescente são: {lista}')
print(f'Foram inseridos {contador} numeros')
print(f'O numero 5 foi digitado {tem5} vezes')