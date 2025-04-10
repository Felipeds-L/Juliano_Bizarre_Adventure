import pygame
from configuracoes import *

class Score:
    def __init__(self, display, fonte_path="graficos/fontes/Pixelate-Regular.ttf", tamanho=30):
        self.display = display
        self.fonte = pygame.font.Font(fonte_path, tamanho)
        self.texto = [": ", "/ 10"]
        self.textos_renderizados = []
        self.char_indices = []
        self.proximo_char_times = []
        self.tempo_fim = 0
        self.exibindo = False

        # Carregar imagem da caixa de diálogo
        self.caixa_img = pygame.image.load("graficos/fontes/caixa_dialogo.png").convert_alpha()
        self.caixa_rect = self.caixa_img.get_rect()
        self.caixa_rect.midbottom = (JANELA_LARGURA/ 2, JANELA_ALTURA + 80)  # Centralizado na parte inferior

    def mostrar(self, frases, duracao=None):
        self.frases = frases[:4]
        self.textos_renderizados = [""] * len(self.frases)
        self.char_indices = [0] * len(self.frases)
        agora = pygame.time.get_ticks()
        self.proximo_char_times = [agora + self.tempo_letra * i for i in range(len(self.frases))]

        if duracao is not None:
            self.tempo_fim = agora + duracao
        else:
            self.tempo_fim = agora + self.duracao_total
            self.exibindo = True
    
    def desenhar(self):
        if not self.exibindo:
            return

        # Desenha imagem da caixa
        self.display.blit(self.caixa_img, self.caixa_rect)

        # Posição inicial de texto dentro da caixa (ajuste conforme imagem)
        margem_x = 40
        margem_y = 30
        espaco_linhas = self.fonte.get_height() + 5
        largura_texto_max = self.caixa_rect.width - 2 * margem_x

        # Defina o espaçamento entre blocos de frases (após quebra de linha)
        espacamento_frases = 25 if len(self.textos_renderizados) == 2 else 10