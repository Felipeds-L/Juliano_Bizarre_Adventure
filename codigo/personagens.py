class Personagem:
    def __init__(self):
        self.nome = ''
        self.vidaCheia = 0
        self.vidaAtual = 0
        self.hitbox = ''
        self.pombaLaser = False
        self.oculos = False
        self.listaAtaques = []

    def setVida(self, vida):
        self.vidaCheia = vida
        self.vidaAtual = vida
    
    def curar(self):
        if self.vidaAtual < self.vidaCheia:
            self.vidaAtual += 1
        else:
            self.vidaAtual = self.vidaCheia
    
    def sofrerDano(self, dano):
        self.vidaAtual -= dano
    
    def pegarPombaLaser(self):
        self.pombaLaser = True
        self.listaAtaques.append('Pomba Laser')
    
    def pegarOculos(self):
        self.oculos = True
        self.listaAtaques.append('Intimidar')
    
    def setHitbox(self, hitbox):
        self.hitbox = hitbox