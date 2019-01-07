# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
# e mostre quantos dolares ela pode comprar. Considere U$$ 1 = R$ 3,27

dolar = float(3.27)

carteira = float(input('Quantos dinheiros vc tem? '))

formula = carteira // dolar

sobra = carteira % dolar 

print('Com o dolar à {}'.format(dolar))
print('Com {} dinheiros, voce consegue comprar {} dolares e ainda sobra {:.2f}'.format(carteira, formula, sobra))
