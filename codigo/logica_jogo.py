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
        self.mapa_colisao = [] 
        self.iniciar(self.mapa_tmx, 'casa')

    def carregar_colisao(self, mapa_tmx):
        self.mapa_colisao = [
            [False for _ in range(mapa_tmx.height)] 
            for _ in range(mapa_tmx.width)
        ]
        
        colisao_layer = mapa_tmx.get_layer_by_name('Colisões')
        if colisao_layer and hasattr(colisao_layer, 'objects'):
            print(f"Camada 'Colisões' encontrada com {len(colisao_layer.objects)} objetos")
            for obj in colisao_layer.objects:
                print(f"Objeto: x={obj.x}, y={obj.y}, width={obj.width}, height={obj.height}")
                start_x = int(obj.x // TAMANHO_TILE)
                start_y = int(obj.y // TAMANHO_TILE)
                end_x = int((obj.x + obj.width) // TAMANHO_TILE) + 1
                end_y = int((obj.y + obj.height) // TAMANHO_TILE) + 1
                
                for x in range(max(0, start_x), min(end_x, len(self.mapa_colisao))):
                    for y in range(max(0, start_y), min(end_y, len(self.mapa_colisao[0]))):
                        self.mapa_colisao[x][y] = True
        else:
            print("Erro: Camada 'Colisões' não encontrada ou não contém objetos!")
        
        print("Mapa de colisão carregado:", self.mapa_colisao)

    def importar_graficos(self):
        self.mapa_tmx = load_pygame('graficos/mapa/oficial_game_map.tmx')

    def iniciar(self, mapa_tmx, posicao_inicial_player):
        self.carregar_colisao(mapa_tmx)

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
                self.player = Player((obj.x, obj.y), self.todas_sprites, self)

    def verificar_colisao(self, rect):
        if not hasattr(self, 'mapa_colisao'):
            return False
            
        
        pontos = [
            (rect.left, rect.top),     
            (rect.right, rect.top),     
            (rect.left, rect.bottom),   
            (rect.right, rect.bottom),  
            (rect.centerx, rect.centery) 
        ]
        
        for px, py in pontos:
            tile_x = px // TAMANHO_TILE
            tile_y = py // TAMANHO_TILE
            
            if 0 <= tile_x < len(self.mapa_colisao) and 0 <= tile_y < len(self.mapa_colisao[0]):
                if self.mapa_colisao[tile_x][tile_y]:
                    return True
        return False
    
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