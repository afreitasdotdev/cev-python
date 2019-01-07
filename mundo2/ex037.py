# Escreva um programa que leia um numero inteiro qualquer e pergunte qual
# qual a base de conversão. 1 Binario, 2 Octal e 3 para Hexa

num = int(input('Digite um numero e veja sua conversão: '))

base = int(input("""Escolha em qual base o número deve ser convertido:
Digite (1) para BINARIO
Digite (2) para OCTAL
Digite (3) para HEXADECIMAL \n"""))

if base == 1:
    convertBin = bin(num)
    print('O numero {0} em Binario é {1}'.format(num, convertBin))
elif base == 2: 
    convertOct = oct(num)
    print('O numero {0} em Octal é {1}'.format(num, convertOct))
elif base == 3: 
    convertHex = hex(num)
    print('O numero {0} em Hexadecimal é {1}'.format(num, convertHex))
else: 
    print('Opção invalida. Tente novamente')
