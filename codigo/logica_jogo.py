import pygame
import pytmx
from pytmx.util_pygame import load_pygame

from pygame.locals import *
from configuracoes import *
from sprites.sprites import *
from entidades import *

from tela_inicial.tela_introdução import TelaInicial
from logica_batalha import Batalha
from audios.musicas import Musica
from sprites.grupos import TodasSprites
from personagens import Personagem

import sys

class Jogo:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.display = pygame.display.set_mode((JANELA_LARGURA, JANELA_ALTURA))
        self.nome_display = pygame.display.set_caption(JANELA_NOME)
        self.fps = pygame.time.Clock()

        self.todas_sprites = TodasSprites()

        self.tela_inicial_obj = None

        self.batalha = None
        self.estado = 'tela_inicial'

        self.npcs = pygame.sprite.Group()
        
        ################################ CRIAÇÃO DE PERSONAGENS #############################
        # Criar Juliano
        self.juliano = Personagem()
        self.juliano.setVida(20)
        self.juliano.setNome('Juliano')

        # Criar Teobaldo
        self.teobaldo = Personagem()
        self.teobaldo.setVida(20)
        self.teobaldo.setDano(5)
        self.teobaldo.setNome('Teobaldo')

        # Criar Narcisa
        self.narcisa = Personagem()
        self.narcisa.setVida(20)
        self.narcisa.setDano(5)
        self.narcisa.setNome('Narcisa')

        # Criar Zé Carcará
        self.carcara = Personagem()
        self.carcara.setVida(20)
        self.carcara.setDano(5)
        self.carcara.setNome('Zé Carcará')

        self.importar_graficos()
        self.tocar_musica()
        self.iniciar(self.mapa_tmx, 'casa')

    def carregar_colisao(self, mapa_tmx):
        self.mapa_colisao = [[False for _ in range(mapa_tmx.height)] for _ in range(mapa_tmx.width)]

        for obj in mapa_tmx.get_layer_by_name('Colisões'):
            if obj.name == "Colisão":
                start_x = int(obj.x // TAMANHO_TILE)
                start_y = int(obj.y // TAMANHO_TILE)
                end_x = int((obj.x + obj.width) // TAMANHO_TILE) + 1
                end_y = int((obj.y + obj.height) // TAMANHO_TILE) + 1

                for x in range(max(0, start_x), min(end_x, len(self.mapa_colisao))):
                    for y in range(max(0, start_y), min(end_y, len(self.mapa_colisao[0]))):
                        self.mapa_colisao[x][y] = True
            else:
                if 0 <= start_x < mapa_tmx.width and 0 <= start_y < mapa_tmx.height:
                    self.mapa_colisao[start_x][start_y] = True

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

        for obj in mapa_tmx.get_layer_by_name('Coletáveis'):
            Sprite((obj.x, obj.y), obj.image, self.todas_sprites, CAMADAS_MAPA['background'])

        for obj in mapa_tmx.get_layer_by_name('Entidades'):
            if obj.name == 'Player' and obj.properties['pos'] == posicao_inicial_player:
                self.player = Player((obj.x - LARGURA_PLAYER/2, obj.y - ALTURA_PLAYER/2), self.todas_sprites, self)

            if obj.name == 'Narcisa':
                narcisa = Narcisa((obj.x, obj.y), self.todas_sprites)
                self.npcs.add(narcisa)

            if obj.name == 'Teobaldo':
                teobaldo = Teobaldo((obj.x, obj.y), self.todas_sprites)
                self.npcs.add(teobaldo)


    def update(self):
        self.fps.tick(FPS)
        if self.estado == 'jogando':
            self.todas_sprites.update()
        elif self.estado == 'batalha':
            self.batalha.update()

        self.verificar_colisao_npcs()

    def verificar_colisao_npcs(self):
        colisoes = pygame.sprite.spritecollide(self.player, self.npcs, False)
        if colisoes and self.estado == 'jogando':
            npc = colisoes[-1] 
            self.comecar_batalha(npc)

    def comecar_batalha(self, npc):
        self.estado = 'batalha'

        if isinstance(npc, Narcisa):
            oponente = self.narcisa
        elif isinstance(npc, Teobaldo):
            oponente = self.teobaldo
        else:
            oponente = self.carcara
    
        self.batalha = Batalha(self, self.juliano, oponente)

    def desenhar(self):
        if self.estado == 'tela_inicial':
            self.tela_inicial()

        elif self.estado == 'jogando':
            self.display.fill(PRETO)
            self.todas_sprites.desenhar(self.player.rect.center)
            
        elif self.estado == 'batalha' and self.batalha:
            self.batalha.desenhar()
            
        elif self.estado == 'game_over':
            self.tela_game_over()

    def tocar_musica(self):
        if self.estado == 'jogando':
            self.musica = Musica('codigo/audios/jojo.mp3', 0.1, -1)

    def tela_inicial(self):
        self.tela_inicial_obj = TelaInicial(self)

    def tela_game_over(self):
        self.display.fill(PRETO)
        texto = pygame.font.Font(None, 36).render("Game Over", True, (255, 255, 255))
        self.display.blit(texto, (JANELA_LARGURA // 2 - texto.get_width() // 2, JANELA_ALTURA // 2))

    def remover_npc(self, nome_npc):
        for npc in self.npcs:
            if hasattr(npc, "nome") and npc.nome == nome_npc:
                pos_x = int(npc.rect.x // TAMANHO_TILE)
                pos_y = int(npc.rect.y // TAMANHO_TILE)

                if 0 <= pos_x < len(self.mapa_colisao) and 0 <= pos_y < len(self.mapa_colisao[0]):
                    self.mapa_colisao[pos_x][pos_y] = False

                npc.kill()
                break

    def run(self):
        while True:
            teclas = pygame.key.get_pressed()

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT or teclas[pygame.K_ESCAPE]:
                    pygame.quit()
                    sys.exit()
                    
                if self.estado == 'tela_inicial' and self.tela_inicial_obj:
                    self.tela_inicial_obj.verificar_clique(evento)

                elif self.estado == 'batalha' and self.batalha:
                    self.batalha.tratar_eventos(evento)

            if self.estado == 'tela_inicial' and self.tela_inicial_obj:
                if self.tela_inicial_obj.mouse_sobre_botao():
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                else:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

            self.update()
            self.desenhar()
            pygame.display.update()