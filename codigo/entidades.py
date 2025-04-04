import pygame
from pygame.locals import *

from configuracoes import *

class Player(pygame.sprite.Sprite):
    def __init__(self, posicao, grupos):
        super().__init__(grupos)
        self.z = CAMADAS_MAPA['main']
        
        self.spritesheet = pygame.image.load("graficos/personagens/juliano_spritesheet.png").convert_alpha()
        self.spritesheet = [
                        [self.spritesheet.subsurface(0, 0, LARGURA_PLAYER, ALTURA_PLAYER), self.spritesheet.subsurface(LARGURA_PLAYER, 0, LARGURA_PLAYER, ALTURA_PLAYER)],
                        [self.spritesheet.subsurface(0, ALTURA_PLAYER, LARGURA_PLAYER, ALTURA_PLAYER), self.spritesheet.subsurface(LARGURA_PLAYER, ALTURA_PLAYER, LARGURA_PLAYER, ALTURA_PLAYER)]
                      ]
        
        self.direcao = 'direita'
        self.image = self.spritesheet[0][0]

        self.contador_frame = 0
        self.sprite_atual = 0

        self.rect = self.image.get_frect(center = posicao)
        self.y_ordenar = self.rect.centery
        self.rect.x = posicao[0]
        self.rect.y = posicao[1]

        self.update()

    def update(self, *args):
        self.y_ordenar = self.rect.centery
        self.movimento()
        self.virar_player()

    def movimento(self):
        self.novo_x = 0
        self.novo_y = 0
        botao = pygame.key.get_pressed()

        if botao[pygame.K_a]:
            self.novo_x += VELOCIDADE_PLAYER
            self.direcao = 'esquerda'
        if botao[pygame.K_w]:
            self.novo_y += VELOCIDADE_PLAYER
        if botao[pygame.K_s]:
            self.novo_y -= VELOCIDADE_PLAYER
        if botao[pygame.K_d]:
            self.novo_x -= VELOCIDADE_PLAYER
            self.direcao = 'direita'

        self.rect.x -= self.novo_x
        self.rect.y -= self.novo_y
    
    def virar_player(self):
        botao = pygame.key.get_pressed()
        direita, esquerda = 0, 1

        if botao[pygame.K_a] or botao[pygame.K_w] or botao[pygame.K_s] or botao[pygame.K_d]:
            self.contador_frame += 1

            if self.contador_frame > VELOCIDADE_ANIMACAO:
                self.contador_frame = 0
                self.sprite_atual = (self.sprite_atual + 1) % 2
        else:
            self.sprite_atual = 0
            
        if self.direcao == 'direita':
            self.image = self.spritesheet[direita][self.sprite_atual]
        elif self.direcao == 'esquerda':
            self.image = self.spritesheet[esquerda][self.sprite_atual]

    