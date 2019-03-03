# Desenvolva um programa que leia seis numeros inteiros e apenas
# mostre a soma apenas daqueles que forem pares. Se o valor digitado
# for impar, desconsidere-o

soma = 0

for i in range(1,7):
    valor = int(input('Digite um numero: '))
    if valor % 2 == 0:
        soma += valor
print(soma)