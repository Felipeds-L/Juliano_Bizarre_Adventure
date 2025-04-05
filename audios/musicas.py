import pygame

class musicaJojo():
    def __init__(self, musica, volume, loop):
        self.tocar_musica(musica, volume, loop)
        

    def tocar_musica(self, musica, volume, loop):
        pygame.mixer.music.load(musica)
        pygame.mixer.music.set_volume(volume)          
        pygame.mixer.music.play(loop) 