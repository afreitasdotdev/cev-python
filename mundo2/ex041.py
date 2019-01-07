# A confederação de natação precisa de um programa que leia o ano de
# nascimento de um atleta e mostre sua categoria de acordo com a idade:
# Até 9 anos: Mirim
# Até 14 anos: Infantil
# Até 19 anos: Junior
# Até 20 anos: Sênior
# Acima: Master

import datetime

anoNasc = int(input('Digite o ano de nascimento: '))

idade = (datetime.date.today().year - anoNasc)

if idade < 9:
    print('Atleta de {} anos, categoria: Mirim'.format(idade))
elif idade >= 9 and idade < 14:
    print('Atleta de {} anos, categoria: Infantil'.format(idade))
elif idade >= 14 and idade < 19:
    print('Atleta de {} anos, categoria: Junior'.format(idade))
elif idade >= 19 and idade <= 20:
    print('Atleta de {} anos, categoria: Senior'.format(idade))
elif idade > 20: 
    print('Atleta de {} anos, categoria: Master'.format(idade))