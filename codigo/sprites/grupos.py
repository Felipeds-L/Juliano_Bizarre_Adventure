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

        background_sprites = [sprite for sprite in self if sprite.z < CAMADAS_MAPA['main']]
        main_sprites = sorted([sprite for sprite in self if sprite.z == CAMADAS_MAPA['main']], key=lambda sprite: sprite.y_ordenar)

        for camada in (background_sprites, main_sprites):
            for sprite in camada:
                self.display.blit(sprite.image, sprite.rect.topleft + self.offset)