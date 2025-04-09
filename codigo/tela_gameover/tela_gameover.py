import pygame
from configuracoes import *

class TelaGameover:
    def __init__(self, jogo):
        self.jogo = jogo

        self.fundo = pygame.image.load('codigo/tela_gameover/tela_gameover_juliano.png').convert_alpha()
        self.fundo_rect = self.fundo.get_rect()

        self.botao_jogar = Botao((JANELA_LARGURA/2)-325, (JANELA_ALTURA/2) + 50)

        self.desenhar()

    def desenhar(self):
        self.jogo.display.blit(self.fundo, self.fundo_rect)
        self.jogo.display.blit(self.botao_jogar.imagem, self.botao_jogar.rect)

    def verificar_clique(self, evento):
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if self.botao_jogar.esta_pressionado(pygame.mouse.get_pos(), pygame.mouse.get_pressed()):
                self.jogo.estado = 'tela_inicial'
                self.jogo.tela_inicial_obj = None
                self.jogo.tela_gameover = None 
                self.jogo.resetar_jogo()  
                pygame.mixer.music.stop()

    def mouse_sobre_botao(self):
        pos_mouse = pygame.mouse.get_pos()
        return self.botao_jogar.sobre_pixel(pos_mouse)

class Botao:
    def __init__(self, x, y):
        self.imagem = pygame.image.load('codigo/tela_gameover/Botao_playagain.png').convert_alpha()
        self.imagem = pygame.transform.scale(self.imagem, (500, 500))
        self.rect = self.imagem.get_rect(center=(x, y))
        self.mascara = pygame.mask.from_surface(self.imagem)

    def esta_pressionado(self, pos, pressionado):
        if self.sobre_pixel(pos) and pressionado[0]:
            return True
        return False
    
    def sobre_pixel(self, pos):
        offset = (pos[0] - self.rect.x, pos[1] - self.rect.y)
        if self.rect.collidepoint(pos):
            return self.mascara.get_at(offset) != 0
        return False