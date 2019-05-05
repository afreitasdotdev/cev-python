# Faça um programa que leia um numero qualquer e mostre
# seu fatorial

# Ex: 5! = 5x4x3x2x1 = 120

num = int(input('Digite um valor: '))
contador = num
fator = 1

print('Calculando {}! = '.format(num), end ='')
while contador > 0: 
    print('{}'.format(contador), end='')
    print(' x ' if contador > 1 else ' = ', end='')
    fator = fator * contador
    contador -= 1
print('{}'.format(fator))
