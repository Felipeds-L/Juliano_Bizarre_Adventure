import pygame
import pytmx
from pytmx.util_pygame import load_pygame

from pygame.locals import *
from configuracoes import *
from sprites.sprites import *
from entidades import *
from coletaveis import *

from tela_inicial.tela_introdução import TelaInicial
from tela_gameover.tela_gameover import TelaGameover
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
        self.tela_gameover = None

        self.batalha = None
        self.estado_anterior = None
        self.estado = 'tela_inicial'

        self.npcs = pygame.sprite.Group()
        self.coletaveis_grupo = pygame.sprite.Group()

        self.musica = Musica('codigo/audios/jojo.ogg', 1, -1)
        self.musica_batalha = Musica('codigo/audios/jojo_epico.ogg', 1, -1)
        
        ################################ CRIAÇÃO DE PERSONAGENS #############################
        # Criar Juliano
        self.juliano = Personagem()
        self.juliano.setVida(5)
        self.juliano.setNome('Juliano')

        # Criar Teobaldo
        self.teobaldo = Personagem()
        self.teobaldo.setVida(5)
        self.teobaldo.setDano(1)
        self.teobaldo.setNome('Teobaldo')

        # Criar Narcisa
        self.narcisa = Personagem()
        self.narcisa.setVida(5)
        self.narcisa.setDano(1)
        self.narcisa.setNome('Narcisa')

        # Criar Zé Carcará
        self.carcara = Personagem()
        self.carcara.setVida(6)
        self.carcara.setDano(2)
        self.carcara.setNome('Zé Carcará')
        
        self.iniciar('casa')

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

    def iniciar(self, posicao_inicial_player):
        self.mapa_tmx = load_pygame('graficos/mapa/oficial_game_map.tmx')
        self.carregar_colisao(self.mapa_tmx)

        for camada in ['Agua', 'Terra']:
            for x, y, superficie in self.mapa_tmx.get_layer_by_name(camada).tiles():
                Sprite((x * TAMANHO_TILE, y * TAMANHO_TILE), superficie, self.todas_sprites, CAMADAS_MAPA['background'])

        for obj in self.mapa_tmx.get_layer_by_name('Objetos'):
            if obj.name == 'Ponte' or obj.name == 'Girassol':
                Sprite((obj.x, obj.y), obj.image, self.todas_sprites, CAMADAS_MAPA['background'])
            else:
                Sprite((obj.x, obj.y), obj.image, self.todas_sprites)

        #Coletaveis devem ser instanciados como as entidades
        for obj in self.mapa_tmx.get_layer_by_name('Coletáveis'):
            if obj.name == 'Aveia':
                aveia = Aveia((obj.x, obj.y), self.todas_sprites)
                self.coletaveis_grupo.add(aveia)
            
            if obj.name == 'Óculos':
                oculos = Oculos((obj.x, obj.y), self.todas_sprites)
                self.coletaveis_grupo.add(oculos)
            
            if obj.name == 'Pomba Laser':
                pomba_laser = PombaLaser((obj.x, obj.y), self.todas_sprites)
                self.coletaveis_grupo.add(pomba_laser)

        for obj in self.mapa_tmx.get_layer_by_name('Entidades'):
            if obj.name == 'Player' and obj.properties['pos'] == posicao_inicial_player:
                self.player = Player((obj.x - LARGURA_PLAYER/2, obj.y - ALTURA_PLAYER/2), self.todas_sprites, self)

            if obj.name == 'Narcisa':
                narcisa = Narcisa((obj.x, obj.y), self.todas_sprites)
                self.npcs.add(narcisa)

            if obj.name == 'Teobaldo':
                teobaldo = Teobaldo((obj.x, obj.y), self.todas_sprites)
                self.npcs.add(teobaldo)

            if obj.name == 'Carcará':
                carcara = Carcara((obj.x, obj.y), self.todas_sprites)
                self.npcs.add(carcara)

    def resetar_jogo(self):
        self.juliano.setVida(self.juliano.vidaCheia)
        self.teobaldo.setVida(self.teobaldo.vidaCheia)
        self.narcisa.setVida(self.narcisa.vidaCheia)
        self.carcara.setVida(self.carcara.vidaCheia)

        self.todas_sprites.empty()
        self.npcs.empty()
        self.coletaveis_grupo.empty()

        self.batalha = None
        self.iniciar('casa')

    def update(self):
        self.fps.tick(FPS)

        if self.estado != self.estado_anterior:
            self.tocar_musica()
            self.estado_anterior = self.estado

        if self.estado == 'jogando':
            self.todas_sprites.update()
            
            if self.juliano.getVida() <= 0:
                self.estado = 'game_over'
        elif self.estado == 'batalha' and self.batalha:
            self.batalha.update()

        self.verificar_colisao_npcs() 
        self.verificar_colisao_coletaveis()

    def verificar_colisao_npcs(self):
        colisoes = pygame.sprite.spritecollide(self.player, self.npcs, False)
        if colisoes and self.estado == 'jogando':
            npc = colisoes[-1] 
            self.comecar_batalha(npc)

    def verificar_colisao_coletaveis(self):
        colisao_coletaveis = pygame.sprite.spritecollide(self.player, self.coletaveis_grupo, False)
        if colisao_coletaveis and self.estado == 'jogando':
            coletou = colisao_coletaveis[-1]
            if isinstance(coletou, Aveia):
                self.juliano.pegar_aveia()
                self.juliano.curar()
                self.remover_coletavel(coletou)

            elif isinstance(coletou, Oculos):
                self.juliano.pegarOculos()
                self.remover_coletavel(coletou)
                self.player.mudar_spritesheet("graficos/personagens/juliano_oculos_redimensionado.png")
            
            elif isinstance(coletou, PombaLaser):
                self.juliano.pegarPombaLaser()
                self.remover_coletavel(coletou)

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
            if self.estado_anterior == 'batalha':
                self.musica.retomar_musica()
            else:
                self.musica.tocar_musica()

        elif self.estado == 'batalha':
            self.musica.pausar_musica()
            self.musica_batalha.tocar_musica()

    def tela_inicial(self):
        if self.tela_inicial_obj is None:  
            self.tela_inicial_obj = TelaInicial(self)
        self.tela_inicial_obj.desenhar()

    def tela_game_over(self):
        if self.tela_gameover is None:
            self.tela_gameover = TelaGameover(self)
        self.tela_gameover.desenhar()
    
    def remover_npc(self, nome_npc):
        for npc in self.npcs:
            if hasattr(npc, "nome") and npc.nome == nome_npc:
                pos_x = int(npc.rect.x // TAMANHO_TILE)
                pos_y = int(npc.rect.y // TAMANHO_TILE)

                if 0 <= pos_x < len(self.mapa_colisao) and 0 <= pos_y < len(self.mapa_colisao[0]):
                    self.mapa_colisao[pos_x][pos_y] = False

                npc.kill()
                break
    
    def remover_coletavel(self, coletavel):
        pos_x = int(coletavel.rect.x // TAMANHO_TILE)
        pos_y = int(coletavel.rect.y // TAMANHO_TILE)

        if 0 <= pos_x < len(self.mapa_colisao) and 0 <= pos_y < len(self.mapa_colisao[0]):
            self.mapa_colisao[pos_x][pos_y] = False

        coletavel.kill()
    
    def run(self):
        while True:
            teclas = pygame.key.get_pressed()

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT or teclas[pygame.K_ESCAPE]:
                    pygame.quit()
                    sys.exit()
                
                if self.estado == 'tela_inicial' and self.tela_inicial_obj:
                    self.tela_inicial_obj.verificar_clique(evento)

                elif self.estado == 'game_over' and self.tela_gameover:
                    self.tela_gameover.verificar_clique(evento)

                elif self.estado == 'batalha' and self.batalha:
                    self.batalha.tratar_eventos(evento)

            if self.estado == 'tela_inicial' and self.tela_inicial_obj:
                if self.tela_inicial_obj.mouse_sobre_botao():
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                else:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

            elif self.estado == 'game_over' and self.tela_gameover:
                if self.tela_gameover.mouse_sobre_botao():
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                else:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

            self.update()
            self.desenhar()
            pygame.display.update()