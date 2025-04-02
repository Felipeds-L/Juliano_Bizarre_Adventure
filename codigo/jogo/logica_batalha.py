#Logica inicial batalha

#Isso vai ser pego pelas classes e sistemas, eu apenas simulei aqui
cont_monstro_atual = 0
cont_rodada = 0

vida_player = 500

ataque_oculos = 20
ataque_monstro = 20

oculos = True
pomba_laser= True

dicionario_monstros = {0: 'Gato', 1: 'Narcisa', 2: 'Zé carcará' }
dicionario_monstros_vida = {'Gato': 100, 'Narcisa': 200, 'Zé carcará': 300}

while cont_monstro_atual <= 2:
    monstro_atual = dicionario_monstros(cont_monstro_atual)
    vida_monstro = dicionario_monstros_vida(monstro_atual)

    if oculos:
        vida_monstro -= ataque_oculos
    while vida_player > 0 and vida_monstro > 0:
        if cont_rodada % 2 == 0: #vez do player
            opcoes_ataque = {}
            if pomba_laser:
                opcoes_ataque = {'Ataque normal' : 10, 'Ataque pomba-laser' : 20}
            else: 
                opcoes_ataque = {'Ataque normal' : 10}
            
            ataque_nome = input()
            
            ataque = opcoes_ataque[ataque_nome]
            vida_monstro -= ataque

        elif cont_rodada % 2 == 1: #vez do monstro
            vida_player -= ataque_monstro

        cont_rodada += 1

    else:
        if vida_player == 0:
            ganhador = 'monstro'
            perdedor = 'player'
        elif vida_monstro == 0:
            ganhador = 'player'
            perdedor = 'monstro'

        print('Vencedor: ', ganhador)
        print('Perdedor: ', perdedor)

    cont_monstro_atual += 1
    #Se o ataque for inválido pois não está na lista de ataques, a opção não vai ser meio de input, 
    # e sim, das teclas, então não vai haver esse problema