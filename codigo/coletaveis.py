
import pygame

from configuracoes import *

class Aveia(pygame.sprite.Sprite):
    def __init__(self, posicao, grupos):
        super().__init__(grupos)
        self.z = CAMADAS_MAPA['main']

        self.nome = "Aveia"

        self.image = pygame.image.load('graficos/objetos/aveia.png').convert_alpha()

        self.rect = self.image.get_frect(center = posicao)
        self.y_ordenar = self.rect.centery
        self.rect.x = posicao[0]
        self.rect.y = posicao[1]

        self.hitbox = self.rect.inflate(-20, -20)

class PombaLaser(pygame.sprite.Sprite):
    def __init__(self, posicao, grupos):
        super().__init__(grupos)
        self.z = CAMADAS_MAPA['main']

        self.nome = "pomba laser"

        self.image = pygame.image.load('graficos/objetos/pomba_laser.png').convert_alpha()

        self.rect = self.image.get_frect(center = posicao)
        self.y_ordenar = self.rect.centery +40
        self.rect.x = posicao[0]
        self.rect.y = posicao[1]

        self.hitbox = self.rect.inflate(-20, -20)

class Oculos(pygame.sprite.Sprite):
    def __init__(self, posicao, grupos):
        super().__init__(grupos)
        self.z = CAMADAS_MAPA['main']

        self.nome = "oculos"

        self.image = pygame.image.load('graficos/objetos/óculos.png').convert_alpha()

        self.rect = self.image.get_frect(center = posicao)
        self.y_ordenar = self.rect.centery +40
        self.rect.x = posicao[0]
        self.rect.y = posicao[1]

        self.hitbox = self.rect.inflate(-20, -20)
