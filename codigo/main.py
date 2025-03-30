from jogo.logica_jogo import *

jogo = Jogo()

if __name__ == '__main__':
    jogo.tela_introducao()
    jogo.iniciar_jogo()
    jogo.run()