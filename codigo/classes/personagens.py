############## FUNÇÕES ###############
# ----> personagem = Personagem() <----
#
# personagem.setNome("Nome") (str) --> Escolhe um Nome para o personagem
# personagem.setVida(vida) (int) --> Escolhe uma vida base para o personagem
# personagem.sofrerDano(dano) (int) --> O personagem sofre dano na vida
# personagem.setAtaques("ataque") (str) --> Adiciona um ataque a lista de ataques do personagem
# personagem.curar() --> Cura o personagem em um de vida
# personagem.sprite("sprite") (str) --> Define a sprite atual do personagem
# personagem.oculos() --> Seta o uso do óculos do personagem para True
#
# >Somente< Juliano terá uma lista de ataques e opção de usar óculos, por padrão Juliano começará apenas com "Bicada" na lista
# até que o "Óculos" e a "Pomba Laser" sejam adquiridos, adicionando os ataques "Intimidar" e "Pomba Laser" respectivamente.

class Personagem():
    def __init__(self):
        self.nome = None
        self.vida = None
        self.ataques = ["Bicada"]
        self.sprite = None
        self.oculos - False

    def setNome(self, nome):
        self.nome = nome
    
    def setVida(self, vida):
        self.vida = vida
    
    def sofrerDano(self, dano):
        self.vida -= dano
    
    def curar(self):
        self.vida += 1

    def setAtaques(self, ataque):
        self.ataques.append(ataque)
    
    def setSprite(self, sprite):
        self.sprite = sprite
    
    def setOculos(self):
        self.oculos = True