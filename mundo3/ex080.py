# Crie um programa onde o usuario possa digitar 5 valores
# numericos e cadastre-os em uma lista, ja na posição correta
# de inserção, sem usar o sort. No final, mostre a lista ordenada
# na tela.

numeros = []

for i in range(0,5):
    valor = int(input('Digite um valor: '))
    if i == 0 or valor > numeros[-1]: 
        numeros.append(valor)
        print(f'Adicionado na posição {i}')
    else: 
        pos = 0
        while pos < len(numeros):
            if valor <= numeros[pos]:
                numeros.insert(pos, valor)
                print(f'Adicionado na posição {pos}')
                break
            pos += 1

print(f'Lista de numeros digitados: ')
print(numeros)