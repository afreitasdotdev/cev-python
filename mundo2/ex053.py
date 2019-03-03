# Crie um programa que leia uma frase qualquer e diga se ela é
# um palindromo, desconsiderando os espaços.
frase = str(input('Digite a frase: ')).upper().strip()

palavras = frase.split()
junto = ''.join(palavras)
inverso=''

for i in range(len(junto) - 1, -1, -1):
    inverso += junto[i]
if inverso == junto:
        print('Temos um palindromo')
else:
        print('A frase não é um palindromo')