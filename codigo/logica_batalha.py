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
        self.vida_player = self.player.getVida()
        self.vida_oponente = self.oponente.getVida()

        if self.vida_player <= 0:
            self.jogo.estado = 'game_over'
            self.jogo.batalha = None
        elif self.vida_oponente <= 0:
            self.jogo.remover_npc(self.oponente.getNome())
            self.jogo.batalha = None
            self.jogo.estado = 'jogando'

    def desenhar(self):
        ########################## COMEÇANDO A TRANSIÇÃO #########################
        if self.iniciando:
            tempo_atual = pygame.time.get_ticks()

            # Alterna entre preto e a tela piscando
            if tempo_atual - self.ultimo_flash >= self.intervalo_flash:
                self.flash_mostrando = not self.flash_mostrando
                self.ultimo_flash = tempo_atual

            if self.flash_mostrando:
                self.jogo.display.fill(PRETO)
                self.jogo.todas_sprites.desenhar(self.jogo.player.rect.center)
            else:
                self.jogo.display.fill(PRETO)

            # Se passou o tempo da transição, sair do modo iniciando
            if tempo_atual - self.tempo_inicio > 2700:
                self.iniciando = False

            return  # não desenha o resto da batalha ainda

        ##################### BATALHA #########################################
        self.display.blit(self.background, self.rect)

        vida_player_texto = self.font.render(f"Vida Player: {self.vida_player}", True, (255, 255, 255))
        vida_oponente_texto = self.font.render(f"Vida {self.oponente.getNome()}: {self.vida_oponente}", True, (255, 255, 255))
        self.display.blit(vida_player_texto, (10, 10))
        self.display.blit(vida_oponente_texto, (10, 40))

        if self.cont_rodada % 2 == 0:
            opcoes_lista = self.player.listaAtaques

            for i, opcao in enumerate(opcoes_lista):
                cor = (255, 255, 0) if i == self.opcao_selecionada else (255, 255, 255)
                texto = self.font.render(opcao, True, cor)
                self.display.blit(texto, (JANELA_LARGURA // 2 - texto.get_width() // 2, JANELA_ALTURA // 2 + i * 50))  
        else:
            vez_oponente_texto = self.font.render(f"Vez de {self.oponente.getNome()}", True, (255, 0, 0))
            self.display.blit(vez_oponente_texto, (JANELA_LARGURA // 2 - vez_oponente_texto.get_width() // 2, JANELA_ALTURA // 2))

    def tratar_eventos(self, evento):
        if self.iniciando:
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

                    ########## BICADA É ATAQUE BÁSICO E PODE SER USADO SEMPRE ############
                    if ataque_selecionado == 'Bicada':
                        self.oponente.sofrerDano(1)
                        self.cont_rodada += 1

                    ########### POMBA LASER SÓ PODE SER USADO 2X POR BATALHA, PRECISA DE UM POP-UP AVISANDO QUE NÃO HÁ MAIS MUNIÇÃO E NÃO PASSA A VEZ PARA O OPONENTE AINDA #################
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