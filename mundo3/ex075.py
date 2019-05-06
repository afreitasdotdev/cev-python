# Desenvolva um programa que leia quatro valores pelo
# teclado e guarde-os em uma tupla. No final mostre: 
# a) quantas vezes apareceu o valor 9
# b) Em que posição foi digitado o primeiro valor 3
# c) Quais os numeros foram pares

val1 = int(input('Digite o 1º valor: '))
val2 = int(input('Digite o 2º valor: '))
val3 = int(input('Digite o 3º valor: '))
val4 = int(input('Digite o 4º valor: '))
val5 = int(input('Digite o 5º valor: '))

conj = (val1, val2, val3, val4, val5)

#qtd9 = 0
#par = 0
#for numero in conj:
#    if numero == 9:
#        qtd9 +=1

#print(f'Digitaram nove {qtd9} vezes')
print(f'Digitaram nove {conj.count(9)} vezes')
if 3 in conj:
    print(f'O primeiro 3 aparece na posição {conj.index(3)}')
print('Os valores pares são: ', end='')
for num in conj:
    if num % 2 == 0:
        print(f'{num}', end=' ')
print()