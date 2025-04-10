import pygame
from pygame.locals import *

from configuracoes import *

class Player(pygame.sprite.Sprite):
    def __init__(self, posicao, grupos, jogo):
        super().__init__(grupos)
        self.jogo = jogo
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

        self.rect = self.image.get_rect(center = posicao)
        self.y_ordenar = self.rect.centery
        self.rect.x = posicao[0]
        self.rect.y = posicao[1]


        self.hitbox = self.rect.copy().inflate( -LARGURA_PLAYER, -ALTURA_PLAYER)
        self.update()

    def update(self, *args):
        self.y_ordenar = self.rect.centery
        self.movimento()
        self.virar_player()

    def movimento(self):
        x_original, y_original = self.hitbox.x, self.hitbox.y

        self.novo_x, self.novo_y = 0, 0
        botao = pygame.key.get_pressed()

        if botao[pygame.K_a]:
            self.novo_x = -VELOCIDADE_PLAYER  
            self.direcao = 'esquerda'
        if botao[pygame.K_d]:
            self.novo_x = VELOCIDADE_PLAYER  
            self.direcao = 'direita'
        if botao[pygame.K_w]:
            self.novo_y = -VELOCIDADE_PLAYER  
        if botao[pygame.K_s]:
            self.novo_y = VELOCIDADE_PLAYER  

        self.hitbox.x += self.novo_x
        if self.verificar_colisao(self.hitbox):  
            self.hitbox.x = x_original
        
        self.hitbox.y += self.novo_y
        if self.verificar_colisao(self.hitbox):  
            self.hitbox.y = y_original
        
        self.rect.center = self.hitbox.center

    def verificar_colisao(self, rect):
        pontos = [
            (rect.left, rect.top),
            (rect.right, rect.top),
            (rect.left, rect.bottom),
            (rect.right, rect.bottom)
        ]
        
        for px, py in pontos:
            tile_x = px // TAMANHO_TILE
            tile_y = py // TAMANHO_TILE
            
            if 0 <= tile_x < len(self.jogo.mapa_colisao) and 0 <= tile_y < len(self.jogo.mapa_colisao[0]):
                if self.jogo.mapa_colisao[tile_x][tile_y]:
                    return True
        return False
    
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

    def mudar_spritesheet(self, novo_caminho):
        nova_spritesheet = pygame.image.load(novo_caminho).convert_alpha()
        self.spritesheet = [
                        [nova_spritesheet.subsurface(0, 0, LARGURA_PLAYER, ALTURA_PLAYER), nova_spritesheet.subsurface(LARGURA_PLAYER, 0, LARGURA_PLAYER, ALTURA_PLAYER)],
                        [nova_spritesheet.subsurface(0, ALTURA_PLAYER, LARGURA_PLAYER, ALTURA_PLAYER), nova_spritesheet.subsurface(LARGURA_PLAYER, ALTURA_PLAYER, LARGURA_PLAYER, ALTURA_PLAYER)]
                      ]

class Narcisa(pygame.sprite.Sprite):
    def __init__(self, posicao, grupos):
        super().__init__(grupos)
        self.z = CAMADAS_MAPA['main']

        self.nome = "Narcisa"

        self.image = pygame.image.load('graficos/personagens/narcisa.png').convert_alpha()

        self.rect = self.image.get_frect(center = posicao)
        self.y_ordenar = self.rect.centery +40
        self.rect.x = posicao[0]
        self.rect.y = posicao[1]

        self.hitbox = self.rect.inflate(-20, -20)

class Teobaldo(pygame.sprite.Sprite):
    def __init__(self, posicao, grupos):
        super().__init__(grupos)
        self.z = CAMADAS_MAPA['main']

        self.nome = "Teobaldo"

        self.image = pygame.image.load('graficos/personagens/teobaldo_mapa.png').convert_alpha()

        self.rect = self.image.get_frect(center = posicao)
        self.y_ordenar = self.rect.centery +40
        self.rect.x = posicao[0]
        self.rect.y = posicao[1]

        self.hitbox = self.rect.inflate(-20, -20)

class Carcara(pygame.sprite.Sprite):
    def __init__(self, posicao, grupos):
        super().__init__(grupos)
        self.z = CAMADAS_MAPA['main']

        self.nome = "Zé Carcará"

        self.image = pygame.image.load('graficos/personagens/carcara_mapa.png').convert_alpha()
        self.image = pygame.transform.flip(self.image, True, False)

        self.rect = self.image.get_frect(center = posicao)
        self.y_ordenar = self.rect.centery +40
        self.rect.x = posicao[0]
        self.rect.y = posicao[1]

        self.hitbox = self.rect.inflate(-70, -70)