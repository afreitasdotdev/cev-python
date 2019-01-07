# Conversão de ºC para ºF

temp1 = float(input('Digite a temperatura em ºC: '))
# 1ºC equivale a 33,8 ºF
# res = float(temp1 * 33.8)
res = ((temp1 * 9/5) + 32)

print('A temperatura de {}ºC equivale a {:.2f}ºF'.format(temp1, res))
