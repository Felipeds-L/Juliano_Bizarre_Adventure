import pygame

class Musica():
    def __init__(self, musica, volume, loop):
        super().__init__()
        self.tocar_musica(musica, volume, loop)
        

    def tocar_musica(self, musica, volume, loop):
        pygame.mixer.music.load(musica)
        pygame.mixer.music.set_volume(volume)          
        pygame.mixer.music.play(loop) 