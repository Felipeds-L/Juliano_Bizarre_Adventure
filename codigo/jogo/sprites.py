# NESTE ARQUIVO SERÁ FEITA A SPRITE DO JOGADOR, OU SEJA, DO JULIANO!!!!
# NESTE ARQUIVO TAMBÉM TERÁ AS SPRITES DE CADA PARTE DO MAPA!!!!

import pygame
import pytmx
from pygame.locals import *
from configs.configuracoes import *
from pygame.locals import *

##################################### SPRITE DO PLAYER ###########################################
class Player(pygame.sprite.Sprite):
    def __init__(self, jogo, x, y):
        self.jogo = jogo
        self._camada = CAMADA_PLAYER
        self.grupo_sprites = self.jogo.sprite_player
        pygame.sprite.Sprite.__init__(self, self.grupo_sprites)

        ########## VARIÁVEIS DE CONTAGEM DE FRAME PARA ANIMAÇÃO ##############
        self.velocidade_animacao = 10
        self.contador_frame = 0
        self.frame_atual = 0

        ############# POSIÇÃO INICIAL DO PLAYER E SEU TAMANHO ###############
        self.x = x - (LARGURA_PLAYER/2)
        self.y = y - (ALTURA_PLAYER/2)
        self.largura = LARGURA_PLAYER
        self.altura = ALTURA_PLAYER

        ########## COMEÇA COM O PLAYER VIRADO PARA A DIREITA ###########
        self.direcao = 'direita'

        modelsheet = pygame.image.load('graficos/personagens/juliano_spritesheet.png').convert_alpha()

        ##################### SPRITES DO PLAYER QUE ESTÃO DENTRO DO PNG #########################
        self.sprites = [[modelsheet.subsurface((0, 0, self.largura, self.altura)), modelsheet.subsurface((self.largura, 0, self.largura, self.altura))],
                        [modelsheet.subsurface((0, self.altura, self.largura, self.altura)), modelsheet.subsurface((self.largura, self.altura, self.largura, self.altura))]] 

        self.update()

    ################ ATUALIZA A SPRITE DE ACORDO COM A POSIÇÃO ##################
    def update(self):
        esquerda, direita = 1, 0
        self.virar_player()

        if self.direcao == 'direita':
            self.image = self.sprites[direita][self.frame_atual]
        elif self.direcao == 'esquerda':
            self.image = self.sprites[esquerda][self.frame_atual]
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    ################ MUDA POSICAO DO PLAYER ###############
    def virar_player(self):
        botao = pygame.key.get_pressed()
        voando = botao[pygame.K_a] or botao[pygame.K_d] or botao[K_w] or botao[K_s]

        self.contador_frame += 1
        if voando:
            if self.contador_frame > self.velocidade_animacao:
                self.contador_frame = 0
                self.frame_atual = (self.frame_atual+1)%2

        if botao[pygame.K_a]:
            self.direcao = 'esquerda'
        elif botao[pygame.K_d]:
            self.direcao = 'direita'

########################################### SPRITES DOS ELEMENTOS DO MAPA ######################################
class Arvore(pygame.sprite.Sprite):
    def __init__(self, jogo, x, y):
        self.jogo = jogo

class Arbusto(pygame.sprite.Sprite):
    def __init__(self, jogo, x, y):
        self.jogo = jogo

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
        self.grupo_sprites = self.jogo.sprites_mapa
        pygame.sprite.Sprite.__init__(self, self.grupo_sprites)

        self.x = 0
        self.y = 0

        self.x_andar = 0
        self.y_andar = 0
        
        self.mapa = pytmx.load_pygame('graficos/mapa/game_mapa.tmx')
        self.largura = self.mapa.width * self.mapa.tilewidth
        self.altura = self.mapa.height * self.mapa.tileheight
        self.image = pygame.Surface((self.largura, self.altura))
        
        self.carregar_mapa()
        self.rect = self.image.get_rect()
    
    ################ SERVE PARA CARREGAR O MAPA COMO BACKGROUND ##############
    def carregar_mapa(self):
        for camada in self.mapa.visible_layers:
            if isinstance(camada, pytmx.TiledTileLayer):
                for x, y, gid in camada:
                    tile = self.mapa.get_tile_image_by_gid(gid)
                    if tile:
                        self.image.blit(tile, (x * self.mapa.tilewidth, y * self.mapa.tileheight))

    ################## ATUALIZA A POSIÇÃO DO PLAYER PÓS MOVIMENTO ##################
    def update(self):
        self.movimento()
        
        self.rect.x += self.x_andar
        self.rect.y += self.y_andar

        self.x_andar = 0
        self.y_andar = 0

    ################ TECLAS PARA MOVIMENTAR O PLAYER ###############
    def movimento(self):
        botao = pygame.key.get_pressed()

        if botao[pygame.K_a]:
            self.x_andar += VELOCIDADE_PLAYER
        if botao[pygame.K_w]:
            self.y_andar += VELOCIDADE_PLAYER
        if botao[pygame.K_s]:
            self.y_andar -= VELOCIDADE_PLAYER
        if botao[pygame.K_d]:
            self.x_andar -= VELOCIDADE_PLAYER