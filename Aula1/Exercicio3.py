"O programa transforma o valor de um tempo expresso em hora, minutos e segundos, no valor correspondente em segundos"

s = float(input('Inserir a quantidade de segundos:'))

h = s//3600
min = (s%3600)//60
seg = s%60


print(f'Esse valor é igual a {h}h, {min}min e {seg}s.')