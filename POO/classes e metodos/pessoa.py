class Pessoa:
    def __init__(self, nome, idade, endereco):
        self.nome = nome
        self.idade = int(idade)  # Certificicando que idade é um número inteiro
        self.endereco = endereco

    def apresentar(self):
        print(
            f'Olá, meu nome é: {self.nome}, tenho {self.idade} anos e moro em {self.endereco}')


pessoa1 = Pessoa('Joao', '30', 'São Paulo')
pessoa1.apresentar()
