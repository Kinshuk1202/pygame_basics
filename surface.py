import pygame

#initialize pygame
pygame.init()

#creating display surface
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
#caption
pygame.display.set_caption("Hello World!")
#the main game loop
running = True
while running:
    #loop through a list of events that have occured
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:  
            running = False
#End the game
pygame.quit()