from random import choice
a1 = str(input('Informe o nome do aluno: '))
a2 = str(input('Informe o nome do aluno: '))
a3 = str(input('Informe o nome do aluno: '))
a4 = str(input('Informe o nome do aluno: '))
sorteio = [a1, a2, a3, a4]
escolhido = choice(sorteio)
print('O aluno sorteado foi:{} '.format(escolhido))
