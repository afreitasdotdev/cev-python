# Crie um programa que leia o ano de nascimento de sete pessoas. 
# No final, mostre quantas pessoas ainda não atingiram a maioridade
# e quantas ja são maiores

maiores = 0
menores = 0

for i in range(1,8):
    ano = int(input('Digite o ano de nascimento: '))
    idade = (2019 - ano)
    if idade > 18:
        maiores += 1
    else:
        menores += 1

print('{} são menores e {} são maiores'.format(menores, maiores))