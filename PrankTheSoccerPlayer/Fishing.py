#Setup pygame
import math
import pygame
pygame.init()

#Definizione costanti: Risoluzione finestra, FPS e titolo del gioco
GAME_RES = WINDOW_WIDTH, WINDOW_HEIGHT = 1366, 768
FPS = 60
GAME_TITLE = "Prank the soccer player"

#Impostazione dei parametri per migliorare le prestazioni e la finestra
window = pygame.display.set_mode(GAME_RES, pygame.HWACCEL|pygame.HWSURFACE|pygame.DOUBLEBUF)
pygame.display.set_caption(GAME_TITLE)
clock = pygame.time.Clock()
BG_COLOR = (255, 255, 255)

#Variabili utili al gioco/programma
countP = 750
count = 1
count2 = 0
EnemySpeed = 1
start = 1
r = 0
dPE = 1000

#Sezione elementi del gioco
radius = 0

player_img = pygame.image.load("player.png")
enemy_img = pygame.image.load("enemy.png")
enemyR_img = pygame.image.load("enemyR.png")
BG_img = pygame.image.load("BG.jpg")
StartScreen_img = pygame.image.load("StartScreen.png")
EndScreen_img = pygame.image.load("EndScreen.png")
Line1_img = pygame.image.load("Line1.png")
Line2_img = pygame.image.load("Line2.png")


player_img = pygame.transform.scale(player_img, (210, 210))
enemy_img = pygame.transform.scale(enemy_img, (210, 210))
enemyR_img = pygame.transform.scale(enemyR_img, (210, 210))
BG_img = pygame.transform.scale(BG_img, (1366, 768))
StartScreen_img = pygame.transform.scale(StartScreen_img, (1366, 768))
EndScreen_img = pygame.transform.scale(EndScreen_img, (1366, 768))
Line1_img = pygame.transform.scale(Line1_img, (1366, 768))
Line2_img = pygame.transform.scale(Line2_img, (1366, 768))

player_rect = player_img.get_rect(center=(0, 0))
enemy_rect = enemy_img.get_rect(center=(0, 0))
BG_rect = BG_img.get_rect(center=(0, 0))
StartScreen_rect = StartScreen_img.get_rect(center=(0, 0))
EndScreen_rect = EndScreen_img.get_rect(center=(0, 0))
Line1_rect = Line1_img.get_rect(center=(0, 0))
Line2_rect = Line2_img.get_rect(center=(0, 0))

player_rect.x = 50
player_rect.y = 50
enemy_rect.x = 1318
enemy_rect.y = 718
BG_rect.x = 0
BG_rect.y = 0
StartScreen_rect.x = 0
StartScreen_rect.y = 0
EndScreen_rect.x = 0
EndScreen_rect.y = 0
Line1_rect.x = 0
Line1_rect.y = 0
Line2_rect.x = 0
Line2_rect.y = 0

font = pygame.font.Font(None, 74)



#Inizio del loop del gioco
game_ended = False
while not game_ended:
    # Event handling
    ##Sezione chiusura del gioco
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_ended = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_ended = True

    if start == 3:
        pygame.Surface.fill(window, BG_COLOR)
        window.blit(Line1_img, Line1_rect)
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_r]:
            start = 4
    if start == 4:
        pygame.Surface.fill(window, BG_COLOR)
        window.blit(Line2_img, Line2_rect)
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_SPACE]:
            start = 0

    if start == 2:
        window.blit(EndScreen_img, EndScreen_rect)
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_r]:
            start = 1
        player_img = pygame.transform.scale(player_img, (300, 300))
        player_rect.x -= 3
        player_rect.y -= 1
        #Display draw and update
        pygame.Surface.fill(window, BG_COLOR)
        text = font.render(str(count), True, (255, 255, 255))  # White color
        window.blit(EndScreen_img, EndScreen_rect)
        window.blit(text, (100, 290))
        window.blit(player_img, player_rect)

    if start == 1:
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_SPACE]:
            count = 0
            start = 3
            player_rect.x = 50
            player_rect.y = 50
            enemy_rect.x = 1318
            enemy_rect.y = 718
        #Display draw and update
        pygame.Surface.fill(window, BG_COLOR)
        window.blit(StartScreen_img, StartScreen_rect)

    if start == 0:   
        ##Input player
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_w]:
            player_rect.y -= 5
        if keys_pressed[pygame.K_a]:
            player_rect.x -= 5
        if keys_pressed[pygame.K_s]:
            player_rect.y += 5
        if keys_pressed[pygame.K_d]:
            player_rect.x += 5
        
        ##Enemy behaviour
        if (enemy_rect.x)>(player_rect.x):
            enemy_rect.x -= EnemySpeed
            r = 1
        if (enemy_rect.y)>(player_rect.y):
            enemy_rect.y -= EnemySpeed
        if (enemy_rect.x)<(player_rect.x):
            enemy_rect.x += EnemySpeed
            r = 0
        if (enemy_rect.y)<(player_rect.y):
            enemy_rect.y += EnemySpeed
    

        #Update game logic
        count += 1
        text = font.render(str(count), True, (255, 255, 255))  # White color
        dPE = math.dist(player_rect, enemy_rect)
        if (dPE < 10):
            player_rect.x = 700
            player_rect.y = 260
            start = 2
        ##Teleporting
        if (player_rect.x) > 1300:
            player_rect.x = -120
        if (player_rect.y) > 628:
            player_rect.y = -140
        if (player_rect.x) < -140:
            player_rect.x = 1280
        if (player_rect.y) < -190:
            player_rect.y = 628
        ##EnemyAcceleration
        if count>countP:
            countP=count+750
            EnemySpeed += 1
            count2=10
        if count2>0:
            text = font.render(str(count), True, (255, 0, 0))  # Red color
            count2 -= 1
        

        

        #Display draw and update
        pygame.Surface.fill(window, BG_COLOR)
        window.blit(BG_img, BG_rect)
        window.blit(player_img, player_rect)
        if r == 1:
            window.blit(enemy_img, enemy_rect)
        if r == 0:
            window.blit(enemyR_img, enemy_rect)
        window.blit(text, (100, 290))

    ##Aggiornamento dell'immagine
    pygame.display.update()
    clock.tick(FPS)    
    
pygame.quit()
exit(0)