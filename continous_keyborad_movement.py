import pygame

pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300

screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Continous keyboard movement!")

#set fps and clock
FPS = 60
clock = pygame.time.Clock()
#set values
VELOCITY = 5

#load images
dragon_img = pygame.image.load('dragon_right.png')
dragon_img_rect = dragon_img.get_rect(center = (WINDOW_WIDTH//2,WINDOW_HEIGHT//2))

running = True
while running:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:  
            running = False
    #getlist of all keys that are pressed dwn
    keys = pygame.key.get_pressed()
    print(keys)
    #move dragon continously
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        dragon_img_rect.x -= VELOCITY 
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        dragon_img_rect.x += VELOCITY 
    if keys[pygame.K_UP]or keys[pygame.K_w]:
        dragon_img_rect.y -= VELOCITY 
    if keys[pygame.K_DOWN]or keys[pygame.K_s]:
        dragon_img_rect.y += VELOCITY 
    screen.fill((0,0,0))
    screen.blit(dragon_img,dragon_img_rect)
    pygame.display.update()
    #tick the clock
    clock.tick(FPS) # this will delay game loop in such a way that it will not exceed fps and make it uniform
pygame.quit()