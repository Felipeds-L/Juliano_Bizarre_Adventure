import pygame
from codigo.configs.configuracoes import *
from sys import exit

class Jogo():
    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode((JANELA_LARGURA, JANELA_ALTURA))
        pygame.display.set_caption(JANELA_NOME)

    def run(self):
        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            pygame.display.update()