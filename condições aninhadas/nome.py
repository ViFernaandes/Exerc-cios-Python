nome = str(input('Qual é seu nome? '))
if nome == 'Vini':
    print('Que nome legal!')
elif nome == 'Pedro' or nome == 'João' or nome == 'Bia':
    print('Seu nome é bem comum no Brasil.')
elif nome in 'Paula Fernanda Giovana':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal.')
print(f'Tenha um bom dia, {nome}')
