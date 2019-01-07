# Elabore um programa que calcule o valor a ser pago de um produto considerando
# o preço normal e sua forma de pagamento
# a vista / dinheiro / cheque = 10% de desconto
# a vista no cartão = 5% de desconto
# em até 2x no cartão = preço normal
# 3x ou mais no cartão = 20% de juros 

produto = float(input('Forneça o preço do produto: '))
formaPgto = int(input("""
Qual a forma de pagamento? 

1) A vista / dinheiro / cheque = 10% de desconto
2) A vista no cartão = 5% de desconto
3) Em até 2x no cartão = preço normal
4) 3x ou mais no cartão = 20% de juros 

"""))

if formaPgto == 1: 
    valorFinal = (produto / 100 * 90)
    print('O produto de R${} deve ser vendido por R${}'.format(produto, valorFinal))
elif formaPgto == 2: 
    valorFinal = (produto / 100 * 95)
    print('O produto de R${} deve ser vendido por R${}'.format(produto, valorFinal))
elif formaPgto == 3: 
    valorFinal = (produto / 100 * 100)
    print('O produto de R${} deve ser vendido por R${}'.format(produto, valorFinal))
elif formaPgto == 4: 
    valorFinal = (produto / 100 * 120)
    print('O produto de R${} deve ser vendido por R${}'.format(produto, valorFinal))