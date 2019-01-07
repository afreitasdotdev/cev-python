# Escreva um programa que pergunte a quantidade de KM rodado, por um carro alugado
# e quantos dias ele permaneceu locado
# Valor por diaria = 60 R$
# Valor por KM rodado = 0,15 R$ 
# Calcule o preço a pagar 

dias = float(input('Por favor, informe quantos dias o carro permaneceu locado: '))
kms = float(input('Quantos kms foram rodados: '))

calcDia = float((dias * 60))
calcKM = float((kms * 0.15))
total = float((calcDia + calcKM))

print('O valor a ser pago por dia é de R$ {}, considerando R$ 60/diária'.format(calcDia))
print('O valor a ser pago por km é de R$ {}, considerando R$ 0,15/km rodado'.format(calcKM))
print('O valor total a ser pago é de R$ {}'.format(total))
