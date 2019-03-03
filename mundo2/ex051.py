# Desenvolva um programa que leia o primeiro termo e a razão
# de uma PA. No final, mostre os 10 primeiros termos dessa progressao

primeiro = int(input('Insira o primeiro valor: '))
razao = int(input('Insira a razão da sua PA:'))

decimo = primeiro + (10 -1) * razao

for i in range(primeiro, decimo, razao):
    print('{} '.format(i), end='-> ')

print('ACABOU')
