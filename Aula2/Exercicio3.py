#
#
#
"O programa recebe as notas e a frequencia de um aluno de graduacao e define se ele é aprovado ou nao levando em consideracao sua frequencia e media."
frequencia = float(input('Qual foi a frequência percentual do aluno?'))
p1 = float(input('Qual a nota do aluno na primeira avaliação?'))
p2 = float(input('Qual a nota do aluno na segunda avaliação?'))
pf = float(input('E na prova final? (caso não tenha sido realizada, insira 0):'))
media1 = (p1 + p2)/2
media2 = (media1 + pf)/2

if  frequencia < 75:
    result = 'Aluno Reprovado'

elif media1 >= 7:
    result = "Aluno Aprovado"

elif media1 < 7 >= 3 and media2 >= 5:
    result = "Aluno Aprovado"

elif media1 < 7 >= 3 and media2 < 5:
    result = "Aluno Reprovado"

print(result)



