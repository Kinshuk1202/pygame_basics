import pygame

pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 650

display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("bltiitng text")

#color
GREEN = (0,255,0)
DRGREEN = (10,50,10)
BLACK = (0,0,0)

#seeing all available fonts
fonts = pygame.font.get_fonts()
for font in fonts:
    print(font)

#define fonts
system_font = pygame.font.SysFont('calibri',20)
custom_font = pygame.font.Font('AttackGraffiti.ttf',32)

#define text
sys_txt = system_font.render("Dragons Rule!",True,GREEN,DRGREEN) #(txt color,bg color(optional)) # sys_txt is a surface obj
sys_txt_rect = sys_txt.get_rect(center = (WINDOW_WIDTH//2,50))


running = True
while running:
     for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            running = False
     #blitting text
     display_surface.blit(sys_txt,sys_txt_rect)
     #update display
     pygame.display.update()

pygame.quit()