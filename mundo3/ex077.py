# Crie um programa que tenha uma tupla com varias palavras (não usar
# acentos). Depois disso, voce deve mostrar, para cada palavra, quais
# são as suas vogais

palavras = ('abacaxi', 'banana', 'uva', 'ovo', 'pera')

for p in palavras:
    print(f'\nNa palavra {p}, temos: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(f'{letra.upper()}',end=' ')
print('\n')
