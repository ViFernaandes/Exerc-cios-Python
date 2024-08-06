# .strip() - Elimina os espaços "antes" do nome e "depois", mas mantém os espaços entre as palavras.
# len() - Conta quantidade de letras ao todo.
# .count (" ") - Conta a quantidade de espaços entre as letras.
# .split() - Joga dentro de uma lista os nomes inteiros.
nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome ...')
print(f'Seu nome em maiúsculas é: {nome.upper()}')
print(f'Seu nome em minúsculas é: {nome.lower()}')
print(f'Seu nome tem ao todo: {len(nome) - nome.count(" ")} letras')
nome1 = nome.split()
print(f'Seu primeiro nome é {nome1[0]} e ele tem {len(nome1[0])} letras')
