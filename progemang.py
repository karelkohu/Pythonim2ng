import pygame
import sys

# Inits
pygame.init()
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tegelase liikumine pildiga")
CLOCK = pygame.time.Clock()

# Lae tegelase pilt
player_image = pygame.image.load("batman.png").convert_alpha()  # peab olema samas kaustas
player_image = pygame.transform.scale(player_image, (80, 80))
player_rect = player_image.get_rect(center=(WIDTH // 2, HEIGHT // 2))
player_speed = 300  # px sekundis

running = True
while running:
    dt = CLOCK.tick(60) / 1000.0  # delta time sekundites

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
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
    player_rect.x += dx * player_speed * dt
    player_rect.y += dy * player_speed * dt

    # Piira ekraani sisse
    if player_rect.left < 0:
        player_rect.left = 0
    if player_rect.right > WIDTH:
        player_rect.right = WIDTH
    if player_rect.top < 0:
        player_rect.top = 0
    if player_rect.bottom > HEIGHT:
        player_rect.bottom = HEIGHT

    # Joonista ekraan
    SCREEN.fill((40, 40, 40))
    SCREEN.blit(player_image, player_rect)
    pygame.display.flip()

pygame.quit()
sys.exit()

