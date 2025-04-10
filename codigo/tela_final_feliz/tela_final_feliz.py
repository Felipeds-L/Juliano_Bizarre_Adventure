import pygame
from configuracoes import *

class TelaFeliz:
    def __init__(self, jogo):
        self.jogo = jogo
        self.fundo = pygame.Surface((JANELA_LARGURA, JANELA_ALTURA))
        self.fundo = pygame.image.load('codigo/tela_final_feliz/tela_final_feliz.png').convert_alpha()
        self.fundo_rect = self.fundo.get_rect()

    def desenhar(self):
        self.jogo.display.blit(self.fundo,  self.fundo_rect)