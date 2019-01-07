# Crie um programa que leia o peso e altura de uma pessoa e calcule o IMC
# Abaixo de 18.5 = Abaixo do peso
# Entre 18.5 e 25 = Peso ideal
# 25 até 30 = Sobrepeso
# 30 até 40 = Obesidade
# Acima de 40 = Obesidade mórbida

peso = float(input('Informe seu peso: '))
alt = float(input('Informe sua altura: '))

imc = (peso / (alt * alt))

if imc < 18.5: 
    print('Seu IMC é {:.2f}. Vc está abaixo do peso ideal.'.format(imc))
elif imc > 18.5 and imc <= 25:
    print('Seu IMC é {:.2f}. Vc está no peso ideal.'.format(imc))
elif imc > 25 and imc <= 30:
    print('Seu IMC é {:.2f}. Vc está com sobrepeso.'.format(imc))
elif imc > 30 and imc <= 40:
    print('Seu IMC é {:.2f}. Vc está com obesidade.'.format(imc))
elif imc > 40:
    print('Seu IMC é {:.2f}. Vc está com obesidade mórbida.'.format(imc))