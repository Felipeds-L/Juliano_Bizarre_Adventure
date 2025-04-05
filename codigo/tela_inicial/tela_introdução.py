import pygame
from configuracoes import *

class TelaInicial:
    def __init__(self, jogo):
        self.intro_background = pygame.image.load('graficos/tela/introbackground.png').convert_alpha()
        self.intro_background = pygame.transform.scale(self.intro_background, (JANELA_LARGURA, JANELA_ALTURA))

        self.titulo = pygame.image.load('codigo/tela_inicial/titulo_jogo.png').convert_alpha()
        self.titulo_rect = self.titulo.get_rect(center = (JANELA_LARGURA // 2, JANELA_ALTURA // 4))

        self.botao_jogar = Botao(JANELA_LARGURA/2, JANELA_ALTURA/2)
        
        jogo.display.blit(self.intro_background, (0, 0)) 
        jogo.display.blit(self.titulo, self.titulo_rect)  
        jogo.display.blit(self.botao_jogar.image, self.botao_jogar.rect)  


class Botao:
    def __init__(self,x,y):
        self.image = pygame.image.load('codigo/tela_inicial/botao_jogar.png')
        self.rect = self.image.get_rect(center = (x, y+100))
        self.image.blit(self.image, (x, y+100))
    
    def esta_pressionado(self, pos, pressionado):
        if self.rect.collidepoint(pos):
            if pressionado[0]:
                return True
            return False
        return False