import pygame

white = ((255, 255, 255))
blue = ((10, 10, 250))
green = ((0, 135, 0))
red = ((255, 0, 0))
black = ((0, 0, 0))


pygame.init()
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Snake")
pygame.display.update()

gameExit = False

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    gameDisplay.fill(green)
    pygame.display.update()


pygame.quit()
quit()
