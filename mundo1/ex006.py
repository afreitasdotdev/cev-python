# Crie um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada.

entrada = int(input('Digite um número: '))

dobro = entrada * 2
triplo = entrada * 3
raiz = entrada**(1/2)

print('O dobro de {} é {}, o triplo {} e a raiz {:.2f}'.format(entrada, dobro, triplo, raiz))
