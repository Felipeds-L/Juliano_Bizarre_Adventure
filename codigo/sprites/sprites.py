import pygame

from configuracoes import *

class Sprite(pygame.sprite.Sprite):
    def __init__(self, posicao, superficie, grupos, z = CAMADAS_MAPA['main']):
        super().__init__(grupos)
        self.image = superficie
        self.rect = self.image.get_rect(topleft = posicao)
        self.z = z
        self.y_ordenar = self.rect.centery

# class Botao:
#     def __init__(self,x,y,width,height,fg,bg,content,fontsize):
#         self.font = pygame.font.Font('Roboto.ttf', fontsize)
#         self.content = content
#         self.x = x
#         self.y = y
#         self.width = width
#         self.height = height

#         self.fg = fg
#         self.bg = bg

#         self.image = pygame.Surface((self.width, self.height))
#         self.image.fill(self.bg)
#         self.rect = self.image.get_rect(topleft=(self.x, self.y))

#         self.text = self.font.render(self.content, True, self.fg)
#         self.text_rect = self.text.get_rect(center = (self.width/2, self.height/2))
#         self.image.blit(self.text, self.text_rect)
    
#     def esta_pressionado(self,pos, pressionado): #checa posição do mouse, se toca no botao, se esta pressionado (retornar true)
#         if self.rect.collidepoint(pos):
#             if pressionado[0]:
#                 return True
#             return False
#         return False