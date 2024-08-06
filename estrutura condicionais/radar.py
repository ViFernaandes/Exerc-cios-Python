# Programa que funciona como Radar de velocidade:
# Limite de velocidade: 80km/h
# Valor da multa: R$ 7,00 por cada Km acima do limite.
velocidade = float(input('Velocidade do carro atual? '))
if velocidade > 80:
    print('Multado!, Passou do limite de velocidade permitido que é 80Km/h')
# Calcula utilizando a ordem de precedência.
# Tudo que está dentro do parenteses é resolvido primeiro.
# O resultado multiplica por "7".
    multa = (velocidade - 80) * 7
    print(f'O valor da multa é R$ {multa:.2f}')
print('Dirija com segurança!')
