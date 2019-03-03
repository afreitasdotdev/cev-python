# Faça um programa que leia o peso de cinco pessoas. No final, mostre
# qual foi o maior e o menor peso lidos

listaPeso = []

for i in range(1,6):
    novoPeso = int(input('Digite o seu peso: '))
    listaPeso.append(novoPeso)

print(max(listaPeso))