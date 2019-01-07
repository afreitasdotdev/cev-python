print('\033[0;31;40m Olá Mundo\033[m')

nome = 'Freitas'
print('Olá, \033[0;31;40m{}\033[m. Muito Prazer!'.format(nome))

print('Olá, {}{}{}. Muito Prazer!'.format('\033[0;31;40m', nome, '\033[m'))

cores = {'limpa':'\033[m', 
         'azul':'\033[34m', 
         'amarelo':'\033[33m', 
         'pretoebranco':'\033[7:30m'}

print('Olá, {}{}{}. Muito Prazer!'.format(cores['amarelo'], nome, cores['limpa']))