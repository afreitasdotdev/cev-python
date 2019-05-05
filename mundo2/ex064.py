# Crie um programa que leia varios numeros inteiros pelo teclado.
# O programa só vai parar quando o usuario digitar o valor 999, que
# é a condição de parada. No final, mostre quantos numeros foram
# digitados e qual foi a soma entre eles (desconsiderando o flag)

# Feito like a gambiarra
#valor = 0
#soma = 0
#
#while valor != 999:
#    valor = int(input('Digite o valor: '))
#    soma += valor
#
#print(soma-999)

num = cont = soma = 0

num = int(input('Digite um numero e 999 para sair: '))

while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um numero e 999 para sair: '))

print('Voce digitou {} numeros e a soma entre eles foi {}'.format(cont, soma))