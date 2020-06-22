
try:
    import pygame
    import classes
    import random
    from os import system
    from CONST import *
except:
    print('Existem arquivos faltando não instaladas \n... Provavelmente é o pygame')
    exit()

pygame.init()

win = pygame.display.set_mode((WINDOW_W, WINDOW_H))
pygame.display.set_caption("Pong ping") # windowName

pontos = 0
player = classes.playerClass(False)
enemy = classes.playerClass(True)
ball = classes.ballClass() # actually a square
gameObjects = [player, enemy, ball]
kuerten = [player, enemy]

run = True # game running?
fundo = cor_cor()
while run:

    pygame.time.delay(10)# 0.1 sec
    win.fill(fundo)

    for obj in gameObjects:
        pygame.draw.rect(win, obj.color, obj.basic())

    ball.move()
    pygame.display.update()

    keys = pygame.key.get_pressed()
    player.move(keys)
    if ball.velocity < 0: enemy.x = ball.x - (enemy.width / 2)

    if not (player.x in range(0,WINDOW_W - player.width)):
        player.limit()

    if ball.collidelist(kuerten) >= 0:
       ball.changeDir()
       #fundo = cor_cor()
       if ball.velocity < 0 :pontos += 1
       player.color = cor_cor()
       enemy.color = (255 - (25 * pontos),255 - (25 * pontos),255 - (25 * pontos))


    if ball.x > WINDOW_W or ball.x < 0 :
        ball.changeDirX()
        fundo = cor_cor()


    if ball.y > WINDOW_H or ball.y < 0:
        try:
            #Fim do jojo?, marcar pontos
            system('shutdown now')

            pygame.quit()
        except:
            system("shutdown /s /t 1")
            print('Boa noite bruno')
            exit()

    if pontos >= 10:
        print('Parabens você derrotou todas as maquinas e está livre')
        pygame.quit()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            None
            #run = False
            #Não há escapatoria

pygame.quit() # no error quit S2
