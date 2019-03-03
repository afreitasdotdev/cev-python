# Faça um programa que calcule a soma entre todos
# os numeros impares que são multiplos de tres e que
# se encontram no intervalo de 1 ate 500

soma = 0
for num in range(1,500):
    if num % 3 == 0 and num % 2 != 0:
        soma += num

print(soma)