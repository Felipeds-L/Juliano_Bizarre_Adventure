from configuracoes import *

class Player(pygame.sprite.Sprite):
    def __init__(self, posicao, grupos):
        super().__init__(grupos)
        self.image = pygame.Surface((100, 100))
        self.image.fill(VERMELHO)
        self.rect = self.image.get_frect(center = posicao)