import pygame
from configuracoes import *

class TelaFeliz:
    def __init__(self, jogo):
        self.jogo = jogo
        self.fundo_intro = pygame.Surface((JANELA_LARGURA, JANELA_ALTURA))
        
        self.fundo_intro.fill(VERDE)

    def desenhar(self):
        self.jogo.display.blit(self.fundo_intro, (0, 0))