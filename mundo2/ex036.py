# Escreva um programa para aprovar o emprestimos para a compra de uma casa
# O programa vai perguntar o valor da casa, o salario do comprador e em 
# quantos anos ele vai pagar. Calcule o valor da prestação mensal sabendo que
# ela não pode exceder 30% do seu salario ou então seu emprestimo será negado.

valorCasa = int(input('Por favor, informe o valor da casa: R$ '))
salario = float(input('Informe seu salario: R$ '))
parcelas = int(input('Em quantos' '\033[31m ANOS \033[m' 'será pago o imovel? '))

qtdParc = (parcelas * 12)
valorParcela = float((valorCasa / qtdParc))
valorMaxParc = float(((salario / 100) * 30 ))

if valorParcela <= valorMaxParc:
    print("""
    Seu emprestimo foi aprovado.
    O imovel será negociado em {} parcelas de {:.2f}
    """.format(qtdParc, valorParcela))
elif valorParcela > valorMaxParc:
    print("""
    Nessas condições, o imovel seria negociado em {} parcelas de {:.2f}
    A parcela ultrapassa 30% da sua renda. Seu emprestimo foi negado.
    """.format(qtdParc, valorParcela))