def fibonacci (numero):
    #Caso base
    if numero == 0:
        return 0
    elif numero == 1 or numero == 2:
        return 1
    #Subproblemas
    else:
        return fibonacci (numero -1) + fibonacci (numero -2)
x = int(input("Digite um número para calcular fibonacci:"))
res = fibonacci(x)
print(f"O fibonacci de {x} é {res}")