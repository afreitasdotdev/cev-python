# Crie m programa onde o usuario possa digitar varios valores
# numéricos e cadastre-os em uma lista. Caso o número já exista
# lá  dentro, ele não será adicionado. No final, serão exibidos
# todos os valores únicos digitados, em ordem crescente.

lista = []
contador = 0
while True: 
    numero = int(input('Digite um valor: '))
    if numero not in lista:
        print('Adicionando valor...')
        lista.append(numero)
    elif numero in lista:
        print('Numero já cadastrado... Ignorando')
    
    continua = input('Quer continuar? [S/N] ').upper()
    if continua == 'N':
        break
#lista.sort()
#print(lista)
print(sorted(lista))
