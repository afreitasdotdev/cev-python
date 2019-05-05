# Crie um programa que leia varios numeros inteiros pelo teclado. O programa só
# vai parar quando o usuário digitar o valor 999, que é a condição de parada. No
# final mostre quantos numeros foram digitados e qual foi a soma entre eles. 
# desconsiderando o flag.

soma = 0 
while True:
    num = int(input('Digite um numero: '))
    if num == 999:
        break
    soma += num

print(f'O valor total da soma é {soma}')