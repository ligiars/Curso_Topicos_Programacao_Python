#
# Author: Lígia Rocha 18/05/2018
#
"O programa relaciona o preço do produto com sua classificação"
classe = float(input('Insira a classe do Produto:'))

if classe == 1:
    preco = '10 reais'

if classe == 2:
    preco = '15 reais'

if classe == 3:
    preco = '25 reais'

if classe == 4:
    preco = '30 reais'

if classe == 5:
    preco = '40 reais'

elif classe != 1 != 2 != 3 != 4 != 5:
    preco = 'Produto não classificado.'


print(f'O preço desse produto é igual a:\n{preco}')
