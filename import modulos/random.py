# random - escolhe um elemento aleatório.
# choice - escolhe um valor dentro da lista.
from random import choice
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]  # Criação de lista para sortear um dos alunos.
escolhido = lista(choice)
print(f'O alundo escolhido foi {escolhido}')
