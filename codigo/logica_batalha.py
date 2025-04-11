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

        self.turno_em_andamento = True
        self.tempo_espera_turno = pygame.time.get_ticks()
        self.estado_turno = 'anuncio'
        self.mostrar_turno_como_dialogo()
        
        self.ataque_juliano_em_espera = False
        self.ataque_juliano_info = None 

        # Sprites dos personagens
        tamanho_sprite = (240, 240)
        if self.player.oculos == False:
            self.sprite_juliano = pygame.transform.smoothscale(pygame.image.load('graficos/personagens/juliano_batalha.png').convert_alpha(),tamanho_sprite)
        else:
            self.sprite_juliano = pygame.image.load('graficos/personagens/juliano_oculos_batalha.png').convert_alpha()
            self.sprite_juliano = pygame.transform.smoothscale(self.sprite_juliano, tamanho_sprite)

        if self.oponente.nome == 'Narcisa':
            self.sprite_oponente = pygame.transform.smoothscale(pygame.image.load(f'graficos/personagens/{self.oponente.getNome().lower()}_batalha.png').convert_alpha(), tamanho_sprite)
            self.sprite_oponente = pygame.transform.flip(self.sprite_oponente, True, False)
        else:
            self.sprite_oponente = pygame.transform.smoothscale(pygame.image.load(f'graficos/personagens/{self.oponente.getNome().lower()}_batalha.png').convert_alpha(), tamanho_sprite)

        self.pos_juliano = (100, 960 - tamanho_sprite[1] - 50)
        self.pos_oponente = (1440 - tamanho_sprite[0] - 100, 960 - tamanho_sprite[1] - 50)

        # Animação de ataque
        self.animando_ataque = False
        self.tempo_ataque = 0
        self.direcao_ataque = 1
        self.pos_oponente_original = self.pos_oponente

        self.animando_ataque_juliano = False
        self.tempo_ataque_juliano = 0
        self.direcao_ataque_juliano = 1
        self.pos_juliano_original = self.pos_juliano

        self.desenhar()

    def update(self):
        self.vida_player = self.player.getVida()
        self.vida_oponente = self.oponente.getVida()

        if self.jogo.dialogo.exibindo:
            self.jogo.dialogo.update()

        if self.vida_player <= 0:
            self.jogo.estado = 'game_over'
            self.jogo.batalha = None
            return

        elif self.vida_oponente <= 0:
            nome_oponente = self.oponente.getNome()
            if nome_oponente == 'Narcisa':
                if self.jogo.estado != 'escolha_narcisa':
                    self.jogo.estado = 'escolha_narcisa'
                    self.jogo.batalha = self
            else:
                if not hasattr(self, "mensagem_vitoria_mostrada") or not self.mensagem_vitoria_mostrada:
                    self.jogo.dialogo.mostrar(["ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA ORA!!!!"], duracao=3500)
                    pygame.time.set_timer(pygame.USEREVENT + 2, 3500)
                    self.mensagem_vitoria_mostrada = True
                    self.turno_em_andamento = False
                    return

        
        if self.turno_em_andamento:
            tempo_atual = pygame.time.get_ticks()
            tempo_passado = tempo_atual - self.tempo_espera_turno

            if self.estado_turno == 'anuncio' and tempo_passado > 1000:
                if self.cont_rodada % 2 == 1:
                    nome = self.oponente.getNome()
                    self.jogo.dialogo.mostrar([f"{nome} atacou!"], duracao=None)
                    self.tempo_espera_turno = pygame.time.get_ticks()
                    self.estado_turno = 'ataque'
                else:
                    self.turno_em_andamento = False
                    self.jogo.dialogo.exibindo = False
                    self.mostrar_opcoes_batalha()

            elif self.estado_turno == 'ataque' and tempo_passado > 1000:
                self.animando_ataque = True
                self.tempo_ataque = pygame.time.get_ticks()

                self.player.sofrerDano(self.oponente.getDano())
                self.cont_rodada += 1
                self.mostrar_turno_como_dialogo()

        
        if self.animando_ataque:
            tempo_agora = pygame.time.get_ticks()
            if tempo_agora - self.tempo_ataque < 200:
                deslocamento = 5 * self.direcao_ataque
                self.pos_oponente = (self.pos_oponente[0] + deslocamento, self.pos_oponente[1])
                self.direcao_ataque *= -1
            else:
                self.animando_ataque = False
                self.pos_oponente = self.pos_oponente_original

        if self.animando_ataque_juliano:
            tempo_agora = pygame.time.get_ticks()
            if tempo_agora - self.tempo_ataque_juliano < 200:
                deslocamento = 5 * self.direcao_ataque_juliano
                self.pos_juliano = (self.pos_juliano[0] + deslocamento, self.pos_juliano[1])
                self.direcao_ataque_juliano *= -1
            else:
                self.animando_ataque_juliano = False
                self.pos_juliano = self.pos_juliano_original

    def desenhar(self):
        if self.iniciando:
            tempo_atual = pygame.time.get_ticks()
            if tempo_atual - self.ultimo_flash >= self.intervalo_flash:
                self.flash_mostrando = not self.flash_mostrando
                self.ultimo_flash = tempo_atual

            self.jogo.display.fill(PRETO)
            if self.flash_mostrando:
                self.jogo.todas_sprites.desenhar(self.jogo.player.rect.center)
            if tempo_atual - self.tempo_inicio > 2700:
                self.iniciando = False
            return

        if self.jogo.estado in ['batalha', 'escolha_narcisa']:
            self.display.blit(self.background, self.rect)

            # Sprites dos personagens na tela
            self.display.blit(self.sprite_juliano, self.pos_juliano)
            self.display.blit(self.sprite_oponente, self.pos_oponente)

            texto_vida_player = self.font.render("Juliano", True, (255, 255, 255))
            self.desenhar_barra_vida(150, 625, self.vida_player, self.player.vidaCheia)
            self.display.blit(texto_vida_player, (200, 600))

            nome_oponente = self.oponente.getNome()
            texto_vida_oponente = self.font.render(f"{nome_oponente}", True, (255, 255, 255))
            self.desenhar_barra_vida(1100, 625, self.vida_oponente, self.oponente.vidaCheia)
            self.display.blit(texto_vida_oponente, (1150, 600))

        if self.jogo.estado == 'escolha_narcisa' and not self.dialogo_narcisa_mostrado:
            self.jogo.dialogo.mostrar(["1. Narcisa, até que você é gatinha!",
                                       "2. Morra! Você ficou no meu caminho!"], duracao=None)
            self.dialogo_narcisa_mostrado = True

        if self.jogo.dialogo.exibindo:
            self.jogo.dialogo.desenhar()

    def tratar_eventos(self, evento):
        if self.iniciando:
            return

        if self.jogo.estado == 'escolha_narcisa':
            if evento.type == pygame.KEYDOWN:
                if self.jogo.estado == 'escolha_narcisa':
                    if evento.type == pygame.KEYDOWN:
                        if evento.key == pygame.K_1:
                            self.jogo.romance = True
                            self.jogo.dialogo.mostrar(["Você cativou essa xuxuzinha!"], duracao=3000)

                            # Adia a saída da batalha em 2 segundos
                            pygame.time.set_timer(pygame.USEREVENT + 1, 2500)

                        elif evento.key == pygame.K_2:
                            self.jogo.romance = False
                            self.jogo.dialogo.mostrar(["Juliano é poucas ideias e Narcisa foi assassinada!"], duracao=3000)
                            
                            pygame.time.set_timer(pygame.USEREVENT + 1, 2500)
                    return
                
        if evento.type == pygame.USEREVENT + 1:
            self.jogo.dialogo.exibindo = False
            self.jogo.remover_npc(self.oponente.getNome())
            self.jogo.batalha = None
            self.jogo.estado = 'jogando'
            pygame.time.set_timer(pygame.USEREVENT + 1, 0)
            return
        
        if evento.type == pygame.USEREVENT + 2:
            self.jogo.dialogo.exibindo = False
            self.jogo.remover_npc(self.oponente.getNome())
            self.jogo.batalha = None
            self.jogo.estado = 'jogando'
            pygame.time.set_timer(pygame.USEREVENT + 2, 0)
            return
        
        if evento.type == pygame.KEYDOWN:
            if self.cont_rodada % 2 == 0:
                opcoes_lista = self.player.listaAtaques

                if evento.key == pygame.K_UP:
                    self.opcao_selecionada = max(0, self.opcao_selecionada - 1)
                    self.mostrar_opcoes_batalha()

                elif evento.key == pygame.K_DOWN:
                    self.opcao_selecionada = min(len(opcoes_lista) - 1, self.opcao_selecionada + 1)
                    self.mostrar_opcoes_batalha()

                elif evento.key == pygame.K_RETURN:
                    ataque_selecionado = opcoes_lista[self.opcao_selecionada]

                    if ataque_selecionado == 'Bicada':
                        self.oponente.sofrerDano(1)
                        self.animando_ataque_juliano = True
                        self.tempo_ataque_juliano = pygame.time.get_ticks()
                        self.cont_rodada += 1
                        self.mostrar_turno_como_dialogo()

                    elif ataque_selecionado == 'Pomba Laser' and self.contador_pomba < 2:
                        self.oponente.sofrerDano(2)
                        self.animando_ataque_juliano = True
                        self.tempo_ataque_juliano = pygame.time.get_ticks()
                        self.cont_rodada += 1
                        self.contador_pomba += 1
                        self.mostrar_turno_como_dialogo()

                    elif ataque_selecionado == 'Pomba Laser' and self.contador_pomba >= 2:
                        self.oponente.sofrerDano(0)
                        self.jogo.dialogo.mostrar(['O pombo tá com o butico esgotado, deixe-o descansar para a próxima batalha!'])

                    elif ataque_selecionado == 'Intimidar':
                        if self.oponente.dano > 1:
                            self.oponente.dano -= 1
                        self.cont_rodada += 1
                        self.mostrar_turno_como_dialogo()

    def mostrar_opcoes_batalha(self):
        opcoes = []
        for i, opcao in enumerate(self.player.listaAtaques):
            prefixo = ">> " if i == self.opcao_selecionada else "   "
            opcoes.append(f"{prefixo}{opcao}")

        self.jogo.dialogo.mostrar(opcoes, duracao=None)

    def mostrar_turno_como_dialogo(self):
        nome = "Juliano" if self.cont_rodada % 2 == 0 else self.oponente.getNome()
        self.jogo.dialogo.mostrar([f"Vez de {nome}"], duracao=None)
        self.tempo_espera_turno = pygame.time.get_ticks()
        self.turno_em_andamento = True
        self.estado_turno = 'anuncio'

    def desenhar_barra_vida(self, x, y, vida_atual, vida_maxima, largura=200, altura=20):
        proporcao = vida_atual / vida_maxima
        largura_preenchida = int(largura * proporcao)

        pygame.draw.rect(self.display, (29, 55, 89), (x-10, y-35, 220, 70))
        pygame.draw.rect(self.display, (255, 0, 0), (x, y, largura, altura))
        pygame.draw.rect(self.display, (0, 255, 0), (x, y, largura_preenchida, altura))
        pygame.draw.rect(self.display, (255, 255, 255), (x, y, largura, altura), 2)
