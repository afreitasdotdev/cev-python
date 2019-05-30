# Crie um programa onde o usuario digite uma expressao qualquer
# que use parenteses. Seu aplicativo deverá analisar se a expressão
# passada está com os parenteses abertos e fechados na ordem correta.

expr = str(input('Digite uma expressão:'))

parenteses = []

for letra in expr:
    if letra == '(':
        parenteses.append(letra)
    elif letra == ')':
        if len(parenteses) > 0:
            parenteses.pop()
        else:
            parenteses.append(letra)
            break
if len(parenteses) == 0:
    print('Parabens, sua expressão está correta!!')

else: 
    print('Oh não! Sua expressão está incorreta.')
    print(f'Tem coisa a mais ai: {parenteses}')
