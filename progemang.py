import pygame, sys

# --- Algseaded ---
pygame.init()
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Kaardivahetus mõlemas suunas")
CLOCK = pygame.time.Clock()

# --- Tegelane ---
player_image = pygame.image.load("batman.png").convert_alpha()
player_image = pygame.transform.scale(player_image, (80, 80))
player_rect = player_image.get_rect(center=(WIDTH // 2, HEIGHT // 2))
player_speed = 300  # px sekundis

# --- Kaardid ---
maps = [
    (100, 150, 250),   # kaart 0
    (0, 180, 90),      # kaart 1
    (180, 60, 60),     # kaart 2
]
current_map = 0

# --- Põhiloop ---
running = True
while running:
    dt = CLOCK.tick(60) / 1000

    # --- Sündmuste kontroll ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # --- Liikumine ---
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
        dx *= 0.7071
        dy *= 0.7071

    # Uuenda tegelase positsiooni
    player_rect.x += dx * player_speed * dt
    player_rect.y += dy * player_speed * dt

    # --- Kaardivahetus paremale ja vasakule ---
    if player_rect.right > WIDTH:  # paremale serv
        if current_map < len(maps) - 1:
            current_map += 1
            player_rect.left = 0
        else:
            player_rect.right = WIDTH  # viimase kaardi serv

    if player_rect.left < 0:  # vasakule serv
        if current_map > 0:
            current_map -= 1
            player_rect.right = WIDTH
        else:
            player_rect.left = 0  # esimese kaardi vasak serv

    # --- Piirid üleval ja all ---
    if player_rect.top < 0:
        player_rect.top = 0
    if player_rect.bottom > HEIGHT:
        player_rect.bottom = HEIGHT

    # --- Joonista ---
    SCREEN.fill(maps[current_map])
    SCREEN.blit(player_image, player_rect)
    pygame.display.flip()

# --- Väljumine ---
pygame.quit()
sys.exit()
