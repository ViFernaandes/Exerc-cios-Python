class Computador:
    def __init__(self, marca, memoria_ram, placa_de_video):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video

    def Ligar(self):
        print('Estou ligando')

    def Desligar(self):
        print('Estou desligando')

    def ExibirInformacoesDesteComputador(self):
        print('A marca do computador é: {}, quantidade de memoria ram: {}GB, modelo da placa de video {},'.format(
            self.marca, self.memoria_ram, self.placa_de_video))


computador1 = Computador('Asus', '36', 'Nvidia')
computador1.Ligar()
computador1.ExibirInformacoesDesteComputador()
computador1.Desligar()
