import pygame , random

pygame.init()

WIN_WIDTH = 600
WIN_HEIGHT = 300
VELOCITY = 5
screen = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))
pygame.display.set_caption("Collision Detection")

#set fps and clck
FPS = 60
clock = pygame.time.Clock()
drg_img = pygame.image.load('dragon_right.png')
drg_img_rect = drg_img.get_rect(topleft = (25,25))
coin_img = pygame.image.load('coin.png')
coin_img_rect = coin_img.get_rect(center = (WIN_WIDTH//2,WIN_HEIGHT//2))
running  = True
while running:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and drg_img_rect.left>0:
        drg_img_rect.x -= VELOCITY
    if keys[pygame.K_RIGHT] and drg_img_rect.right<WIN_WIDTH:
        drg_img_rect.x += VELOCITY
    if keys[pygame.K_UP] and drg_img_rect.top>0:
        drg_img_rect.y -= VELOCITY
    if keys[pygame.K_DOWN] and drg_img_rect.bottom<WIN_HEIGHT:
        drg_img_rect.y += VELOCITY
    #checkn for collision b/w 2 rects
    if drg_img_rect.colliderect(coin_img_rect):
        print("HIT")
        coin_img_rect.x = random.randint(0,WIN_HEIGHT-32)
        coin_img_rect.y = random.randint(0,WIN_HEIGHT-32)
    screen.fill((0,0,0))
    #draw rects to represent each objects
    pygame.draw.rect(screen,(0,255,0),drg_img_rect,1)
    pygame.draw.rect(screen,(255,255,0),coin_img_rect,1)
    screen.blit(drg_img,drg_img_rect)
    screen.blit(coin_img,coin_img_rect)
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()