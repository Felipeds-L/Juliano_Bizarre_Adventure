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

        ########## VARIÁVEIS DA TRANSIÇÃO DE TELA ###################
        self.iniciando = True
        self.tempo_inicio = pygame.time.get_ticks()
        self.intervalo_flash = 130  # tempo entre piscadas
        self.flash_mostrando = True
        self.ultimo_flash = pygame.time.get_ticks()

        ######### VARIÁVEIS DA BATALHA #############
        self.cont_rodada = 0
        self.opcao_selecionada = 0
        self.contador_pomba = 0

        ########## DADOS DO PLAYER E OPONENTE #############
        self.player = player
        self.oponente = oponente
        self.vida_player = self.player.getVida()
        self.vida_oponente = self.oponente.getVida()
        
        self.desenhar()

    def update(self):
        # Atualiza as vidas
        self.vida_player = self.player.getVida()
        self.vida_oponente = self.oponente.getVida()

        ########################### VERIFICAÇÕES DE FIM DE BATALHA ###########################
        
        # Caso o player morra
        if self.vida_player <= 0:
            self.jogo.estado = 'game_over'
            self.jogo.batalha = None
            return

        # Caso o oponente morra
        elif self.vida_oponente <= 0:
            nome_oponente = self.oponente.getNome()

            if nome_oponente == 'Narcisa':
                # Se for a Narcisa, abre a tela de escolha
                self.jogo.estado = 'escolha_narcisa'
                self.jogo.batalha = self  # mantém a batalha ativa até que o jogador escolha
            else:
                # Remove NPC normalmente e volta ao jogo
                self.jogo.remover_npc(nome_oponente)
                self.jogo.estado = 'jogando'
                self.jogo.batalha = None


    def desenhar(self):
        ########################## TRANSIÇÃO INICIAL #########################
        if self.iniciando:
            tempo_atual = pygame.time.get_ticks()

            # Alterna entre preto e tela piscando
            if tempo_atual - self.ultimo_flash >= self.intervalo_flash:
                self.flash_mostrando = not self.flash_mostrando
                self.ultimo_flash = tempo_atual

            if self.flash_mostrando:
                self.jogo.display.fill(PRETO)
                self.jogo.todas_sprites.desenhar(self.jogo.player.rect.center)
            else:
                self.jogo.display.fill(PRETO)

            # Finaliza transição após um tempo
            if tempo_atual - self.tempo_inicio > 2700:
                self.iniciando = False

            return  # Não desenha mais nada por enquanto

        ########################## ESTADO DE BATALHA #########################
        if self.jogo.estado == 'batalha':
            self.display.blit(self.background, self.rect)

            # Exibir vida dos personagens
            vida_player_txt = self.font.render(f"Vida Player: {self.vida_player}", True, (255, 255, 255))
            vida_oponente_txt = self.font.render(f"Vida {self.oponente.getNome()}: {self.vida_oponente}", True, (255, 255, 255))

            self.display.blit(vida_player_txt, (10, 10))
            self.display.blit(vida_oponente_txt, (10, 40))

            # Turno do jogador
            if self.cont_rodada % 2 == 0:
                for i, opcao in enumerate(self.player.listaAtaques):
                    cor = (255, 255, 0) if i == self.opcao_selecionada else (255, 255, 255)
                    texto = self.font.render(opcao, True, cor)
                    self.display.blit(texto,(JANELA_LARGURA // 2 - texto.get_width() // 2, JANELA_ALTURA // 2 + i * 50))

            # Turno do oponente
            else:
                texto_oponente = self.font.render(f"Vez de {self.oponente.getNome()}",True,(255, 0, 0))
                self.display.blit(texto_oponente,(JANELA_LARGURA // 2 - texto_oponente.get_width() // 2, JANELA_ALTURA // 2))

        ########################## ESCOLHA APÓS BATALHA #########################
        elif self.jogo.estado == 'escolha_narcisa':
            caixa = pygame.Rect(JANELA_LARGURA / 2 - 250, JANELA_ALTURA / 2 + 200, 500, 200)

            pygame.draw.rect(self.display, (50, 50, 50), caixa)           # fundo da caixa
            pygame.draw.rect(self.display, (255, 255, 255), caixa, 3)     # borda branca

            opcao1 = self.font.render("1. Narcisa, até que você é bem gatinha.", True, (0, 255, 0))
            opcao2 = self.font.render("2. Morra! Vou comer girassol sozinho!", True, (255, 0, 0))

            self.display.blit(opcao1, (caixa.x + 20, caixa.y + 70))
            self.display.blit(opcao2, (caixa.x + 20, caixa.y + 120))

    def tratar_eventos(self, evento):
        if self.iniciando:
            return

        if self.jogo.estado == 'escolha_narcisa':
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_1:
                    self.jogo.romance = True
                    self.jogo.remover_npc(self.oponente.getNome())
                    self.jogo.batalha = None
                    self.jogo.estado = 'jogando'

                elif evento.key == pygame.K_2:
                    self.jogo.romance = False
                    self.jogo.remover_npc(self.oponente.getNome())
                    self.jogo.batalha = None
                    self.jogo.estado = 'jogando'
            return 

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