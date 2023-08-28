import pygame

pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 650

display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Blitting images") #path if working in different folder

#create image... returns a surface object with image on it and then use rect for its pos
dragon_left_image = pygame.image.load("dragon_left.png")
dragon_left_rect = dragon_left_image.get_rect()
dragon_left_rect.topleft = (0,0)

dragon_right_image = pygame.image.load("dragon_right.png")
dragon_right_rect = dragon_right_image.get_rect(topright = (WINDOW_WIDTH,0))  #both ways can work for positon


running = True
while running:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            running = False
    #blit or copy suface obj at given coord on given surface
    display_surface.blit(dragon_left_image,dragon_left_rect)
    display_surface.blit(dragon_right_image,dragon_right_rect)
    pygame.draw.line(display_surface,(255,255,255),(0,75),(WINDOW_WIDTH,75),5)
    #update display
    pygame.display.update()
pygame.quit()