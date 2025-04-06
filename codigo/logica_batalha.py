import pygame
from pygame.locals import *
from configuracoes import *
from logica_jogo import *

class Batalha:
    def __init__(self, jogo, player, oponente):
        self.jogo = jogo
        self.display = jogo.display
        self.font = pygame.font.Font(None, 36)
        self.background = pygame.image.load('graficos/backgrounds_batalha/forest.png').convert_alpha()
        self.rect = self.background.get_rect()

        self.cont_rodada = 0
        self.opcao_selecionada = 0

        self.vida_player = player.vidaAtual
        self.vida_oponente = oponente.vidaAtual
        self.oponente = oponente
        self.player = player

        self.iniciar_batalha()
        self.update()
        self.desenhar()

    def iniciar_batalha(self):

        self.cont_rodada = 0
        self.opcao_selecionada = 0

    def update(self):
        self.vida_player = self.player.vidaAtual
        self.vida_oponente = self.oponente.vidaAtual

        if self.vida_player <= 0:
            self.jogo.estado = 'game_over'

        elif self.vida_oponente <= 0:
            self.jogo.remover_npc(self.oponente.nome)
            self.jogo.batalha = None
            self.jogo.estado = 'jogando'

    def desenhar(self):
        self.display.blit(self.background, self.rect)

        vida_player_texto = self.font.render(f"Vida Player: {self.vida_player}", True, (255, 255, 255))
        vida_oponente_texto = self.font.render(f"Vida {self.oponente.nome}: {self.oponente.vidaAtual}", True, (255, 255, 255))
        self.display.blit(vida_player_texto, (10, 10))
        self.display.blit(vida_oponente_texto, (10, 40))

        if self.cont_rodada % 2 == 0:
            opcoes_ataque = self.player.listaAtaques
            opcoes_lista = list(opcoes_ataque.keys())
            
            for i, opcao in enumerate(opcoes_lista):
                cor = (255, 255, 0) if i == self.opcao_selecionada else (255, 255, 255)
                texto = self.font.render(opcao, True, cor)
                self.display.blit(texto, (JANELA_LARGURA // 2 - texto.get_width() // 2, JANELA_ALTURA // 2 + i * 50))  
        else:
            vez_oponente_texto = self.font.render(f"Vez de {self.oponente.nome}", True, (255, 0, 0))
            self.display.blit(vez_oponente_texto, (JANELA_LARGURA // 2 - vez_oponente_texto.get_width() // 2, JANELA_ALTURA // 2))

    def tratar_eventos(self, evento):
        if evento.type == pygame.KEYDOWN:
            if self.cont_rodada % 2 == 0:  
                opcoes_ataque = self.player.listaAtaques
                opcoes_lista = list(opcoes_ataque.keys())
                
                if evento.key == pygame.K_UP:
                    self.opcao_selecionada = max(0, self.opcao_selecionada - 1)
                elif evento.key == pygame.K_DOWN:
                    self.opcao_selecionada = min(len(opcoes_lista) - 1, self.opcao_selecionada + 1)
                elif evento.key == pygame.K_RETURN:
                    ataque = opcoes_ataque[opcoes_lista[self.opcao_selecionada]]
                    self.oponente.sofrerDano(ataque)
                    self.cont_rodada += 1

            elif self.cont_rodada % 2 == 1:  
                self.player.sofrerDano(self.oponente.dano)
                self.cont_rodada += 1