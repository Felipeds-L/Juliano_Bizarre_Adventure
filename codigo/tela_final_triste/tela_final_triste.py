import pygame
from configuracoes import *

class TelaTriste:
    def __init__(self, jogo):
        self.jogo = jogo
        self.fundo_intro = pygame.Surface((JANELA_LARGURA, JANELA_ALTURA))

        self.fundo_intro.fill(VERMELHO)

    def desenhar(self):
        self.jogo.display.blit(self.fundo_intro, (0, 0))