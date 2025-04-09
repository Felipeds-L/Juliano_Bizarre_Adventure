import pygame

class Musica():
    def __init__(self, musica, volume, loop):
        super().__init__()
        self.musica = musica
        self.volume = volume
        self.loop = loop
        self.posicao_pausa = 0

    def tocar_musica(self, continuar=False):
        pygame.mixer.music.load(self.musica)
        pygame.mixer.music.set_volume(self.volume)

        if continuar and self.posicao_pausa > 0:
            pygame.mixer.music.play(self.loop, start=self.posicao_pausa / 1000) 
        else:
            pygame.mixer.music.play(self.loop)

    def pausar_musica(self):
        self.posicao_pausa = pygame.mixer.music.get_pos()
        pygame.mixer.music.pause()

    def retomar_musica(self):
        self.tocar_musica(continuar=True)

    def parar_musica(self):
        self.posicao_pausa = 0
        pygame.mixer.music.stop()