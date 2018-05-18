"Em sala"

import sys

while True:
    print('Digite exit para sair do programa:')
    resposta = input()
    if resposta == 'exit':
        sys.exit()
    print(f'Você digitou {resposta}.')