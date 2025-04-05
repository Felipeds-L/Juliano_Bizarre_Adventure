import pygame
from pygame.locals import *
from configuracoes import JANELA_LARGURA, JANELA_ALTURA
from logica_jogo import *

class Batalha:
    #todos os dados pra batalha
    def __init__(self, jogo):
        self.jogo = jogo
        self.display = jogo.display
        self.font = pygame.font.Font(None, 36)
        self.cont_rodada = 0
        self.opcao_selecionada = 0
        self.dicionario_monstros = {0: 'Gato', 1: 'Narcisa', 2: 'Zé carcará'}
        self.dicionario_monstros_vida = {'Gato': 100, 'Narcisa': 200, 'Zé carcará': 300}
        self.cont_monstro_atual = jogo.cont_monstro_atual if hasattr(jogo, 'cont_monstro_atual') else 0
        self.vida_player = jogo.vida_player if hasattr(jogo, 'vida_player') else 500 #isso aqui confere o bool de alguns objetos
        self.vida_monstro = 0
        self.monstro_atual = ''
        self.ataque_oculos = jogo.ataque_oculos if hasattr(jogo, 'ataque_oculos') else 20
        self.ataque_monstro = 20
        self.oculos = jogo.oculos if hasattr(jogo, 'oculos') else True
        self.pomba_laser = jogo.pomba_laser if hasattr(jogo, 'pomba_laser') else True
        self.iniciar_batalha()

    def iniciar_batalha(self):
        #questao das pontuações e atualizações de quem é o inimigo da vez
        if self.cont_monstro_atual <= 2:
            self.monstro_atual = self.dicionario_monstros[self.cont_monstro_atual]
            self.vida_monstro = self.dicionario_monstros_vida[self.monstro_atual]
            if self.oculos:
                self.vida_monstro -= self.ataque_oculos
            self.cont_rodada = 0
            self.opcao_selecionada = 0

    #isso ainda vai mudar pois se ele ganhar uma vez ele vai voltar pro estado de jogando e se colidir
    #começa a segunda batalha

    #já o game-over realmente se morrer, acaba.
    def update(self):
        if self.vida_player <= 0:
            self.jogo.estado = 'game_over'
        elif self.vida_monstro <= 0:
            self.cont_monstro_atual += 1
            self.jogo.cont_monstro_atual = self.cont_monstro_atual
            if self.cont_monstro_atual > 2:
                self.jogo.estado = 'jogando'
            else:
                self.iniciar_batalha()

    def desenhar(self):
        self.display.fill((50, 50, 50)) #Isso aqui vai ser mudado pois a batalha o personagem vai ficar de costas e etc

        #aparecer vidas na tela
        vida_player_texto = self.font.render(f"Vida Player: {self.vida_player}", True, (255, 255, 255))
        vida_monstro_texto = self.font.render(f"Vida {self.monstro_atual}: {self.vida_monstro}", True, (255, 255, 255))
        self.display.blit(vida_player_texto, (10, 10))
        self.display.blit(vida_monstro_texto, (10, 40))

        # opções de ataque (se tiver armas especiais ou etc) ou vez do monstro no meio da tela
        if self.cont_rodada % 2 == 0:
            opcoes_ataque = {'Ataque normal': 10}
            if self.pomba_laser:
                opcoes_ataque['Ataque pomba-laser'] = 20
            opcoes_lista = list(opcoes_ataque.keys())
            
            #opções de seleção
            for i, opcao in enumerate(opcoes_lista):
                cor = (255, 255, 0) if i == self.opcao_selecionada else (255, 255, 255)
                texto = self.font.render(opcao, True, cor)
                self.display.blit(texto, (JANELA_LARGURA // 2 - texto.get_width() // 2, JANELA_ALTURA // 2 + i * 50))  # Meio da tela
        else:
            vez_monstro_texto = self.font.render(f"Vez de {self.monstro_atual}", True, (255, 0, 0))
            self.display.blit(vez_monstro_texto, (JANELA_LARGURA // 2 - vez_monstro_texto.get_width() // 2, JANELA_ALTURA // 2))

    def tratar_eventos(self, evento):
        if evento.type == pygame.KEYDOWN:
            if self.cont_rodada % 2 == 0:  # Vez do player
                opcoes_ataque = {'Ataque normal': 10}
                if self.pomba_laser:
                    opcoes_ataque['Ataque pomba-laser'] = 20
                opcoes_lista = list(opcoes_ataque.keys())
                
                if evento.key == pygame.K_UP:
                    self.opcao_selecionada = max(0, self.opcao_selecionada - 1)
                elif evento.key == pygame.K_DOWN:
                    self.opcao_selecionada = min(len(opcoes_lista) - 1, self.opcao_selecionada + 1)
                elif evento.key == pygame.K_RETURN:
                    ataque = opcoes_ataque[opcoes_lista[self.opcao_selecionada]]
                    self.vida_monstro -= ataque
                    self.cont_rodada += 1

            elif self.cont_rodada % 2 == 1:  # Vez do monstro
                self.vida_player -= self.ataque_monstro
                self.jogo.vida_player = self.vida_player
                self.cont_rodada += 1