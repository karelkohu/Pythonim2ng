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
player_rect = batman.get_rect(bottomleft=(125, 450))
player_speed = 300  # px sekundis

alfred = pygame.image.load("alfredtaustata.png").convert_alpha()
alfred = pygame.transform.scale(alfred,(64,64))
alfred_rect = alfred.get_rect(topleft=(300, 350))

kassnaine = pygame.image.load("kassnainetaustata.png").convert_alpha()
kassnaine = pygame.transform.scale(kassnaine,(64,64))
kassnaine_rect = pygame.Rect(290,280,50,50)

#pygame.draw.rect(SCREEN, (0, 0, 255), alfred_rect)

#---DELTA---
delta = pygame.image.load("testDelta.jpeg").convert_alpha()
delta = pygame.transform.scale(delta,(640,640))

#---KLASSIRUUM---
klassiruum = pygame.image.load("klassesialgne (1).jpg").convert_alpha()
klassiruum = pygame.transform.scale(klassiruum,(640,640))

#---PHYSICUM---
physicum = pygame.image.load("physicum.jpg").convert_alpha()
physicum = pygame.transform.scale(physicum,(640,640))
physicum_rect = pygame.Rect(175,380,50,50)

#---PHYSICUM2---
physicum2 = pygame.image.load("adminlaud.jpg")
physicum2 = pygame.transform.scale(physicum2,(640,640))

#---ADMINLAUD---
admin_rect = pygame.Rect(300,300,50,50)

font = pygame.font.Font(None, 32)  # None = vaikimisi font, 36 = suurus



# --- Kaardid ---
maps = [
    (delta),   # map 0
    (klassiruum),      # map 1
    (physicum), # map 2
    (physicum2) # map 3   
]
current_map = 0

#--- DIALOOG ---
dialog_active = False
dialog_lines = []
dialog_index = 0

WHITE = (255, 255, 255)  #värvid
YELLOW = (255, 220, 0)
CYAN = (0, 200, 255)

#--- Erinevate map-ide tekstid ---
map_dialogs = {
    0: [
        {"speaker": "Narrator", "text": "Tartu vajab sind!"},
        {"speaker": "Narrator", "text": "Liigu Delta hoonesse."}
    ],
    1: [
        {"speaker": "Narrator", "text": "Oled jõudnud Delta hoonesse."},
        {"speaker": "Narrator", "text": "Huvitav, mis Alfredil rääkida on..."}
    ],
    2: [
        {"speaker": "Narrator", "text": "Jõudsid bussiga Tehnoloogiainstituudi peatusesse!"},
        {"speaker": "Narrator", "text": "Liigu Physicumi."}
    ],
    3: [
        {"speaker": "Batman", "text": "Nii, olen Physicumis, äkki peaks admini lauas\nveidi mesijuttu rääkima"}
    ]
}


#--- Alfredi tekstid ---
alfred_dialog = [
    {"speaker": "Alfred", "text": "Alfred: Mees, täna olevat Arvuti arhitektuuris\nmingi haige töö."},
    {"speaker": "Alfred", "text": "Kui oleks vaid keegi, kes murraks Physicumi sisse..."}
]

alfred_dialog_done = False

batman_dialog = [
    {"speaker": "Batman", "text":"Batman: Selge, lähen hilisõhtul bussiga Physicumi..."},
    {"speaker": "Batman", "text":"Ma ei maga, Delta vajab mind.\n Aeg liikuda!"}
]

batman_dialog_done = False

admin_dialog = [
    {"speaker": "Narrator", "text": "Administraator: Tere, kuidas saan teid aidata?"},
    {"speaker": "Batman", "text": "Tere, olen Tartu Ülikooli õppejõud ja unustasin\nenda konto parooli, kus mul on kõik\ntestide vastused, palun öelge, mis see oli"},
    {"speaker": "Narrator", "text": "Admin: Huvitav kostüüm õppejõu jaoks, aga okei,\nteie parool on \"NaisedKaovadTehnikaJääb\""},
    {"speaker": "Batman", "text": "Batman: Suur aitäh teile!"},
    {"speaker": "Narrator", "text": "Logisid arvutisse sisse, kuid tuli ette turvaküsimus...\nMis on operatsioonisüsteemide õppejõu\n vähim lemmik OS?"},
    {"speaker": "Narrator", "text": "Kui arvad, et Windows, vajuta W,\nLinux, vajuta L\nvõi Mac, vajuta M"}
]

admin_dialog_done = False

vastused_dialog = [
    {"speaker": "Batman", "text": "Väga hea, vastused on käes,\nNüüd viin need Deltasse ja olen kangelane!"}
]
vastused_dialog_done = False

#--- Funktsioon, mis väljastab map-i alguses ekraanile teksti, mida pead tegema jnejne ---

current_text = ""  # praegune tekst, mis kuvatakse ekraanil
text_index = 0     # millise täheni oleme jõudnud
text_speed = 0.05  # aeg ühe tähe näitamiseks sekundites
last_update = 0    # viimane kord, kui täht lisati

