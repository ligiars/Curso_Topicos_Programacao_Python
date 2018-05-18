#
# Author: Lígia Rocha 18/05/2018
#
"O programa pede qual operação você deseja fazer, pede os números e imprime os resultados."
operacao = input ('Você deseja somar ou multiplicar?')
numero_1 = float(input('Digite o primeiro número:'))
numero_2 = float(input('Agora o segundo:'))

if operacao == 'somar':
    resultado = numero_1+numero_2

if operacao == 'multiplicar':
    resultado = numero_1*numero_2

elif operacao != 'somar' != 'multiplicar':
    resultado = 'Operação inválida.'


print(f'Seu resultado deu igual a :{resultado}')
