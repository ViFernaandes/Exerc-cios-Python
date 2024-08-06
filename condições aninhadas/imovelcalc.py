print('-=-' * 14)
print('\033[1;31;40mBem vindo ao financiamento do seu imóvel\033[m')
print('-=-' * 14)
casa = float(input('Digite o valor do imóvel? R$ '))
salario = float(input('Digite seu salário? R$ '))
anos = int(input('Em quantos anos vai financiar o imóvel? '))
prestacao_mensal = casa / (anos * 12)
minimo = salario * 30 / 100
if prestacao_mensal <= minimo:
    print('Parabéns foi aprovado seu financiamento! ')
    print(
        f'Você vai pagar o valor da R${prestacao_mensal:.2f} por mês, durante {anos} anos! ')
else:
    print(
        f'Para pagar um imóvel de R${casa:.2f} em {anos} anos a prestação será de R${prestacao_mensal:.2f}')
    print('Não foi aprovado seu financiamento')
