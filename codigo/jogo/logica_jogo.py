import pygame
from pygame.locals import *
from jogo.sprites import *
from configs.configuracoes import *
from classes.personagens import Personagem
import sys

class Jogo:
    ################### CONFIGURAÇÃO DA TELA AO INICIAR JOGO ####################
    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode((JANELA_LARGURA, JANELA_ALTURA))
        self.nome_display = pygame.display.set_caption(JANELA_NOME)
        self.fps = pygame.time.Clock()
        self.running = True

    ################### INICIA O JOGO E SEUS ELEMENTOS ###################
    def iniciar_jogo(self):
        self.jogando = True
        self.sprites_mapa = pygame.sprite.LayeredUpdates()
        self.sprite_player = pygame.sprite.LayeredUpdates()
        
        ######### CRIA O MAPA ###########
        self.mapa = Mapa(self)

        ########## CRIA JULIANO E DEFINE SUA SPRITE #############
        juliano = Personagem()
        juliano.setSprite(Player(self, JANELA_LARGURA/2, JANELA_ALTURA/2))

    ################### ATUALIZA AS SPRITES DO JOGO EM TODOS CICLOS ###################
    def update_sprites(self):
        self.sprites_mapa.update()
        self.sprite_player.update()
    
    ################### ATUALIZA O MAPA EM TODOS CICLOS ###################
    def desenhar(self):
        self.display.fill((0, 0, 0))
        self.sprites_mapa.draw(self.display)
        self.sprite_player.draw(self.display)
        self.fps.tick(FPS)
        pygame.display.update()
    
    ################### FIM DE JOGO ###################
    def game_over(self):
        pass
    
    ################### TELA DE START ###################
    def tela_introducao(self):
        pass
    
    ################### JOGO RODANDO ATÉ SER FECHADO ###################
    def run(self):
        while self.running:
            botao = pygame.key.get_pressed()
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT or botao[pygame.K_ESCAPE]:
                    self.running = False
                    self.jogando = False

            if self.jogando:
                self.update_sprites()
                self.desenhar()