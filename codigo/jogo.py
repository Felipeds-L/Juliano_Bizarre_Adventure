import pygame
from configs.configuracoes import *

class Jogo():
    ###### CONFIGURAÇÃO DA TELA DO JOGO AO ABRIR ######
    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode((JANELA_LARGURA, JANELA_ALTURA))
        pygame.display.set_caption(JANELA_NOME)

    ####### IMPORTA TODAS AS SPRITES DO JOGO #######
    def importar_sprites(self):
        sprites = {}
    
    ######## COMEÇA O JOGO #########
    def run(self):

        ######### MANTÉM O JOGO RODANDO ATÉ FECHAR #########
        sair = False
        while sair == False:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    sair = True
                    
            pygame.display.update()

        ######### COMANDOS DE ANDAR #########
        entrada = pygame.key.get_pressed()
        if entrada[K_d]:
            pass
        if entrada[K_s]:
            pass
        if entrada[K_a]:
            pass
        if entrada[K_w]:
            pass