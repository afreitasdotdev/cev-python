# Crie um programa que simule o funcionamento de um caixa eletronico. 
# No inicio, pergunte ao usuario qual será o valor sacado (numero int)
# e o programa vai informar quantas cedulas de cada valor serão entregues
# Considere que o caixa tem notas de 50, 20, 10 e 1

print('=' * 30)
print('{:^30}'.format('BANCO CEV'))
print('=' * 30)

saque = int(input('Quanto você quer sacar? R$ '))
maiorCed = 50
saldo = saque
qtdCed = 0

while True: 
    if saldo >= maiorCed:
        saldo -= maiorCed
        qtdCed += 1
    else:
        if qtdCed > 0:
            print(f'Total de {qtdCed} cédulas de R$ {maiorCed}')
        if maiorCed == 50:
            maiorCed = 20
            qtdCed = 0
        elif maiorCed == 20:
            maiorCed = 10
            qtdCed = 0
        elif maiorCed == 10:
            maiorCed = 1
            qtdCed = 0
        if saldo == 0:
            print('=' * 30)
            print('Volte Sempre')
            break
