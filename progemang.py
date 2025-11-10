# Projekti teemaks on pygame teegiga tehtud mäng, autorid: Karel Kohu,
# Rickie Magnus Jojo Roberts, allikad: ...

import pygame

pygame.init()

screen = pygame.display.set_mode((640,640)) #EKRAAN

batman = pygame.image.load("batman.png").convert_alpha() #Tegelane
batman = pygame.transform.scale(batman,(64,64))
player_rect = batman.get_rect(center=(800 // 2, 600 // 2))
batman_speed = 300

running = True
x = 0
clock = pygame.time.Clock()

delta_time = 0.1 

while running:

    screen.fill((255,255,255))
    screen.blit(batman, (x,30))
    dt = clock.tick(60) / 1000.0  # delta time sekundites

    x += 50 * delta_time

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Liikumine
        keys = pygame.key.get_pressed()
        dx = dy = 0
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            dx = -1
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            dx = 1
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            dy = -1
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            dy = 1

        # Normaalseeri diagonaal
        if dx != 0 and dy != 0:
            inv = 0.70710678
            dx *= inv
            dy *= inv

        # Uuenda asukohta
        player_rect.x += dx * batman_speed * dt
        player_rect.y += dy * batman_speed * dt


    pygame.display.flip()

    delta_time = clock.tick(60)
    delta_time = max(0.001, min(0.1,delta_time))

pygame.quit()