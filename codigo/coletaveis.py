class Coletaveis():
    def __init__(self, quantidade, diminuirDano, maximo, quantidadeDano, dano):
        self.quantidade = quantidade
        self.diminuirDano = diminuirDano
        self.maximo = maximo
        self.quantidadeDano = quantidadeDano
        self.dano = dano

    def coletarItem(self):
        if self.quantidade < self.maximo:
            self.quantidade += 1
    
    def definirDano(self):
        self.dano = self.quantidadeDano * self.diminuirDano

class Aveia(Coletaveis):
    def __init__(self, quantidade, diminuirDano, maximo, quantidadeDano, dano):
        super().__init__(quantidade, diminuirDano, maximo, quantidadeDano, dano)
        
        self.quantidade = 0
        self.diminuirDano = 0
        self.maximo = 0
        self.quantidadeDano = 0
        self.dano = 0

class Girassol(Coletaveis):
    def __init__(self, quantidade, diminuirDano, maximo, quantidadeDano, dano):
        super().__init__(quantidade, diminuirDano, maximo, quantidadeDano, dano)

        self.quantidade = 0
        self.diminuirDano = 0
        self.maximo = 0
        self.quantidadeDano = 0
        self.dano = 0

class PombaLaser(Coletaveis):
    def __init__(self, quantidade, diminuirDano, maximo, quantidadeDano, dano):
        super().__init__(quantidade, diminuirDano, maximo, quantidadeDano, dano)

        self.quantidade = 0
        self.diminuirDano = 0
        self.maximo = 0
        self.quantidadeDano = 0
        self.dano = 0

class Oculos(Coletaveis):
    def __init__(self, quantidade, diminuirDano, maximo, quantidadeDano, dano):
        super().__init__(quantidade, diminuirDano, maximo, quantidadeDano, dano)

        self.quantidade = 0
        self.diminuirDano = 0
        self.maximo = 0
        self.quantidadeDano = 0
        self.dano = 0

aveia = Aveia(0, 0, 0, 0, 0)

girassol = Girassol(0, 0, 0, 0, 0)

pombaLaser = PombaLaser(0, 0, 0, 0, 0)

oculos = Oculos(0, 0, 0, 0, 0)
