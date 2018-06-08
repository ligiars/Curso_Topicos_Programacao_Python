import random


def getNumber(number):
    if number == 1:
        return "É o número 1"
    elif number == 2:
        return "É o número 2"
    elif number == 3:
        return "É o número 3"
    elif number == 4:
        return "É o número 4"
    elif number == 5:
        return "É o número 5"
    elif number == 6:
        return "É o número 6"
    elif number == 7:
        return "É o número 7"
    elif number == 8:
        return "É o número 8"
    elif number == 9:
        return "É o número 9"

r = random.randint(1,9)
sorteio = getNumber(r)
print (sorteio)


