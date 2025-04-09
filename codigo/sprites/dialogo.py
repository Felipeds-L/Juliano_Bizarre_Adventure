import pygame
from configuracoes import *

class Dialogo:
    def __init__(self, display, fonte_path="graficos/fontes/Pixelate-Regular.ttf", tamanho=27, tempo_letra=30, duracao_total=4000):
        self.display = display
        self.fonte = pygame.font.Font(fonte_path, tamanho)
        self.tempo_letra = tempo_letra
        self.duracao_total = duracao_total
        self.frases = []
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

    def update(self):
        if not self.exibindo:
            return

        agora = pygame.time.get_ticks()

        if self.tempo_fim is not None and agora >= self.tempo_fim:
            self.exibindo = False
            return

        for i in range(len(self.frases)):
            if agora >= self.proximo_char_times[i] and self.char_indices[i] < len(self.frases[i]):
                self.textos_renderizados[i] += self.frases[i][self.char_indices[i]]
                self.char_indices[i] += 1
                self.proximo_char_times[i] = agora + self.tempo_letra

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

        y_offset = 0
        for i, texto in enumerate(self.textos_renderizados):
            linhas = self.quebrar_texto(texto, largura_texto_max * 0.9)
            for linha in linhas:
                superficie = self.fonte.render(linha, True, (255, 255, 255))
                pos_x = self.caixa_rect.x + margem_x
                pos_y = self.caixa_rect.y + margem_y + y_offset
                self.display.blit(superficie, (pos_x +30, pos_y +140))
                y_offset += espaco_linhas
            y_offset += espacamento_frases  # Espaço maior entre frases

    def quebrar_texto(self, texto, largura_max):
        palavras = texto.split(' ')
        linhas = []
        linha_atual = ""

        for palavra in palavras:
            teste_linha = linha_atual + palavra + " "
            tamanho_teste = self.fonte.size(teste_linha)[0]
            if tamanho_teste <= largura_max:
                linha_atual = teste_linha
            else:
                linhas.append(linha_atual.strip())
                linha_atual = palavra + " "
        linhas.append(linha_atual.strip())
        return linhas
    
