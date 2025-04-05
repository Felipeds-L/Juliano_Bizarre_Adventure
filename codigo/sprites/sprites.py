import pygame

from configuracoes import *

class Sprite(pygame.sprite.Sprite):
    def __init__(self, posicao, superficie, grupos, z = CAMADAS_MAPA['main']):
        super().__init__(grupos)
        self.image = superficie
        self.rect = self.image.get_rect(topleft = posicao)
        self.z = z
        self.y_ordenar = self.rect.centery