import pygame

################ CONFIGURAÇÕES DA JANELA ##################
JANELA_LARGURA, JANELA_ALTURA = 1440, 960
JANELA_NOME = "Juliano Bizarre Adventure"
FPS = 60

############# CONFIGURAÇÕES PLAYER #################
VELOCIDADE_ANIMACAO = 10
LARGURA_PLAYER = 62
ALTURA_PLAYER = 74
VELOCIDADE_PLAYER = 6

############ CONFIGURAÇÕES MAPA ###############
LARGURA_MAPA, ALTURA_MAPA = 2880, 5760
TAMANHO_TILE = 64

############# CORES ###################
VERMELHO = (255, 0, 0)
PRETO = (0, 0, 0)
AZUL = (0, 0, 255)

camadas_mundo = {
    'jogador' : 1,
    'mapa' : 0,
}