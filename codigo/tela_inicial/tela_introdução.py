import pygame
from configuracoes import *

class TelaInicial:
    def __init__(self, jogo):
        self.jogo = jogo
        self.fundo_intro = pygame.image.load('codigo/tela_inicial/imagem_tela_inicial.png').convert_alpha()
        self.fundo_intro = pygame.transform.scale(self.fundo_intro, (JANELA_LARGURA, JANELA_ALTURA))
        
        self.titulo = pygame.image.load('codigo/tela_inicial/titulo_jogo.png').convert_alpha()
        self.titulo_rect = self.titulo.get_rect(center=((JANELA_LARGURA // 2) - 400, JANELA_ALTURA // 4))

        self.botao_jogar = Botao((JANELA_LARGURA/2)-400, JANELA_ALTURA/2)

        self.desenhar()

    def desenhar(self):
        self.jogo.display.blit(self.fundo_intro, (0, 0))
        self.jogo.display.blit(self.titulo, self.titulo_rect)
        self.jogo.display.blit(self.botao_jogar.imagem, self.botao_jogar.rect)

    def verificar_clique(self, evento):
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if self.botao_jogar.esta_pressionado(pygame.mouse.get_pos(), pygame.mouse.get_pressed()):
                self.jogo.estado = 'jogando'
                self.jogo.tocar_musica()

    def mouse_sobre_botao(self):
        pos_mouse = pygame.mouse.get_pos()
        return self.botao_jogar.sobre_pixel(pos_mouse)

class Botao:
    def __init__(self, x, y):
        self.imagem = pygame.image.load('codigo/tela_inicial/botao_jogar.png').convert_alpha()
        self.rect = self.imagem.get_rect(center=(x, y+100))
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