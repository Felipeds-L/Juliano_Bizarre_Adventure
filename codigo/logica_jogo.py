from configuracoes import *

class Jogo:
    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode((JANELA_LARGURA, JANELA_ALTURA))
        self.nome_display = pygame.display.set_caption(JANELA_NOME)
        self.fps = pygame.time.Clock()
        self.running = True

        self.todas_sprites = pygame.sprite.Group()

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
    
    def update(self):
        self.todas_sprites.update()

    def desenhar(self):
        self.todas_sprites.draw(self.display)

    def run(self):
        while True:
            botao = pygame.key.get_pressed()
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT or botao[pygame.K_ESCAPE]:
                    pygame.quit()
                    sys.exit()

                self.update()
                self.desenhar()
                pygame.display.update()