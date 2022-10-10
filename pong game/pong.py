import pygame
import pygame.freetype

pygame.init()
dis = pygame.display.set_mode((750, 500))
menu = pygame.display.set_mode((750, 500))

myfont = pygame.font.SysFont("monospace", 40)
myfont2 = pygame.font.SysFont("monospace", 100)
myfont3 = pygame.font.SysFont("monospace", 60)

pygame.display.set_caption("Pong Game")

game_over = False
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255, 255, 255)
green = (0, 128, 0)

left_y = 250
left_y_change = 0

vel = 5

right_y = 250
right_y_change = 0

ballx = 350
bally = 350
ballvel_x = 3.5
ballvel_y = 3.5

score_r = 0
score_l = 0
start = False
clock = pygame.time.Clock()


def menudisp():

    while not start:
        menu.fill(white)
        exit = pygame.draw.rect(menu, red, [50/2, 250, 200, 100])
        play = pygame.draw.rect(menu, green, [50/2, 100, 200, 100])
        playtext = myfont3.render(str("PLAY"), 1, (0,0,0))
        exittext = myfont3.render(str("EXIT"), 1, (0,0,0))
        pong = myfont3.render(str("PONG"), 1, (0,0,0))
        name = myfont3.render(str("by Berke"), 1, (0,0,0))
        menu.blit(playtext, (50, 115))
        menu.blit(exittext, (50, 270))
        menu.blit(pong, (350, 150))
        menu.blit(name, (350, 270))
        for event1 in pygame.event.get():
            if event1.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if play.collidepoint(pos):
                    return
                if exit.collidepoint(pos):
                    quit()
                if event1.type == pygame.QUIT:
                    pygame.quit()
                    quit()
        pygame.display.update()


menudisp()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    dis.fill(green)
    boundary_up = pygame.draw.rect(dis, white, [0,0, 750, 10])
    boundary_down = pygame.draw.rect(dis, white, [0,490, 750, 10])
    ball = pygame.draw.circle(dis, blue, (ballx,bally), 10)#ball
    rightStick = pygame.draw.rect(dis, red, [700, right_y, 10, 50])#right
    leftStick = pygame.draw.rect(dis, white, [50, left_y, 10, 50])#left

    keys = pygame.key.get_pressed()  #checking pressed keys

    right_y += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * vel
    left_y += (keys[pygame.K_s] - keys[pygame.K_w]) * vel

    scoretext_l = myfont.render(str(score_l), 1, (white))
    scoretext_r = myfont.render(str(score_r), 1, (red))
    dis.blit(scoretext_l, (5, 10))
    dis.blit(scoretext_r, (700, 10))



    if rightStick.colliderect(ball) or leftStick.colliderect(ball):
        ballvel_x *= -1
        ballvel_x += ballvel_x * 0.05
        ballvel_y += ballvel_y * 0.05

    if ballx > 710 or ballx < -10:
        if ballx > 710:
            score_l += 1
        elif ballx < -10:
            score_r += 1
        ballx = 350
        bally = 350
        ballvel_x = 3.5
        ballvel_y = 3.5

    if rightStick.y == 0:
        right_y = 1
    if rightStick.y == 450:
        right_y = 440
    if leftStick.y == 0:
        left_y = 1
    if leftStick.y == 450:
        left_y = 440

    if boundary_up.colliderect(ball) or boundary_down.colliderect(ball):
        ballvel_y *= -1
    ballx += ballvel_x
    bally += ballvel_y

    if abs(score_l - score_r) == 3:
        if score_l > score_r:
            win1 = myfont2.render(str("WHITE WINS"), 1, white)
            dis.blit(win1, (75, 150))

        if score_r > score_l:
            win2 = myfont2.render(str("RED WINS"), 1, red)
            dis.blit(win2, (75, 150))

    pygame.display.update()

    clock.tick(60)
    #print(right_y)
pygame.quit()
quit()