# Crie um programa que leia duas notas e calcule a media de um aluno
# abaixo de 5.0 = Reprovado
# entre 5.0 e 6.9 = recuperação
# acima de 7.0 = aprovado

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = float((nota1 + nota2) / 2)

if media < 5.0:
    print('Sua media foi {} e vc esta REPROVADO'.format(media))
elif media >= 5.0 and media <= 6.9:
    print('Sua media foi {} e vc esta em RECUPERACAO'.format(media))
elif media >= 7.0:
    print('Sua media foi {} e vc esta APROVADO'.format(media))