# o mesmo professor do desafio anterior quer sortear a ordem de apresentação
# de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos 
# e mostre a ordem sorteada

import random

prim = str(input('Digite o nome do primeiro aluno: '))
sgnd = str(input('Digite o nome do segundo aluno: '))
terc = str(input('Digite o nome do terceiro aluno: '))
quar = str(input('Digite o nome do quarto alunno: '))

lista = [prim, sgnd, terc, quar]

#escolhido = random.sample(lista, k=4)
#print('escolhido {}'.format(escolhido))

random.shuffle(lista)
print('A nova ordem é: ')
print(lista)
