# Faça um programa que mostre a tabuada de varios numeros, um de cada vez
# para cada valor digitado pelo usuario. O programa será interrompido quando
# o numero solicitado for negativo.

while True:
    
    print('='*10)
    print('Digite um numero negativo para cancelar')
    print('='*10)
    
    num = int(input('De qual numero voce quer ver a tabuada??  '))

    if num < 0:
        break
    else:
        for c in range(0,11):
            print(f"{num} x {c} = ({num * c})")
    