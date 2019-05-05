# Refaça o desafio 51, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura
# while

primTermo = int(input('Digite o termo da sua PA: '))
razao = int(input('Digite a razao da sua PA: '))
valor = primTermo
contador = 0 

while contador < 10: 
    valor += razao
    print(valor, end=' ')
    contador += 1