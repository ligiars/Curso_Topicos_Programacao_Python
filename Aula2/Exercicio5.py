#
# Author: Lígia Rocha
#
"O programa gera a tabuada de multiplicação de um numero"
x = 1
soma = 0

n = int(input('Digite o número:\n'))
while x <= 10:
    soma += n
    print(x * n)
    x += 1

