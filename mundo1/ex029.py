# Escreva um programa que leia a velocidade de um carro
# Se ele ultrapassar a velocidade de 80km/h, mostre uma mensagem
# Dizendo que ele foi multado. A multa deve custar R$ 7,00 por cada
# km acima do limite

vel = int(input('Digite a velocidade do veiculo: '))

if vel > 80:
    print('Voce será multado.')
    excesso = (vel - 80)
    valor = (excesso * 7)
    print('Voce excedeu {}km/h acima do permitido.'.format(excesso))
    print('Com a taxa de R$ 7,00/km, deverá pagar R${},00'.format(valor))
else:
    print('Voce não será multado.')