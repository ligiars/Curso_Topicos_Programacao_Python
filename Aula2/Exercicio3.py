#
# Author: Lígia Rocha 18/05/2018
#
"O programa recebe as notas e a frequencia de um aluno de graduacao e define se ele é aprovado ou nao levando em consideracao sua frequencia e media."
frequencia = float(input('Qual foi a frequência percentual do aluno?'))

if  frequencia > 25:
    p1 = float(input('Qual a nota do aluno na primeira avaliação?'))
    p2 = float(input('Qual a nota do aluno na segunda avaliação?'))
    media1 = (p1 + p2) / 2
    if media1 >= 7:
        result = 'Aluno Aprovado'

    elif media1 < 3:
        result = 'Aluno Reprovado'

    if media1 >= 3 > 7:
        pf = float(input('E na prova final?'))
        media2 = (media1 + pf) / 2
        if media2 >= 5:
            result = 'Aluno Aprovado'

        else:
            result = 'Aluno Reprovado'

else:
    result = 'Aluno Reprovado'

print(result)
