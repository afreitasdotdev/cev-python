# Refaça o desafio 35, dos triangulos, acrescentando o recurso de mostrar
# o tipo de triangulo que será formado 
# Equilatero = todos os lados iguais
# Isósceles = dois lados iguais
# Escaleno = todos os lados diferentes

r1 = int(input('Digite o primeiro segimento: '))
r2 = int(input('Digite o primeiro segimento: '))
r3 = int(input('Digite o primeiro segimento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print('OK. Triangulo possivel')

    if r1 == r2 and r1 == r3:
        print('Triangulo do tipo Equilatero')
    elif r1 == r2 and r1 != r3: or r2 == r3 and r2 != r1 
        print('Triangulo do tipo Isósceles')
    elif r1 != r2 and r1 != r3 and r2 != r3:
        print('Triangulo do tipo Escaleno')

else: 
    print('Não é possível formar um triangulo')
