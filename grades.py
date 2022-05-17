prova1 = int(input('Digite a nota da prova 1: '))
trab = int(input('Digite a nota do trabalho: '))
prova2 = int(input('Digite a nota da prova 2: '))

media = ((prova1 * 2) + trab + (prova2 *2)) /5

if media>= 6 :
    print('Aluno aprovado com nota: ', media )
elif media >3 :
    print('Aluno em recuperação com nota: ', media)
else:
    print('Reprovado! nota: ', media )