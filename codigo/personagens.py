class Personagem:
    def __init__(self):
        self.vidaCheia = 0
        self.vidaAtual = 0
        self.dano = 0
        self.hitbox = ''
        self.pombaLaser = False
        self.oculos = False
        self.nome = ''
        self.listaAtaques = {'Bicada': 5}

    def setVida(self, vida):
        self.vidaCheia = vida
        self.vidaAtual = vida
    
    def getVida(self):
        return self.vidaAtual
    
    def curar(self):
        if self.vidaAtual < self.vidaCheia:
            self.vidaAtual += 1
        else:
            self.vidaAtual = self.vidaCheia
    
    def sofrerDano(self, dano):
        self.vidaAtual -= dano
    
    def setNome(self, nome):
        self.nome = nome
    
    def getNome(self):
        return self.nome
    
    def setDano(self, dano):
        self.dano = dano
    
    def getDano(self):
        return self.dano
    
    def pegarOculos(self):
        self.oculos = True
        self.listaAtaques.append('Intimidar')

    def pegarPombaLaser(self):
        self.pombaLaser = True
        self.listaAtaques.append('Pomba Laser')
    
