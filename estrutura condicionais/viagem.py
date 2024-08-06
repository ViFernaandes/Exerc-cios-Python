# Para viagens acima de 200km o preço cobrado é R$0.45 por km
# Para viagens abaixa de 200km o preço cobrado é R$0.50 por km

distancia = float(input(f'Qual a distância da sua viagem? '))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print(f'O preço da sua passagem é R$ {preco:.2f}')
