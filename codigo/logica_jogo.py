import pygame
import pytmx
from pygame.locals import *
from pytmx.util_pygame import load_pygame

from configuracoes import *
from sprites.sprites import *
from entidades import Player
from sprites.grupos import TodasSprites

import sys



class Jogo:
    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode((JANELA_LARGURA, JANELA_ALTURA))
        self.nome_display = pygame.display.set_caption(JANELA_NOME)
        self.fps = pygame.time.Clock()

        self.todas_sprites = TodasSprites()
    
        self.importar_graficos()
        self.iniciar(self.mapa_tmx, 'casa')
    
    def importar_graficos(self):
        self.mapa_tmx = load_pygame('graficos/mapa/oficial_game_map.tmx')
    
    def iniciar(self, mapa_tmx, posicao_inicial_player):
        for camada in ['Agua', 'Terra']:
            for x, y, superficie in mapa_tmx.get_layer_by_name(camada).tiles():
                Sprite((x * TAMANHO_TILE, y * TAMANHO_TILE), superficie, self.todas_sprites, CAMADAS_MAPA['background'])
        
        for obj in mapa_tmx.get_layer_by_name('Objetos'):
            if obj.name == 'Ponte':
                Sprite((obj.x, obj.y), obj.image, self.todas_sprites, CAMADAS_MAPA['background'])
            else:
                Sprite((obj.x, obj.y), obj.image, self.todas_sprites)
        
        for obj in mapa_tmx.get_layer_by_name('Entidades'):
            if obj.name == 'Player' and obj.properties['pos'] == posicao_inicial_player:
                self.player = Player((obj.x, obj.y), self.todas_sprites)
    
    def update(self):
        self.fps.tick(FPS)
        self.todas_sprites.update()

    def desenhar(self):
        self.display.fill(PRETO) 
        self.todas_sprites.desenhar(self.player.rect.center)

    def tela_inicial(self):
        pass

    def tela_game_over(self):
        pass

    def run(self):
        while True:
            
            botao = pygame.key.get_pressed()
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT or botao[pygame.K_ESCAPE]:
                    pygame.quit()
                    sys.exit()
                    
            self.update()
            self.desenhar()
            pygame.display.update()