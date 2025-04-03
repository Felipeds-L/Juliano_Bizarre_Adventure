import pygame
import pytmx
from pygame.math import Vector2 as vector 
from pygame.locals import *

from configuracoes import *

class Player(pygame.sprite.Sprite):
    def __init__(self, posicao, grupos):
        super().__init__(grupos)
        self.image = pygame.Surface((100, 100))
        self.image.fill(VERMELHO)
        self.rect = self.image.get_frect(center = posicao)

        self.direcao = vector()
 
    def entrada(self):
        botao = pygame.key.get_pressed()
        entrada_vetor = vector()
        if botao[pygame.K_a]:
            entrada_vetor.x -= 1
        if botao[pygame.K_w]:
            entrada_vetor.y -= 1
        if botao[pygame.K_s]:
            entrada_vetor.y += 1
        if botao[pygame.K_d]:
            entrada_vetor.x += 1 
        self.direcao = entrada_vetor
        print(entrada_vetor)

    def movimento(self, dt):
        self.rect.center += self.direcao * VELOCIDADE_PLAYER * dt

    def update(self, dt):
        self.entrada()
        self.movimento(dt)