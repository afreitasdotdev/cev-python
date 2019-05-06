# Crie um programa que tenha uma tupla totalmente preenchida com uma 
# contagem por extenso de zero até vinte. Seu programa deverá ler um 
# numero pelo teclado (entre 0 e 20) e mostra-lo por extenso.

numeros = ('zero','um','dois','tres','quatro','cinco',
            'seis','sete', 'oito', 'nove', 'dez', 'onze',
            'doze', 'treze','quatorze', 'quinze','dezesseis',
            'dezesete', 'dezoito','dezenove','vinte')

while True:
    entrada = int(input('Digite um numero de 0 à 20: '))
    if 0 <= entrada <= 20:
        print(f'Você digitou {numeros[entrada]}')
        continua = input('Voce quer continuar S/N? ').upper()
        if continua == 'N':
            break

print('Finalizando!')