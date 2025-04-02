from configuracoes import *

class Sprite(pygame.sprite.Sprite):
    def __init__(self, posicao, superficie, grupos):
        super().__init__(grupos)
        self.image = superficie
        self.rect = self.image.get_frect(topleft = posicao)