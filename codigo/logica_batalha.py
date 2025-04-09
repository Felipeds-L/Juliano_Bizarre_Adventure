import pygame
from pygame.locals import *
from configuracoes import *
from logica_jogo import *
from sprites.dialogo import Dialogo

class Batalha:
    def __init__(self, jogo, player, oponente):
        self.jogo = jogo
        self.display = jogo.display
        self.font = pygame.font.Font(None, 36)
        self.background = pygame.image.load('graficos/backgrounds_batalha/forest.png').convert_alpha()
        self.rect = self.background.get_rect()

        self.iniciando = True
        self.tempo_inicio = pygame.time.get_ticks()
        self.intervalo_flash = 130
        self.flash_mostrando = True
        self.ultimo_flash = pygame.time.get_ticks()

        self.cont_rodada = 0
        self.opcao_selecionada = 0
        self.contador_pomba = 0

        self.player = player
        self.oponente = oponente
        self.vida_player = self.player.getVida()
        self.vida_oponente = self.oponente.getVida()

        self.dialogo_narcisa_mostrado = None
        
        self.desenhar()

    def update(self):
        self.vida_player = self.player.getVida()
        self.vida_oponente = self.oponente.getVida()

        # Sempre atualiza o diálogo, se estiver sendo exibido
        if self.jogo.dialogo.exibindo:
            self.jogo.dialogo.update()

        # Verificações de fim de batalha
        if self.vida_player <= 0:
            self.jogo.estado = 'game_over'
            self.jogo.batalha = None
            return

        elif self.vida_oponente <= 0:
            nome_oponente = self.oponente.getNome()
            if nome_oponente == 'Narcisa':
                self.jogo.estado = 'escolha_narcisa'
                self.jogo.batalha = self
            else:
                self.jogo.remover_npc(nome_oponente)
                self.jogo.estado = 'jogando'
                self.jogo.batalha = None

    def desenhar(self):
        if self.iniciando:
            tempo_atual = pygame.time.get_ticks()
            if tempo_atual - self.ultimo_flash >= self.intervalo_flash:
                self.flash_mostrando = not self.flash_mostrando
                self.ultimo_flash = tempo_atual

            if self.flash_mostrando:
                self.jogo.display.fill(PRETO)
                self.jogo.todas_sprites.desenhar(self.jogo.player.rect.center)
            else:
                self.jogo.display.fill(PRETO)

            if tempo_atual - self.tempo_inicio > 2700:
                self.iniciando = False
            return

        if self.jogo.estado == 'batalha':
            self.display.blit(self.background, self.rect)

            vida_player_txt = self.font.render(f"Vida Player: {self.vida_player}", True, (255, 255, 255))
            vida_oponente_txt = self.font.render(f"Vida {self.oponente.getNome()}: {self.vida_oponente}", True, (255, 255, 255))

            self.display.blit(vida_player_txt, (10, 10))
            self.display.blit(vida_oponente_txt, (10, 40))

            if self.cont_rodada % 2 == 0:
                for i, opcao in enumerate(self.player.listaAtaques):
                    cor = (255, 255, 0) if i == self.opcao_selecionada else (255, 255, 255)
                    texto = self.font.render(opcao, True, cor)
                    self.display.blit(texto,(JANELA_LARGURA // 2 - texto.get_width() // 2, JANELA_ALTURA // 2 + i * 50))
            else:
                texto_oponente = self.font.render(f"Vez de {self.oponente.getNome()}",True,(255, 0, 0))
                self.display.blit(texto_oponente,(JANELA_LARGURA // 2 - texto_oponente.get_width() // 2, JANELA_ALTURA // 2))

        elif self.jogo.estado == 'escolha_narcisa':
            if not self.dialogo_narcisa_mostrado:
                self.jogo.dialogo.mostrar(["1. Narcisa, até que você é gatinha!",
                                           "2. Morra! Vou comer girassol sozinho!"], duracao=None)
                self.dialogo_narcisa_mostrado = True

        # Sempre desenha o diálogo, se estiver ativo
        if self.jogo.dialogo.exibindo:
            self.jogo.dialogo.desenhar()

    def tratar_eventos(self, evento):
        if self.iniciando:
            return

        if self.jogo.estado == 'escolha_narcisa':
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_1:
                    self.jogo.romance = True
                    self.jogo.dialogo.exibindo = False 
                    self.jogo.remover_npc(self.oponente.getNome())
                    self.jogo.batalha = None
                    self.jogo.estado = 'jogando'

                elif evento.key == pygame.K_2:
                    self.jogo.romance = False
                    self.jogo.dialogo.exibindo = False  
                    self.jogo.remover_npc(self.oponente.getNome())
                    self.jogo.batalha = None
                    self.jogo.estado = 'jogando'
            return  # Evita processar outros eventos

        if evento.type == pygame.KEYDOWN:
            if self.cont_rodada % 2 == 0:  
                opcoes_lista = self.player.listaAtaques

                if evento.key == pygame.K_UP:
                    self.opcao_selecionada = max(0, self.opcao_selecionada - 1)

                elif evento.key == pygame.K_DOWN:
                    self.opcao_selecionada = min(len(opcoes_lista) - 1, self.opcao_selecionada + 1)

                elif evento.key == pygame.K_RETURN:
                    ataque_selecionado = opcoes_lista[self.opcao_selecionada]

                    if ataque_selecionado == 'Bicada':
                        self.oponente.sofrerDano(1)
                        self.cont_rodada += 1

                    elif ataque_selecionado == 'Pomba Laser' and self.contador_pomba < 2:
                        self.oponente.sofrerDano(2)
                        self.contador_pomba += 1
                        self.cont_rodada += 1

                    elif ataque_selecionado == 'Pomba Laser' and self.contador_pomba >= 2:
                        self.oponente.sofrerDano(0)

                    elif ataque_selecionado == 'Intimidar':
                        if self.oponente.dano > 1:
                            self.oponente.dano -= 1
                        self.cont_rodada += 1

            elif self.cont_rodada % 2 == 1:
                self.player.sofrerDano(self.oponente.getDano())
                self.cont_rodada += 1
