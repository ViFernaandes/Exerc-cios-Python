class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def calcular_valor_total(self):
        # Efetua o calculo entre o preço e a quantidade de produto em estoque.
        return self.preco * self.quantidade


# Exemplo de uso da classe
produto1 = Produto('Caneta', 1.50, 100)
valor_total = produto1.calcular_valor_total()
print(f'O valor total do estoque de {produto1.nome} é R${valor_total:.2f}')
