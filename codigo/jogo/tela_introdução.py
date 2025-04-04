self.intro_background = pygame.image.load('graficos/tela/introbackground.png')
self.font = pygame.font.SysFont('arial', 32)


        titulo = self.font.render('Juliano Bizarre Adventures', True, PRETO)
        titulo_rect = titulo.get_rect(x=10,y=10)
        botao_jogar = Botao(10,50,100,50, BRANCO, PRETO, 'Jogar', 32)
        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    intro = False
                    self.running = False
                
            mouse_pos = pygame.mouse.get_pos()
            mouse_pressionado = pygame.mouse.get_pressed()

            if botao_jogar.esta_pressionado(mouse_pos,mouse_pressionado):
                intro = False
            
            self.display.blit(self.intro_background, (0,0)) 
            self.display.blit(titulo, titulo_rect)  
            self.display.blit(botao_jogar.image, botao_jogar.rect) 