import pygame, sys
'''
 Tegemist on Programmeerimise projektiga ehk PyGame'iga tehtud mäng.
 Autorid: Karel Kohu, Rickie Magnus Jojo Roberts
 Inspiratsiooniallikad hetkeseisuga: https://www.youtube.com/watch?v=blLLtdv4tvo&t=1s
 '''

# --- Algseaded ---
pygame.init()

screen = pygame.display.set_mode((640,640)) #EKRAAN

batman = pygame.image.load("batman.png").convert_alpha() #Tegelane
batman = pygame.transform.scale(batman,(64,64))

running = True
while running:
    dt = CLOCK.tick(60) / 1000

    # --- Sündmuste kontroll ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

    delta_time = clock.tick(60)
    delta_time = max(0.001, min(0.1,delta_time))

pygame.quit()
sys.exit()

# Level 2 - Leiad tegelase, kes ütleb nt "ou arvuti arhitektuuris on mingi haige töö täna"
# "Meil on vaja murda sisse Physicumi ja saada töö vastused, sest meie ega ChatGPT ei saa teha seda"
# Uus map - Liigu Physicumi!
# Jõuad Physicumi, siis pead leidma vastused (collectable item)
# Kui see item on olemas, siis on level läbi ja pead liikuma tagasi Deltasse, kus ootab see sama kunde
# Siis ta on mingi "jouu tänx mees nüüd saame selle töö lebo A"