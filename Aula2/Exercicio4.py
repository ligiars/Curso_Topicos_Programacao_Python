#
# Author: Lígia Rocha
#
"O programa exibe a contagem regressiva do lançamento de um foguete de 10 a 0"

x = int(input('Digite 10 para começar a contagem regressiva:\n'))
y = 1

while x >= y:
    x -= 1
    print(x)
print ('e Fogo!')