import pygame
import time
import random

pygame.init()
white = (255, 255, 255)
black = (0,0,0)
red = (220, 0, 0)
blue = (10, 10, 210)
green = (0, 190, 0)
bright_red = (255, 0, 0)
bright_blue = (0, 0, 255)
snake_blue = (0, 0, 180)

large_Text = pygame.font.SysFont("Fira Mono", 115)
small_Text = pygame.font.SysFont("Fira Mono", 20)
med_Text = pygame.font.SysFont("Fira Mono", 30)
parge_Text = pygame.font.SysFont("Fira Mono", 120)

pygame.mixer.music.load("sounds/music.wav")
snakeImg = pygame.image.load("imgs/snake_Img.png")
appleImg = pygame.image.load("imgs/apple.png")

display_width = 920
display_height = 720

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Snake")
pygame.display.update()

snake_size = 20

apple_size = 20

snake_speed = snake_size

fps = 15

clock = pygame.time.Clock()

gameExit = False 

global high_score
high_score = 0

direction = "up"

def snake_score(count):
    font = pygame.font.SysFont("Fira Mono", 18)
    text = font.render("Length: "+str(count), True, black)
    gameDisplay.blit(text, (0, 1))
    
def best(count):
    font = pygame.font.SysFont("Fira Mono", 18)
    text = font.render("Best: "+str(count), True, black)
    gameDisplay.blit(text, (0, 24))

def snake(snake_size, snakelist):
    
    if direction == "right":
        head = pygame.transform.rotate(snakeImg, 270)
        
    if direction == "left":
        head = pygame.transform.rotate(snakeImg, 90)
        
    if direction == "up":
        head = snakeImg
        
    if direction == "down":
        head = pygame.transform.rotate(snakeImg, 180)
        
    
    gameDisplay.blit(head, (snakelist[-1][0], snakelist[-1][1]))
    
    for XnY in snakelist[:-1]:
        pygame.draw.rect(gameDisplay, snake_blue, [XnY[0], XnY[1], snake_size, snake_size])

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
    
    pygame.mixer.music.pause()

    global pause
    pause = True

    while pause:
        pygame.display.set_caption("Snake")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT
                quit()

        mouse = pygame.mouse.get_pos()
        TextSurf, TextRect = text_objects("Paused", parge_Text)
        TextRect.center = ((display_width / 2), (display_height/2 - 30))
        gameDisplay.blit(TextSurf, TextRect)

        button("Continue", 230, 450, 100, 50, blue, bright_blue, unpause)
        button("Quit", 550, 450, 100, 50, red, bright_red, game_exit)

        pygame.display.update()
        clock.tick(15)    
    
def game_over():
    pygame.mixer.music.stop()
    
    time.sleep(1.5)

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
        TextSurf_1, TextRect_1= text_objects("Press the spacebar to pause", med_Text)
        TextRect_1.center = ((display_width / 2), (display_height/2 ))
        TextSurf_2, TextRect_2= text_objects("Press 'm' to mute the music and 'p' to play it", med_Text)
        TextRect_2.center = ((display_width / 2), (display_height/2 -80))
        gameDisplay.blit(TextSurf, TextRect)
        gameDisplay.blit(TextSurf_2, TextRect_2)
        gameDisplay.blit(TextSurf_1, TextRect_1)
        
        
        button("Start Game", 400, 450, 130, 60, blue, bright_blue, game_loop)

        pygame.display.update()
        clock.tick(15)  
        
def game_loop():
    global direction
    global pause
    global high_score
    
    direction = "up"
    
    pygame.mixer.music.play(-1)
    
    pygame.mixer.music.play(-1)
    
    lead_x = display_width/2
    lead_y = display_height/2

    lead_x_change_left = 0
    lead_x_change_right = 0

    lead_y_change_up = 0
    lead_y_change_down = 0
    
    snakeList = []
    
    snake_length = 1
    
    randAppleX = round(random.randrange(-2, display_width - 16)/20) * 20
    randAppleY = round(random.randrange(-1, display_height - 14)/20) * 20
    
    score = 0

    while not gameExit:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and lead_x_change_right == 0:
                    direction = "left"
                    lead_x_change_left = -snake_speed
                    lead_x_change_right = 0
                    lead_y_change_down = 0
                    lead_y_change_up = 0
                    
                    
                if event.key == pygame.K_RIGHT and lead_x_change_left == 0:
                    direction = "right"
                    lead_x_change_right = snake_speed
                    lead_y_change_down = 0
                    lead_y_change_up = 0
                    lead_x_change_left = 0
                    
                if event.key == pygame.K_DOWN and lead_y_change_up == 0:
                    direction = "down"
                    lead_y_change_down = snake_speed
                    lead_x_change_left = 0
                    lead_y_change_up = 0
                    lead_x_change_right = 0
                    
                if event.key == pygame.K_UP and lead_y_change_down == 0:
                    direction = "up"
                    lead_y_change_up = -snake_speed
                    lead_x_change_left = 0
                    lead_y_change_down = 0
                    lead_x_change_right = 0
                    
                if event.key == pygame.K_SPACE:
                    pause = True
                    paused()
                    
                if event.key == pygame.K_m:
                    pygame.mixer.music.pause()
                    
                if event.key == pygame.K_p:
                    pygame.mixer.music.unpause()
                    
        lead_x += lead_x_change_right
        lead_x += lead_x_change_left
        
        lead_y += lead_y_change_up
        lead_y += lead_y_change_down
        
        if lead_x >= display_width - 17 or lead_x <= -3 or lead_y >= display_height - 15 or lead_y <= -2:
            game_over()
            
        if lead_x == randAppleX and lead_y == randAppleY:
            snake_length +=1
            score +=1
            randAppleX = round(random.randrange(-2, display_width - 16)/20) * 20
            randAppleY = round(random.randrange(-1, display_height - 14)/20) * 20
            
        if score > high_score:
            high_score = score
            high_score = high_score
        
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)
        
        if len(snakeList) > snake_length:
            del snakeList[0]
            
        for eachsegment in snakeList[:-1]:
            if eachsegment == snakeHead:
                game_over()
        
        gameDisplay.fill(green)
        snake_score(score)
        best(high_score)
        gameDisplay.blit(appleImg,(randAppleX, randAppleY))
        #pygame.draw.rect(gameDisplay,red, [randAppleX, randAppleY, apple_size, apple_size])
        snake(snake_size, snakeList)
        pygame.display.update()
        clock.tick(fps)
        
game_intro()
game_loop()
pygame.quit()
quit()