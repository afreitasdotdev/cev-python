# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas
# No final do programa, mostre: # A media de idade do grupo # Qual o nome do homem mais velho
# Quantas mulheres tem menos de 20 anos

somaIdade = 0
mediaIdade = 0
maiorIdadeH = 0
nomeMaisVelho = ''
totalMulheres = 0

for p in range(1,5):
    print(' --- {}ª Pessoa --- '.format(p))
    nome = str(input('Digite o nome: ').strip())
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Sexo [M/F]: '))
    somaIdade += idade
    if p == 1 and sexo in 'Mm':
        maiorIdadeH = idade
        nomeMaisVelho = nome
    if sexo in 'Mm' and idade > maiorIdadeH:
        maiorIdadeH = idade
        nomeMaisVelho = nome
    if sexo in 'Ff' and idade < 20:
        totalMulheres += 1

mediaIdade = somaIdade / 4

print('A média de idade é {} anos'.format(mediaIdade))
print('O nome do homem mais velho é {} e possui {}'.format(nomeMaisVelho, maiorIdadeH))
print('O total de mulher com menos de 20 anos é {}'.format(totalMulheres))