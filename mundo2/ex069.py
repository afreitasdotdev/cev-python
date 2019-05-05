# Crie um programa que leia a idade e o sexo de varias pessoas. 
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário 
# quer ou não continuar. No final, mostre: 
    # a) Quantas pessoas tem mais de 18 anos
    # b) Quantos homens foram cadastrados 
    # c) Quantas mulheres tem menos de 20 anos 

mais18 = 0
homens = 0
mulheres20 = 0

while True:
    
    idade = int(input('Digite a idade: '))
    sexo = ' '
    
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo M/F: ')).upper()

        if sexo == 'M':
            homens += 1
        if idade >= 18:
            mais18 += 1
        if sexo == 'F' and idade < 20:
            mulheres20 += 1

    continua = ' '
    while continua not in 'SN':
        continua = input('Quer continuar [S/N]? ').upper()

    if continua == 'N':
        break

print(f'{homens} homens foram cadastrados.')
print(f'{mais18} pessoas tem mais de 18 anos.')
print(f'{mulheres20} mulheres tem menos de 20 anos.')