def start_dialog(lines):
    global dialog_active, dialog_lines, dialog_index
    dialog_active = True
    dialog_lines = lines
    dialog_index = 0
    current_text = ""     
    text_index = 0          
    last_update = 0 

start_dialog(map_dialogs[0])

#---ITEMS---
vastused = False
vastused_feedback = ""



# --- Põhiloop ---
running = True
while running:
    dt = CLOCK.tick(60) / 1000

    # --- Sündmuste kontroll ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:

            if dialog_active and (event.key == pygame.K_SPACE or event.key == pygame.K_RETURN):

                entry = dialog_lines[dialog_index]
                if text_index < len(entry["text"]):
                    current_text = entry["text"]  # skipi typewriteri animatsioon
                    text_index = len(entry["text"])
                else:
                    dialog_index += 1
                    current_text = ""
                    text_index = 0
                    last_update = 0
                    if dialog_index >= len(dialog_lines):
                        dialog_active = False
                        dialog_index = 0
                        dialog_lines = []

            if current_map == 3 and dialog_active and admin_dialog_done:
                if event.key == pygame.K_m:  # õige vastus
                    vastused = True
                    vastused_feedback = "Õige vastus! Vastused käes."
                    dialog_active = False
                    dialog_index = 0
                    dialog_lines = []
                elif event.key in [pygame.K_w, pygame.K_l]:  # vale vastus
                    vastused_feedback = "Vale vastus! Proovi uuesti."

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

    # Tegelase liikumine, siis kui tekstikast ei ole aktiivne
    if not dialog_active:
        player_rect.x += dx * player_speed * dt
        player_rect.y += dy * player_speed * dt



        # --- Kaardivahetus koolimajaga ---
    if current_map == 0:  # ainult esimesel kaardil
        delta_rect = pygame.Rect(300, 200, 50, 50)
        if player_rect.colliderect(delta_rect):
            current_map += 1
            player_rect.topleft = (50,50)
            start_dialog(map_dialogs[current_map])  # spawn point uuel kaardil ja dialoogi algus
    


    # --- Piirid üleval ja all ---
    if player_rect.top < 0:
        player_rect.top = 0
    if player_rect.bottom > HEIGHT:
        player_rect.bottom = HEIGHT
    if player_rect.left < 0:
        player_rect.left = 0
    if player_rect.right > WIDTH:
        player_rect.right = WIDTH

    # --- Joonista ---
    
    SCREEN.blit(maps[current_map], (0,0))
    
    if current_map == 1:
        SCREEN.blit(alfred, alfred_rect)

        if player_rect.colliderect(alfred_rect):
            if not dialog_active and not alfred_dialog_done:
                start_dialog(alfred_dialog)
                alfred_dialog_done = True
            elif not dialog_active and alfred_dialog_done and not batman_dialog_done:
                start_dialog(batman_dialog)
                batman_dialog_done = True
            elif not dialog_active and alfred_dialog_done and batman_dialog_done:
                current_map += 1
                player_rect.topleft = (500,350)
                start_dialog(map_dialogs[current_map])
                
    if current_map == 2:
        if player_rect.colliderect(physicum_rect):
            current_map += 1
            player_rect.topleft = (140,350)
            start_dialog(map_dialogs[current_map])

    if current_map == 3:
        SCREEN.blit(kassnaine, kassnaine_rect)
        if current_map == 3 and player_rect.colliderect(admin_rect) and not admin_dialog_done:
            start_dialog(admin_dialog)
            admin_dialog_done = True
        

        if not dialog_active and admin_dialog_done:
            start_dialog(vastused_dialog)
            vastused_dialog_done = True

        if not dialog_active and admin_dialog_done and vastused_dialog_done:
            current_map == 1

    #--- JOONISTAMINE ---
    if dialog_active:

        dialog_rect = pygame.Rect(20, HEIGHT - 160, WIDTH - 40, 140)
        pygame.draw.rect(SCREEN, (0, 0, 0), dialog_rect)
        pygame.draw.rect(SCREEN, (255, 255, 255), dialog_rect, 3)
    
        now = pygame.time.get_ticks() / 1000  # aeg sekundites
        entry = dialog_lines[dialog_index]
        full_text = entry["text"]
    
        if text_index < len(full_text):
            if now - last_update > text_speed:
                current_text += full_text[text_index]
                text_index += 1
                last_update = now

        speaker = entry["speaker"]

        color = WHITE
        if speaker == "Alfred":
            color = YELLOW
        elif speaker == "Batman":
            color = CYAN

        text_surface = font.render(current_text, True, color)
        SCREEN.blit(text_surface, (dialog_rect.x + 20, dialog_rect.y + 20))

    if current_map == 2:
        batman_scaled = pygame.transform.scale(batman, (32, 32))
        SCREEN.blit(batman_scaled,player_rect)

        
    else:
        SCREEN.blit(batman, player_rect)

    # --- Vastuste valimine ---
    if current_map == 3 and vastused_feedback:
        feedback_surface = font.render(vastused_feedback, True, (0,255,0))
        SCREEN.blit(feedback_surface, (20, HEIGHT - 200))


    print(player_rect.x, player_rect.y)
    pygame.draw.rect(SCREEN, (255, 0, 0), delta_rect, 2)

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