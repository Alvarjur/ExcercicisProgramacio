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
    pos = [50, 50]

    for row in range(8):
        num = 1
        if row % 2 == 1:
            num = 2
            
        for column in range(8):
            if num == 1:
                pygame.draw.rect(screen, GRAY, (pos, (50, 50)))
                pos[0] += 50
                num += 1
                continue

            elif num == 2:
                pygame.draw.rect(screen, BLACK, (pos, (50, 50)))
                pos[0] += 50

            if num == 2:
                num = 1

        pos[0] = 50
        pos[1] += 50
        

    pygame.display.update()

if __name__ == "__main__":
    main()