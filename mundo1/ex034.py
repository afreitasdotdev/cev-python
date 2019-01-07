# Escreva um programa que pergunte o salario de um funcionario e calcule o aumento.
# para salarios superiores a R$ 1.250, aumento de 10%
# para salarios inferiores ou iguais, aumento de 15%.

sal = float(input('Digite o salario e veja seu aumento: '))

if sal <= 1250:
    aumento = (sal / 100 * 115)
    print('Seu novo salario {}'.format(aumento))
else:
    aumento = (sal / 100 * 110)
    print('Seu novo salario {}'.format(aumento))