from configuracoes import *

class Player(pygame.sprite.Sprite):
    def __init__(self, posicao, grupos):
        super().__init__(grupos)
        self.image = pygame.Surface((100, 100))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_frect(center = posicao)

    def entrada(self):
        botao = pygame.key.get_pressed()
        entrada_vetor = vector()
        if botao[pygame.K_a]:
            entrada_vetor.x -= VELOCIDADE_PLAYER
        if botao[pygame.K_w]:
            entrada_vetor.y -= VELOCIDADE_PLAYER
        if botao[pygame.K_s]:
            entrada_vetor.y -= VELOCIDADE_PLAYER
        if botao[pygame.K_d]:
            entrada_vetor.x += VELOCIDADE_PLAYER

    def movimento(self, dt):
        pass

    def update(self):
        self.entrada()