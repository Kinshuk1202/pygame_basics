import pygame

pygame.init()

MAX_WIDTH = 800
MAX_HEIGHT = 400

screen = pygame.display.set_mode((MAX_WIDTH,MAX_HEIGHT))
 
pygame.display.set_caption("Mouse movement")

dragon_img = pygame.image.load('dragon_left.png').convert_alpha()
dragon_img_rect = dragon_img.get_rect(topleft = (25,25))

running = True
while running:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            running = False
        screen.fill((0,0,0))
        #move based on mouse clicks
        if ev.type == pygame.MOUSEBUTTONDOWN:
            mouse_x = ev.pos[0]
            mouse_y = ev.pos[1]
            dragon_img_rect.centerx = mouse_x
            dragon_img_rect.centery = mouse_y
        #drag when mouse is clicked
        if ev.type == pygame.MOUSEMOTION and ev.buttons[0]==1:
            mouse_x = ev.pos[0]
            mouse_y = ev.pos[1]
            dragon_img_rect.centerx = mouse_x
            dragon_img_rect.centery = mouse_y
        screen.blit(dragon_img,dragon_img_rect)
        pygame.display.update()
pygame.quit()