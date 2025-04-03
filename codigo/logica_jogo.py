import pygame
import pytmx
from pygame.locals import *
from pytmx.util_pygame import load_pygame
from sprites import *
from entidades import Player
import sys

from configuracoes import *

class Jogo:
    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode((JANELA_LARGURA, JANELA_ALTURA))
        self.nome_display = pygame.display.set_caption(JANELA_NOME)
        self.fps = pygame.time.Clock()
        self.font = pygame.font.SysFont('arial', 32)
        self.todas_sprites = pygame.sprite.Group()
        self.intro_background = pygame.image.load('./graficos/tela/introbackground.png')      
        self.running = True 

        self.importar_graficos()
        self.iniciar(self.mapa_tmx['mundo'], 'house')
    
    def importar_graficos(self):
        self.mapa_tmx = {'mundo': load_pygame('graficos/mapa/game_mapa.tmx')}
    
    def iniciar(self, mapa_tmx, posicao_inicial_player):
        for x, y, superficie in mapa_tmx.get_layer_by_name('Terrenos').tiles():
            Sprite((x * TAMANHO_TILE, y * TAMANHO_TILE), superficie, self.todas_sprites)
        
        for obj in mapa_tmx.get_layer_by_name('Entidades'):
            if obj.name == 'player' and obj.properties['pos'] == posicao_inicial_player:
                Player((obj.x, obj.y), self.todas_sprites)
                break
    
    def update(self, dt):
        self.todas_sprites.update(dt)

    def desenhar(self):
        self.display.fill(PRETO) 
        self.todas_sprites.draw(self.display)

    def tela_inicial(self):
        intro = True

        titulo = self.font.render('Juliano Bizarre Adventures', True, PRETO)
        titulo_rect = titulo.get_rect(x=10,y=10)
        botao_jogar = Botao(10,50,100,50, BRANCO, PRETO, 'Jogar', 32)
        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    intro = False
                    self.running = False
                
            mouse_pos = pygame.mouse.get_pos()
            mouse_pressionado = pygame.mouse.get_pressed()

            if botao_jogar.esta_pressionado(mouse_pos,mouse_pressionado):
                intro = False
            
            self.display.blit(self.intro_background, (0,0)) 
            self.display.blit(titulo, titulo_rect)  
            self.display.blit(botao_jogar.image, botao_jogar.rect) 
            self.fps.tick(FPS) 
            pygame.display.update()

    def tela_game_over(self):
        pass

    def run(self):
        self.tela_inicial() 
        while self.running:
            dt = self.fps.tick()/1000
            botao = pygame.key.get_pressed()
            
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT or botao[pygame.K_ESCAPE]:
                    self.running = False

            self.update(dt)
            self.desenhar()
            pygame.display.update()
        
        pygame.quit()
        sys.exit()