class Personagem:
    def __init__(self):
        self.vidaCheia = 0
        self.vidaAtual = 0
        self.dano = 0
        self.hitbox = ''
        self.pombaLaser = False
        self.oculos = False
        self.aveia = 0
        self.nome = ''
        self.listaAtaques = ['Bicada']

    def setVida(self, vida): #set_vida
        self.vidaCheia = vida
        self.vidaAtual = vida
    
    def getVida(self): #get_vida
        return self.vidaAtual
    
    def getVidaTotal(self):
        return self.vidaCheia
    
    def curar(self): 
        if self.vidaAtual < self.vidaCheia:
            self.vidaAtual += 1
        else:
            self.vidaAtual = self.vidaCheia
    
    def sofrerDano(self, dano): #sofrer_dano
        self.vidaAtual -= dano
    
    def setNome(self, nome): #set_nome
        self.nome = nome
    
    def getNome(self): #get_nome
        return self.nome
    
    def setDano(self, dano): #set_dano
        self.dano = dano
    
    def getDano(self): #get_dano
        return self.dano
    
    def pegarOculos(self): #pegar_oculos
        self.oculos = True
        self.listaAtaques.append('Intimidar')

    def pegarPombaLaser(self): #pegar_pomba_laser
        self.pombaLaser = True
        self.listaAtaques.append('Pomba Laser')
    
