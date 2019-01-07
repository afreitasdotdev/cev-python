# Faça um progrma que leia o ano de nascimento e informe a idade
# De acordo com a idade, informe se ele ainda vai se alistar, se 
# ja é hora de se alistar ou se ja passou do tempo de se alistar 
# Seu programa deve mostrar o tempo que falta ou que passou do prazo.

import datetime 

anoNasc = int(input('Digite o ano de nascimento: '))

idade = (datetime.date.today().year - anoNasc)

if idade <=17:
    print('Voce ainda irá se alistar')
    tempo = (18 - idade)
    print('Faltam {} ano(s) para se alistar'.format(tempo))
elif idade == 18:
    print('Já é hora de se alistar')
    tempo = (18 - idade)
    print('Faltam {} ano(s) para se alistar'.format(tempo))
elif idade > 18:
    print('Já passou da fase de alistamento')
    tempo = (idade - 18)
    print('Já fazem {} ano(s) que voce se alistou'.format(tempo))