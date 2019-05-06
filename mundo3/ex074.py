# Crie um programa que vai gerar cinco numeros aleatorios e
# colocar em uma tupla. Depois disso, mostra a listagem de 
# numeros e tambem indique o menor e o maior valor que estão na tupla

import random

numeros = (random.randint(0,10), random.randint(0,10), random.randint(0,10), 
random.randint(0,10), random.randint(0,10))

print(f'''Numeros sorteados: {numeros}
Menor: {min(numeros)}
Maior: {max(numeros)}''')