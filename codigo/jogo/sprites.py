# NESTE ARQUIVO SERÁ FEITA A SPRITE DO JOGADOR, OU SEJA, DO JULIANO!!!!
# NESTE ARQUIVO TAMBÉM TERÁ AS SPRITES DE CADA PARTE DO MAPA!!!!

import pygame
import math
import random
from configs.configuracoes import *
from pygame.locals import *

class Player(pygame.sprite.Sprite):
    def __init__(self, jogo, x, y):
        self.jogo = jogo
        self._camada = CAMADA_PLAYER
        self.grupo_sprites = self.jogo.todas_sprites
        pygame.sprite.Sprite.__init__(self, self.grupo_sprites)

        self.x = x - TAMANHO_PLAYER//2
        self.y = y - TAMANHO_PLAYER//2
        self.largura = TAMANHO_PLAYER
        self.altura = TAMANHO_PLAYER

        self.direcao = 'baixo'

        self.image = pygame.Surface([self.largura, self.altura])
        self.image.fill(VERMELHO)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    ################## ATUALIZA A POSIÇÃO DO PLAYER PÓS MOVIMENTO ##################
    def update(self, *args):
        """Atualiza apenas a direção do personagem"""
        botao = pygame.key.get_pressed()
        
        if botao[K_LEFT] or botao[K_a]:
            self.direcao = 'esquerda'
        elif botao[K_RIGHT] or botao[K_d]:
            self.direcao = 'direita'
        elif botao[K_UP] or botao[K_w]:
            self.direcao = 'cima'
        elif botao[K_DOWN] or botao[K_s]:
            self.direcao = 'baixo'

    ################ TECLAS PARA MOVIMENTAR O MAPA ###############
def movimento(self):
        botao = pygame.key.get_pressed()
        
        self.x_andar = 0
        self.y_andar = 0
        
        if botao[pygame.K_a]:
            for sprite in self.grupo_sprites:
                if sprite != self:
                    sprite.rect.x += self.velocidade
            self.direcao = 'esquerda'
        elif botao[pygame.K_d]:
            for sprite in self.grupo_sprites:
                if sprite != self:
                    sprite.rect.x -= self.velocidade
            self.direcao = 'direita'
        elif botao[pygame.K_w]: 
            for sprite in self.grupo_sprites:
                if sprite != self:
                    sprite.rect.y += self.velocidade
            self.direcao = 'cima'
        elif botao[pygame.K_s]:
            for sprite in self.grupo_sprites:
                if sprite != self:
                    sprite.rect.y -= self.velocidade
            self.direcao = 'baixo'

############# SPRITES DOS ELEMENTOS DO MAPA #################
class Arvore(pygame.sprite.Sprite):
    def __init__(self, jogo, x, y):
        self.jogo = jogo
        self._camada = CAMADA_OBSTACULOS
        self.grupo_sprites = self.jogo.todas_sprites
        pygame.sprite.Sprite.__init__(self, self.grupo_sprites)

        self.x = x
        self.y = y
        self.largura = TAMANHO_PLAYER
        self.altura = TAMANHO_PLAYER

        self.image = pygame.Surface([self.largura, self.altura]) 
        self.image.fill(AZUL)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class Arbusto(pygame.sprite.Sprite):
    def __init__(self, jogo, x, y):
        self.jogo = jogo
        self._camada = CAMADA_OBSTACULOS
        self.grupo_sprites = self.jogo.todas_sprites, self.jogo.sprite_arvore 
        pygame.sprite.Sprite.__init__(self, self.grupo_sprites)

class Semente(pygame.sprite.Sprite):
    def __init__(self, jogo, x, y):
        self.jogo = jogo

############ SPRITES DOS COLETÁVEIS ##################
class Oculos(pygame.sprite.Sprite):
    def __init__(self, jogo, x, y):
        self.jogo = jogo

class Aveia(pygame.sprite.Sprite):
    def __init__(self, jogo, x, y):
        self.jogo = jogo

class PombaLaser(pygame.sprite.Sprite):
    def __init__(self, jogo, x, y):
        self.jogo = jogo

############ SPRITE MAPA ##################
class Mapa(pygame.sprite.Sprite):
    def __init__(self, jogo):
        self.jogo = jogo
        self._camada = CAMADA_MAPA
        self.grupo_sprites = self.jogo.todas_sprites
        pygame.sprite.Sprite.__init__(self, self.grupo_sprites)

        self.x = 0
        self.y = 0
        self.largura = LARGURA_MAPA
        self.altura = ALTURA_MAPA

        self.image = pygame.Surface([self.largura, self.altura]) 

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y