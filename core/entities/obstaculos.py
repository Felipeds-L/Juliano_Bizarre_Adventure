###################### FUNÇÕES ########################
# -----> arvore = Obstaculo() <-----
#
# arvore.setHitbox(altura, largura) (int, int) --> Cria uma matriz com a área da hitbox
# arvore.setSprite("sprite") (str) --> Define a sprite atual do obstáculo

class Obstaculo():
    def __init__(self):
        self.hitbox = None
        self.sprite = None
    
    def setHitbox(self, altura, largura):
        self.hitbox = [[[] for _ in range(largura)] for _ in range(altura)]
    
    def setSprite(self, sprite):
        self.sprite = sprite