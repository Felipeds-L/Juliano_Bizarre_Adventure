import pygame
from pygame.math import Vector2 as vector 

from configuracoes import *

class TodasSprites(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display = pygame.display.get_surface()
        self.offset = vector(100,20)
    
    def desenhar(self, centro_player):
        self.offset.x = -(centro_player[0] - JANELA_LARGURA/2)
        self.offset.y = -(centro_player[1] - JANELA_ALTURA/2)

        for sprite in self:
            self.display.blit(sprite.image, sprite.rect.topleft + self.offset)