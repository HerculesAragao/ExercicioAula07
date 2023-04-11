nota1 = int(input('Digite a 1ª nota do aluno: '))
nota2 = int(input('Digite a 2ª nota do aluno: '))
nota3 = int(input('Digite a 3ª nota do aluno: '))
nota4 = int(input('Digite a 4ª nota do aluno: '))
media = (nota1 + nota2 + nota3 + nota4) / 4
if media >= 7:
    print('O aluno está aprovado com a média=',media)
else:
    print('O aluno foi reprovado com a média=',media)