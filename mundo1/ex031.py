# Desenvolva um programa que pergunte a distancia de uma viagem em km.
# Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens 
# até 200 km e R$ 0,45 para viagens mais longas

viagem = int(input('Qual a distancia da viagem em km? '))

if viagem <= 200:
    valor = (viagem * 0.50)
    print('O valor da passagem será {}'.format(valor))
else: 
    valor = (viagem * 0.45)
    print('O valor da passagem será {}'.format(valor))
