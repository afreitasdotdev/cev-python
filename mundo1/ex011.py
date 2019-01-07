# Faça um programa que leia a largura e altura de uma parede em metros, calcule a sua área
# e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta 
# uma área de 2m²

altura = float(input('Digite a altura: '))
largura = float(input('Digite a largura: '))
area = float(altura * largura)

print('Tendo a altura {} e largura {}, a area da sua parede é {}'.format(altura, largura, area))

tinta = float(area / 2)

print('Sabendo que cada litro pinta 2m², você precisará de {} litros para uma parede com {}m de area.'.format(tinta, area))
