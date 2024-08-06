# Para salários menores que 1.250 ele aplica 15% de aumento
# Para salários maior que 1.250 ele aplica 10% de aumento

salario = float(input('Digite seu salario: '))
if salario > 1250:
    # Multiplica o salário por "10" depois divide o resultado por "100" e depois soma o resultado + o salário.
    novo_aumento = salario + (salario * 10 / 100)
else:
    novo_aumento = salario + (salario * 15 / 100)
print(
    f'Um funcionário que ganhava R${salario:.2f}, com aumento passa a ganhar R${novo_aumento:.2f}')
