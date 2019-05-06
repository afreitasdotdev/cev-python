# Crie uma tupla preenchia com os 20 primeiros colocados da Tabela
# do Camp Bras de Fut, na ordem de colocação. Depois mostre:
# a) aprnas os 5 primeiros colocados. b) Os ultimos 4 colocados
# c) uma lista com os times em ordem alfabetica. d) Em que posição
# na tabela está o time da Chapecoense

classificacao = ('Atlético-MG','Palmeiras','São Paulo','Santos','Botafogo','Goiás',
'Athletico-PR','Grêmio','Flamengo','Chapecoense','Bahia','Corinthians','Ceará',
'Internacional','Fortaleza','Avaí','CSA','Vasco','Fluminense','Cruzeiro')

primeiros = print(f'''Primeiros classificados: \n
    {classificacao[0:5]}''')

ultimos = print(f'''Ultimos classificados: \n
    {classificacao[-4:]}''')

print(f'Times em ordem alfabetica: {sorted(classificacao)}')

for pos, time in enumerate(classificacao):
    if time == 'Chapecoense':
        print(f'\nA {time} está em {pos+1} ºlugar')

# print(f'Chapecoense está em {classificacao.index("Chapecoense")+1} ºlugar')