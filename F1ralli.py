import pygame
import random

# Algseadistused
pygame.init()
laius, kõrgus = 640, 480
aken = pygame.display.set_mode((laius, kõrgus))
pygame.display.set_caption("Rainer Hints ISK24")

# Piltide laadimine
taust = pygame.image.load("bg_rally.jpg")
punane_auto = pygame.image.load("f1_red.png")
sinine_auto = pygame.image.load("f1_blue.png")

#Autode suurused ja pööramine
punane_auto = pygame.transform.scale(punane_auto, (60, 100))
sinine_auto = pygame.transform.scale(sinine_auto, (60, 100))
sinine_auto = pygame.transform.rotate(sinine_auto, 180)

#Siniste autode andmed
autode_arv = 1
sinised_autod = []

for _ in range(autode_arv):
    x_pos = random.choice([170, 290, 410])  # teede vahemik
    y_pos = random.randint(-600, -100)
    sinised_autod.append([x_pos, y_pos])

kiirus = 5 #autode liikumis kiirus
skoor = 0
font = pygame.font.SysFont(None, 36)

# Mängutsükkel
kell = pygame.time.Clock()
on = True

while on: #peamine tsükkel
    for sündmus in pygame.event.get():
        if sündmus.type == pygame.QUIT:
            on = False

    # Siniste autode liikumine
    for auto in sinised_autod:
        auto[1] += kiirus
        if auto[1] > kõrgus:
            auto[1] = random.randint(-600, -100)
            auto[0] = random.choice([170, 290, 410])
            skoor += 1

    aken.blit(taust, (0, 0))
    aken.blit(punane_auto, (290, 370))

    for auto in sinised_autod:
        aken.blit(sinine_auto, (auto[0], auto[1]))

    # Skoori tabloo
    skoori_tekst = font.render("Skoor: " + str(skoor), True, (255, 255, 255))
    aken.blit(skoori_tekst, (10, 10))

    pygame.display.flip()
    kell.tick(60)

pygame.quit()
