# Crie um programa que leia varios numeros inteiros pelo teclado.
# No final da execução, mostre a media entre todos os valores e
# qual foi o maior e menor valores lidos. O programa deve perguntar
# ao usuario se ele quer ou não continuar a digitar valores.

resp = 's'
soma = 0 
c = 0 
maior = 0
menor = 0

while not resp in 'Nn':
    num = int(input("Digite um numero: "))
    soma += num
    c += 1
    if c == 1:
        menor = num
        maior = num
    elif num > maior:
        maior = num
    elif num < menor:
        menor = num

    resp = input("Quer continuar: S/N")

media = (soma / c)

print("A média entre todos os valores é {:.2f}".format(media))
print("O menor valor foi {}".format(menor))
print("O maior valor foi {}".format(maior))