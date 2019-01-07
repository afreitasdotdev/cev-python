# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto

valor = float(input('Digite o valor do produto: '))
novoValor = float((valor / 100) * 95)
desconto = float(valor - novoValor)

print('O seu produto com valor original de R$ {}, fica apenas R$ {:.2f} com 5% de desconto'.format(valor, novoValor))
print('Seu desconto foi de {:.2f}'.format(desconto))

