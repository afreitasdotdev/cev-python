# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo sálario com 15% de aumento

salarioAtual = float(input('Digite o salario atual: '))
salarioAumento = float((salarioAtual / 100) * 115)

print('Com o salario atual de {}, seu funcionario \
passaria a receber {:.2f} com 15% de aumento'.format(salarioAtual, salarioAumento))
