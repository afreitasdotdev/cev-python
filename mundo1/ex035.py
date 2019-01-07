# Desenvolva um progrma que leia tres segmentos de reta e diga ao usuario
# se elas conseguem formar um triangulo

r1 = int(input('Digite o primeiro segimento: '))
r2 = int(input('Digite o primeiro segimento: '))
r3 = int(input('Digite o primeiro segimento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print('OK. Triangulo possivel')
else: 
    print('Não é possível formar um triangulo')
    
