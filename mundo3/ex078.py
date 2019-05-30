# Faça um programa que leia 5 valores numericos e guarde-os em
# uma lista. No final, mostre qual foi o maior e o menor valor
# digitado e as respectivas posições na lista.

lista = []
maior = 0
menor = 0
contador = 0

for i in range(0,5):
    numero = int(input('Digite um numero: '))
    lista.append(numero)
    if contador == 0: 
        maior = numero
        menor = numero
        contador += 1
    else: 
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

print(f'Foram digitados os numeros: {lista}')
print(f'O maior valor digitado foi {maior} nas posições: ', end='')
for indice, valor in enumerate(lista):
    if lista[indice] == maior:
        print(f'{indice}...', end='')
print()
print(f'O menor valor foi {menor} nas posições: ', end='')
for indice, valor in enumerate(lista):
    if lista[indice] == menor:
        print(f'{indice}...', end='')
print()
