import pygame

pygame.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 400
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Adding Music!")

#load sounds

snd1 = pygame.mixer.Sound('sound_1.wav')
snd2 = pygame.mixer.Sound('sound_2.wav')

#play sound
snd1.play()
pygame.time.delay(2000) #will add delay of given ms
snd2.play()
pygame.time.delay(2000)
#changing vol of snd2
snd2.set_volume(0.1)
snd2.play()

#load bg music
pygame.mixer_music.load('music.wav')

#play and stop
pygame.mixer_music.play(-1,0.0) #(loop , st tym , end tym) => -1 for infinite loop 
pygame.time.delay(1000)  #can play snd over bg music
snd2.play()
pygame.time.delay(5000)
pygame.mixer_music.stop()
running = True
while running:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            running = False

pygame.quit()