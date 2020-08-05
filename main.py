import pygame
import time
import random

pygame.init()
white = (255, 255, 255)
black = (0,0,0)
red = (220, 0, 0)
blue = (0, 0, 220)
green = (0, 170, 0)
bright_red = (255, 0, 0)
bright_blue = (0, 0, 255)

large_Text = pygame.font.SysFont("C059", 115)
small_Text = pygame.font.SysFont("C059", 20)
med_Text = pygame.font.SysFont("C059", 30)
parge_Text = pygame.font.SysFont("C059", 120)



display_width = 920
display_height = 720

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Snake")
pygame.display.update()

snake_size = 20

snake_speed = 10

fps = 35

clock = pygame.time.Clock()

gameExit = False 

def game_exit():
    pygame.quit()
    quit()

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    clicked = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y <= mouse[1]:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if clicked[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))
    TextSurf, TextRect = text_objects(msg, small_Text)
    TextRect.center = ((x + (w/2)), (y + (h/2)))
    gameDisplay.blit(TextSurf, TextRect)
    
def unpause():
    global pause
    pygame.mixer.music.unpause()
    pause = False
    
def paused():

    global pause
    pause = True

    while pause:
        pygame.display.set_caption("Snake")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT
                quit()

        gameDisplay.fill(green)
        mouse = pygame.mouse.get_pos()
        TextSurf, TextRect = text_objects("Paused", parge_Text)
        TextRect.center = ((display_width / 2), (display_height/2 - 30))
        gameDisplay.blit(TextSurf, TextRect)

        button("Continue", 230, 450, 100, 50, blue, bright_blue, unpause)
        button("Quit", 550, 450, 100, 50, red, bright_red, game_exit)

        pygame.display.update()
        clock.tick(15)
    
def game_over():
    
    time.sleep(1)

    while True:
        pygame.display.set_caption("Snake")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT
                quit()

        gameDisplay.fill(green)
        mouse = pygame.mouse.get_pos()
        TextSurf, TextRect = text_objects("Game Over", large_Text)
        TextRect.center = ((display_width / 2), (display_height/2 - 30))
        gameDisplay.blit(TextSurf, TextRect)

        button("Replay", 230, 450, 100, 50, blue, bright_blue, game_loop)
        button("Quit", 550, 450, 100, 50, red, bright_red, game_exit)

        pygame.display.update()
        clock.tick(15)
        
def game_intro():

    intro = True

    while intro:
        pygame.display.set_caption("Snake")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT
                quit()

        gameDisplay.fill(green)
        mouse = pygame.mouse.get_pos()
        TextSurf, TextRect = text_objects("Use the arrow keys to control the snake", med_Text)
        TextRect.center = ((display_width / 2), (display_height/2 - 40))
        TextSur, TextRec = text_objects("Press the spacebar to pause", med_Text)
        TextRec.center = ((display_width / 2), (display_height/2 ))
        gameDisplay.blit(TextSurf, TextRect)
        gameDisplay.blit(TextSur, TextRec)

        button("Start Game", 400, 450, 120, 60, blue, bright_blue, game_loop)

        pygame.display.update()
        clock.tick(15)


def game_loop():

    lead_x = display_width/2
    lead_y = display_height/2

    lead_x_change_left = 0
    lead_x_change_right = 0

    lead_y_change_up = 0
    lead_y_change_down = 0
    
    
    while not gameExit:
        global pause
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and lead_x_change_right == 0:
                    lead_x_change_left = -snake_speed
                    lead_x_change_right = 0
                    lead_y_change_down = 0
                    lead_y_change_up = 0
                    
                    
                if event.key == pygame.K_RIGHT and lead_x_change_left == 0:
                    lead_x_change_right = snake_speed
                    lead_y_change_down = 0
                    lead_y_change_up = 0
                    lead_x_change_left = 0
                    
                if event.key == pygame.K_DOWN and lead_y_change_up == 0:
                    lead_y_change_down = snake_speed
                    lead_x_change_left = 0
                    lead_y_change_up = 0
                    lead_x_change_right = 0
                    
                if event.key == pygame.K_UP and lead_y_change_down == 0:
                    lead_y_change_up = -snake_speed
                    lead_x_change_left = 0
                    lead_y_change_down = 0
                    lead_x_change_right = 0
                    
                if event.key == pygame.K_SPACE:
                    pause = True
                    paused()
                    
                if event.key == pygame.K_p:
                    pause = True
                    paused()
                    
                    
        lead_x += lead_x_change_right
        lead_x += lead_x_change_left
        
        lead_y += lead_y_change_up
        lead_y += lead_y_change_down
        
        if lead_x >= display_width - 17 or lead_x <= -3 or lead_y >= display_height - 15 or lead_y <= -2:
            game_over()
        
        gameDisplay.fill(green)
        pygame.draw.rect(gameDisplay, black, [lead_x, lead_y, snake_size, snake_size])
        pygame.display.update()
        clock.tick(fps)
        
game_intro()
game_loop()
pygame.quit()
quit()