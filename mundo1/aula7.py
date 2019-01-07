valor1 = int(input('Insira o primeiro valor: '))
valor2 = int(input('Insira o segundo valor: '))

adicao = valor1 + valor2
sub = valor1 - valor2
multi = valor1 * valor2
div = valor1 / valor2
divi = valor1 // valor2

resto = valor1 % valor2

print('A soma entre {} e {} é {}, a sutração é {}, a divisao é {:.1f} e a multiplicação é {}' .format(valor1, valor2, adicao, sub, div, multi), end='. ')
print('A divisão inteira é {} e o resto {}' .format(divi, resto))
