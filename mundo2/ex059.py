# Crie um programa que leia dois valores e mostre um menu
# na tela: 1 Somar 2 Multiplicar 3 Maior 4 Novos numeros 
# 5 sair do programa. Seu programa deverá realizar a operação
# solicitada em cada caso.

v1 = int(input("Digite um valor: "))
v2 = int(input("Digite outro valor: "))
opcao = 9

while not opcao == 5:
    
    opcao = int(input("""

    [ 1 ] Somar valores
    [ 2 ] Multiplicar valores
    [ 3 ] Maior valor
    [ 4 ] Novos numeros
    [ 5 ] Sair do programa

    """))

    if opcao == 1:
        soma = v1 + v2
        print("O valor da soma entre {} e {} é {}".format(v1, v2, soma))
    elif opcao == 2:
        mult = v1 * v2
        print("O valor da multiplicacao entre {} e {} é {}".format(v1, v2, mult))
    elif opcao == 3:
        if v1 > v2:
            maior = v1
            print("O maior valor entre {} e {} é {}".format(v1, v2, maior))
        elif v1 < v2:
            maior = v2
            print("O maior valor entre {} e {} é {}".format(v1, v2, maior))
        elif v1 == v2:
            print("{} e {} são iguais".format(v1, v2))
    elif opcao == 4:
        v1 = int(input("Digite um valor: "))
        v2 = int(input("Digite outro valor: "))
    
