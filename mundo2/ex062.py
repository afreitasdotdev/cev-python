# Melhore o desafio 61, perguntando para o usuario se ele quer 
# mostrar mais alguns termos. O progrma encerra quando ele disser
# que quer mostrar 0 (zero) termos.

primTermo = int(input('Digite o termo da sua PA: '))
razao = int(input('Digite a razao da sua PA: '))
valor = primTermo
contador = 0 
total = 0
mais = 10

while mais != 0:
    total += mais
    while contador < total: 
        valor += razao
        print(valor, end=' ')
        contador += 1
    print('PAUSA')

    mais = int(input('Quantos termos vc quer mostrar? '))
