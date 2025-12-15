import pygame, sys
'''
 Tegemist on Programmeerimise projektiga ehk PyGame'iga tehtud mäng.
 Autorid: Karel Kohu, Rickie Magnus Jojo Roberts
 Inspiratsiooniallikad hetkeseisuga: https://www.youtube.com/watch?v=blLLtdv4tvo&t=1s
 '''

# --- Algseaded ---
pygame.init()
WIDTH, HEIGHT = 640,640
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tartu vajab sind!")
CLOCK = pygame.time.Clock()

# --- Tegelane ---
batman = pygame.image.load("batman.png").convert_alpha()
batman = pygame.transform.scale(batman, (64, 64))
player_rect = batman.get_rect(bottomleft=(50, 600))
player_speed = 300  # px sekundis

#---DELTA---
delta = pygame.image.load("testDelta.jpeg").convert_alpha()
delta = pygame.transform.scale(delta,(640,640))


font = pygame.font.Font(None, 36)  # None = vaikimisi font, 36 = suurus



# --- Kaardid ---
maps = [
    (delta),   # kaart 0
    pygame.Surface((640,640)),      # kaart 1
    pygame.Surface((640,640)),     # kaart 2
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


        # --- Kaardivahetus koolimajaga ---
    if current_map == 0:  # ainult esimesel kaardil
        delta_rect = pygame.Rect(426, 0, 214, 640)
        if player_rect.colliderect(delta_rect):
            current_map += 1
            player_rect.topleft = (50,50)  # spawn point uuel kaardil
    


    # --- Piirid üleval ja all ---
    if player_rect.top < 0:
        player_rect.top = 0
    if player_rect.bottom > HEIGHT:
        player_rect.bottom = HEIGHT

    # --- Joonista ---
    
    SCREEN.blit(maps[current_map], (0,0))

    if current_map == 0:
        message = "Tartu vajab sind! Liigu Delta hoonesse."
        text_surface = font.render(message, True, (255, 0, 0))  # punane tekst
        SCREEN.blit(text_surface, (50, 50))  # x=50, y=50
    
    if current_map == 1:
        message = "Oled jõudnud Delta hoonesse\n edasi saad avastada Beeta versioonis :)"
        text_surface = font.render(message, True, (255, 0, 0))  # punane tekst
        SCREEN.blit(text_surface, (50, 50))  # x=50, y=50

    maps[1].fill((0, 180, 90))   # roheline / suvaline
    maps[2].fill((180, 60, 60))
    SCREEN.blit(batman, player_rect)
    pygame.display.flip()

# --- Väljumine ---
pygame.quit()
sys.exit()

# Level 2 - Leiad tegelase, kes ütleb nt "ou arvuti arhitektuuris on mingi haige töö täna"
# "Meil on vaja murda sisse Physicumi ja saada töö vastused, sest meie ega ChatGPT ei saa teha seda"
# Uus map - Liigu Physicumi!
# Jõuad Physicumi, siis pead leidma vastused (collectable item)
# Kui see item on olemas, siis on level läbi ja pead liikuma tagasi Deltasse, kus ootab see sama kunde
# Siis ta on mingi "jouu tänx mees nüüd saame selle töö lebo A"