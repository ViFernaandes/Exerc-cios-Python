# 15% corresponde ao aumento salarial do funcionário.
salario = float(input('Qual é o salário do Funcionário? R$'))
aumento_salario = salario + (salario * 15 / 100)
print(
    f'Um funcionário que ganhava R${salario:.2f}, com 15% de aumento vai ganhar R${aumento_salario:.2f}')
