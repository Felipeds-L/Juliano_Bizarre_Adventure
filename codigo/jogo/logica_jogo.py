import pygame
from pygame.locals import *
from jogo.sprites import *
from configs.configuracoes import *
from classes.personagens import Personagem

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
        self.todas_sprites = pygame.sprite.LayeredUpdates()
        self.sprite_arvore = pygame.sprite.LayeredUpdates()
        
        ######### CRIA O MAPA ###########
        self.mapa = Mapa(self)

        ########## CRIA JULIANO E DEFINE SUA SPRITE #############
        juliano = Personagem()
        juliano.setSprite(Player(self, JANELA_LARGURA/2, JANELA_ALTURA/2))

    ################### ATUALIZA AS SPRITES DO JOGO EM TODOS CICLOS ###################
    def update_sprites(self):
        self.todas_sprites.update()
    
    ################### ATUALIZA O MAPA EM TODOS CICLOS ###################
    def update_mapa(self):
        self.display.fill((0, 0, 0))
        self.display.blit(self.mapa.image, (self.mapa.rect.x, self.mapa.rect.y))
        self.todas_sprites.draw(self.display)
        self.fps.tick(FPS)

    ################### FIM DE JOGO ###################
    def game_over(self):
        pass
    
    ################### TELA DE START ###################
    def tela_introducao(self):
        pass
    
    ################### JOGO RODANDO ATÉ SER FECHADO ###################
    def run(self):
        while self.jogando:

            ################# FECHA O JOGO #################
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    self.jogando = False
                    self.running = False

            self.update_sprites()
            self.update_mapa()
            pygame.display.update()