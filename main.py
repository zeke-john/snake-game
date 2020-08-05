import pygame

white = ((255, 255, 255))
blue = ((0, 0, 200))
green = ((0, 135, 0))
red = ((255, 0, 0))
black = ((0, 0, 0))

pygame.init()
display_width = 920
display_height = 720

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Snake")
pygame.display.update()

snake_size = 20

snake_speed = 6

fps = 60

clock = pygame.time.Clock()








def game_loop():
    
    game_over = False
    gameExit = False 

    lead_x = display_width/2
    lead_y = display_height/2

    lead_x_change_left = 0
    lead_x_change_right = 0

    lead_y_change_up = 0
    lead_y_change_down = 0
    
    
    while not gameExit:
        
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
                    
        lead_x += lead_x_change_right
        lead_x += lead_x_change_left
        
        lead_y += lead_y_change_up
        lead_y += lead_y_change_down
        
        if lead_x >= display_width - 16 or lead_x <= 1 or lead_y >= display_height - 16 or lead_y <= 1:
            gameExit = True
        
        gameDisplay.fill(green)
        pygame.draw.rect(gameDisplay, black, [lead_x, lead_y, snake_size, snake_size])
        pygame.display.update()
        clock.tick(fps)

game_loop()