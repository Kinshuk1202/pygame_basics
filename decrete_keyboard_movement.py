import pygame

pygame.init()

screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Keyboard movement")

#set values
VELOCITY = 10

#load img
dragon_img = pygame.image.load('dragon_left.png')  
dragon_img_rect = dragon_img.get_rect(centerx = 400 , bottom = 400)

running = True
while running:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            running = False
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_LEFT:
                dragon_img_rect.x -= VELOCITY
            if ev.key == pygame.K_RIGHT:
                dragon_img_rect.x += VELOCITY
            if ev.key == pygame.K_UP:
                dragon_img_rect.y -= VELOCITY
            if ev.key == pygame.K_DOWN:
                dragon_img_rect.y += VELOCITY
    #fill to cover old img
    screen.fill((0,0,0))
    screen.blit(dragon_img,dragon_img_rect)
    pygame.display.update()
pygame.quit()