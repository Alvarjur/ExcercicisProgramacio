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
    

    
    center_x, center_y =  int(screen.get_width() / 2), int(screen.get_height() / 2)
    iteration = 1
    size = 15


    for _ in range(25):
        if iteration == 1:
            pygame.draw.line(screen, RED, (center_x, center_y), (center_x + size, center_y), 5)
            
            center_x += size
            size += 15

            iteration += 1

        elif iteration == 2:
            pygame.draw.line(screen, RED, (center_x, center_y), (center_x, center_y - size), 5)
            
            center_y -= size
            size += 15

            iteration += 1

        elif iteration == 3:
            pygame.draw.line(screen, RED, (center_x, center_y), (center_x - size, center_y), 5)
            
            center_x -= size
            size += 15

            iteration += 1
            continue

        elif iteration == 4:
            pygame.draw.line(screen, RED, (center_x, center_y), (center_x, center_y + size), 5)
            
            center_y += size
            size += 15

            iteration += 1

        
        if iteration >= 4:
            iteration = 1


    
    pygame.display.update()

if __name__ == "__main__":
    main()