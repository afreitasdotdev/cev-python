# Faça um programa que leia tres numeros e diga qual é o maior e qual é o menor

um = int(input('Digite o primeiro numero: '))
dois = int(input('Digite o segundo numero: '))
tres = int(input('Digite o terceiro numero: '))

if um > dois and um > tres:
    print('{} é o maior numero'.format(um))
if dois > tres and dois > um:
    print('{} é o maior numero'.format(dois))
if tres > dois and tres > um:
    print('{} é o maior numero'.format(tres))
if um < dois and um < tres:
    print('{} é o menor numero'.format(um))
if dois < tres and dois < um:
    print('{} é o menor numero'.format(dois))
if tres < dois and tres < um:
    print('{} é o menor numero'.format(tres))
