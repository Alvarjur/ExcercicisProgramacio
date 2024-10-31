#!/usr/bin/env python3

import math
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import sys
import utils

# Definir colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
PINK = (255, 105, 180)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

pygame.init()
clock = pygame.time.Clock()

# Definir la finestra
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Window Title')

# Bucle de l'aplicació
def main():
    is_looping = True

    while is_looping:
        is_looping = app_events()
        app_run()
        app_draw()

        clock.tick(60) # Limitar a 60 FPS

    # Fora del bucle, tancar l'aplicació
    pygame.quit()
    sys.exit()

# Gestionar events
def app_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Botó tancar finestra
            return False
    return True

# Fer càlculs
def app_run():
    pass

# Dibuixar
def app_draw():
    screen.fill(WHITE)
    utils.draw_grid(pygame, screen, 50)

    pygame.draw.rect(screen, RED, ((50, 50), (550, 100)))

    fuenteHeadline = pygame.font.SysFont('Arial', 60)
    fuenteSub1 = pygame.font.SysFont('Courier New', 40, bold=True)
    fuenteParr = pygame.font.SysFont('Arial', 28)

    txtHeadline = fuenteHeadline.render("HEADLINE NEWS", True, WHITE)
    txtSub = fuenteSub1.render("World goes Wrong!", True, BLACK)
    txtSub2 = fuenteSub1.render("YEP#", True, (100, 150, 100))


    screen.blit(txtHeadline, (75,70))
    screen.blit(txtSub, (50,160))
    screen.blit(txtSub2, (507, 155))

    #PARA ESCRIBIR EL PÁRRAFO
    lineas = ["Lorem ipsum et dolor sit amet, consectutor", "adipiscing elit, sed do eiusmod tempor", "incididunt ut labore et dolore magna aliqua"]
    offset = 0

    for linea in lineas:
        txtParr = fuenteParr.render(linea, True, BLACK)
        screen.blit(txtParr, (50,250 + offset))
        offset += 35

    pygame.display.update()

if __name__ == "__main__":
    main()