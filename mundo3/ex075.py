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

qtd9 = 0
par = 0
for numero in conj:
    if numero == 9:
        qtd9 +=1
    

print(f'Digitaram nove {qtd9} vezes')