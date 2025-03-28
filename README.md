# Juliano_Bizarre_Adventure

*------------------------------------------------------------------------------ ESTRUTURA ------------------------------------------------------------------------------*

my_game/
│
├── assets/                # Recursos do jogo, como imagens, sons e músicas
│   ├── images/            # Imagens do jogo (sprites, backgrounds, etc)
│   ├── sounds/            # Arquivos de áudio (efeitos sonoros, músicas)
│   └── fonts/             # Fontes utilizadas no jogo
│
├── core/                  # Lógica central do jogo (domínio do jogo)
│   ├── __init__.py        # Arquivo para tornar o diretório um pacote Python
│   ├── entities/          # Entidades do jogo, como Jogador, Inimigos, etc
│   │   ├── player.py      # Lógica do jogador
│   │   ├── enemy.py       # Lógica do inimigo
│   │   └── bullet.py      # Lógica das balas do jogador, por exemplo
│   ├── use_cases/         # Casos de uso, como movimentação, colisões, etc
│   │   ├── movement.py    # Lógica de movimentação dos personagens
│   │   ├── collision.py   # Lógica de colisões
│   │   └── game_logic.py  # Regras do jogo (por exemplo, pontuação, vitória, derrota)
│   └── interfaces/        # Interface para abstrair a interação com o Pygame
│       ├── display.py     # Lógica para renderizar objetos na tela
│       └── input.py       # Lógica de captura de entrada (teclado, mouse)
│
├── game/                  # Lógica do jogo em si, que orquestra a execução
│   ├── __init__.py        # Arquivo para tornar o diretório um pacote Python
│   └── game_manager.py    # Controla o fluxo do jogo (início, fim, pause)
│
├── config/                # Arquivos de configuração (parâmetros do jogo, como tamanho da tela, FPS)
│   └── settings.py        # Configurações principais do jogo
│
├── tests/                 # Testes automatizados
│   ├── __init__.py
│   ├── test_entities.py   # Testes das entidades (jogador, inimigo, etc)
│   ├── test_use_cases.py  # Testes dos casos de uso
│   └── test_game_manager.py # Testes do gerenciamento do jogo
│
└── main.py                # Ponto de entrada do jogo (onde o Pygame é inicializado)

*------------------------------------------------------------------------------ PERSONAGENS ------------------------------------------------------------------------------*

Juliano é o personagem principal de nosso game, ele é uma calopsita;
Jeffinho é a calopsita figurante;


Theobaldo (gato) primeiro vilão (tapado);
Narcisa é uma calopsita par romantico (ou não) de Juliano;
Ze-carcará (gavião) boss poderoso;


*------------------------------------------------------------------------------ OBJETOS ------------------------------------------------------------------------------*

Aveia - Item de vida;
Pomba Laser - Arma;
Laço - Para Narcisa;
*---- BUFFS ----*
Óculos - nerf de força dos inimigos;

*------------------------------------------------------------------------------ MAPAS------------------------------------------------------------------------------*

Mapa 1:
  - Laço de Narcisa;
  - Objetivo:
     . Derrotar o Gato que guarda a saida da casa ruim;
    
Mapa 2:
  - Aveia;
  - Pomba Laser;
  - Objetivo:
    . Derrotar Narcisa (Lutam por uma semente de girassol ao final do mapa 2)
      . Opcional: Cativar Narcisa caso Juliano tenha pego o laço no Mapa 1;
    
Mapa 3:
  - Aveia;
  - Oculos;
  - Objetivo:
    . Derrotar o gavião e chegar na casa;

*------------------------------------------------------------------------------ FINAIS ------------------------------------------------------------------------------*
MAPA 1: Juliano morre e nem sai da casa (tururu juliano triste);
MAPA 2: Juliano morre, seus pares são malvados;
MAPA 3: Juliano morre, a vida selvagem é implacável;

CONQUISTOU A FELICIDADE:
Felicidade 1: Com Narcisa e Jeffinho
Felicidade 2: Jeffinho casado com Narcisa e Juliano de vela;

29/03 - 30/03,

Criação das Classes e UseCases das Classes - Marcelo
  . Juliano tem 2 ataques basicos;
 Orientação a Objetos;
 
Estudar Pygame - Duda, Marcelo, Isaac

 . Como funciona;
   - Todos;
     
 . Como movimentar personagens - Duda;
   - Pegar um personagem e movimenta-lo por uma tela;
     
 . Como funciona colisões - Isaac;
   - Pegar um personagem e movimenta-lo por um objeto e fazer o personagem não atravessar ele;
     
Pixel Arts - Belle
 . Juliano - Frente, Trás, Perfil;
Mapa - Milk
