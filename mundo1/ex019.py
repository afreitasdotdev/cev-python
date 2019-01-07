# Um professor quer sortear um do seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome
# do escolhido

import random

prim = input('Digite o nome do primeiro aluno: ')
sgnd = input('Digite o nome do segundo aluno: ')
terc = input('Digite o nome do terceiro aluno: ')
quar = input('Digite o nome do quarto alunno: ')

lista = [prim, sgnd, terc, quar]

escolhido = random.choice(lista)

print('escolhido {}'.format(escolhido))
