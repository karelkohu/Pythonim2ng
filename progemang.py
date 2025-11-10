# Projekti teemaks on pygame teegiga tehtud mäng, autorid: Karel Kohu,
# Rickie Magnus Jojo Roberts, allikad: ...

import pygame

pygame.init()

screen = pygame.display.set_mode((640,640)) #EKRAAN

batman = pygame.image.load("batman.png").convert_alpha() #Tegelane
batman = pygame.transform.scale(batman,(64,64))

running = True
x = 0
clock = pygame.time.Clock()

delta_time = 0.1 

while running:

    screen.fill((255,255,255))
    screen.blit(batman, (x,30))

    x += 50 * delta_time

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

    delta_time = clock.tick(60)
    delta_time = max(0.001, min(0.1,delta_time))

pygame.quit()