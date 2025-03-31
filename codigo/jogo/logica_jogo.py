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
        self.jogando = False 

        self.todas_sprites = pygame.sprite.LayeredUpdates()
        self.sprite_arvore = pygame.sprite.LayeredUpdates()
        
        self.mapa = pygame.image.load('graficos/mapa/mapa.png').convert()
        self.mapa_pos = [0, 0]
        
        self.juliano = Personagem()
    
    ################### INICIA O JOGO E SEUS ELEMENTOS ###################
    def iniciar_jogo(self):
        self.jogando = True
        
        ########## CRIA JULIANO E DEFINE SUA SPRITE #############
        self.juliano.setSprite(Player(self, JANELA_LARGURA//2, JANELA_ALTURA//2))

    ################### ATUALIZA O MAPA ###################
    def update_mapa(self):
        self.display.blit(self.mapa, (self.mapa_pos[0], self.mapa_pos[1]))
    
    ################### ATUALIZA TODAS AS SPRITES ###################
    def update(self):
        botao = pygame.key.get_pressed()
        velocidade = VELOCIDADE_PLAYER
        
        if botao[K_LEFT] or botao[K_a]:
            self.mapa_pos[0] += velocidade
        if botao[K_RIGHT] or botao[K_d]:
            self.mapa_pos[0] -= velocidade
        if botao[K_UP] or botao[K_w]:
            self.mapa_pos[1] += velocidade
        if botao[K_DOWN] or botao[K_s]:
            self.mapa_pos[1] -= velocidade
            
        self.todas_sprites.update()
    
    ################### DESENHA TODOS OS ELEMENTOS NA TELA ###################
    def draw(self):
        self.display.fill((0, 0, 0))
        self.update_mapa()
        self.todas_sprites.draw(self.display)
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
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    self.running = False
                    self.jogando = False
            
            if self.jogando:
                self.update()
                self.draw()
            
            self.fps.tick(FPS)