# Faça um programa que leia qualquer frase e:
# Quantas vezes aparece a letra a
# Em que posição aparece a primeira vez
# Em que posição aparece a ultima vez

frase = str(input('Digite a frase: ')).strip().lower()

contaA = str(frase.count('a'))
inicioA = str(frase.find('a')+1)
fimA = str(frase.rfind('a')+1)

print('A vogal A aparece {}'.format(contaA))
print('A primeira incidencia é em {}'.format(inicioA))
print('A ultima incidencia é em {}'.format(fimA))