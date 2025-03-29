#################### FUNÇÕES #@#######################
# -----> tela = Tela() <-----
#
# tela.setArea(largura, altura) (int, int) --> Define a largura e a altura da tela em pixels
# tela.setNome("nome") (str) --> Define o nome da tela do jogo

import pygame
from pygame.locals import *

pygame.init()

class Tela():
    def __init__(self):
        self.display = None
    
    def setArea(self, largura, altura):
        self.display = pygame.display.set_mode((largura, altura))
    
    def setNome(self, nome):
        pygame.display.set_caption(nome)