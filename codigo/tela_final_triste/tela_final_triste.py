import pygame
from configuracoes import *

class TelaTriste:
    def __init__(self, jogo):
        self.jogo = jogo
        self.fundo = pygame.image.load('codigo/tela_final_triste/tela_final_triste.png').convert_alpha()
        self.fundo_rect = self.fundo.get_rect()
        self.alpha = 0  
        self.transicao_concluida = False
        self.dialogo_mostrado = False

    def desenhar(self):
        self.fundo.set_alpha(self.alpha)
        self.jogo.display.blit(self.fundo, self.fundo_rect)

        if self.transicao_concluida and not self.dialogo_mostrado: 
            self.jogo.dialogo.mostrar(["Juliano agora tem uma nova casa, mas parece que ela já tinha um dono, agora serão dois grandes amigos!"], duracao=10000)
            self.dialogo_mostrado = True

        if self.dialogo_mostrado:
            self.jogo.dialogo.update()
            self.jogo.dialogo.desenhar()

    def executar_transicao(self, tela_atual):
        if self.transicao_concluida:
            return 

        clock = pygame.time.Clock()

        # FADE-OUT: Apagar suavemente a tela atual
        for alpha in range(255, -1, -5):
            tela_atual.desenhar(self.jogo.player.rect.center)  # Redesenha a tela atual antes de apagar
            fade_surface = pygame.Surface((JANELA_LARGURA, JANELA_ALTURA))
            fade_surface.fill((0, 0, 0))
            fade_surface.set_alpha(255 - alpha)  # Escurece gradualmente
            self.jogo.display.blit(fade_surface, (0, 0))
            pygame.display.update()
            clock.tick(30)

        # FADE-IN: Aparecendo a nova tela
        for alpha in range(0, 256, 5):
            self.alpha = alpha
            self.jogo.display.fill((0, 0, 0))  # Fundo preto para evitar resíduos visuais
            self.desenhar()
            pygame.display.update()
            clock.tick(30)

        self.transicao_concluida = True  # Marca a transição como concluída
