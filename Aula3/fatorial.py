def fatorial (numero):
    #Caso base
    if numero == 0 or numero == 1:
        return 1
    #Subproblemas
    else:
        return numero * fatorial (numero -1)
x = int(input("Digite um número para calcular seu fatorial:"))
res = fatorial(x)
print(f"O fatorial de {x} é {res}")