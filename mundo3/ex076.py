# Crie um programa que tenha uma tupla unica com
# nomes de produtos e seus respectivos preços na 
# seguencia. No final, mostre uma lsitagem de preços,
# organizando os dados em forma tabular
# PRODUTO...................R$ valor

produtos = ('Laranja', '3.00', 'Banana', '1.99', 'Abacate', '7.99')

print('=' * 50)
print('{:^50}'.format('LISTA DE PRODUTOS'))
print('=' * 50)

for item in range(0, len(produtos)):
    if item % 2 == 0: 
        print(f'{produtos[item]:.<45}', end='')
    else:
        print(f'R${produtos[item]:>2}')
        
### REFAZER PARA TREINAR MAIS