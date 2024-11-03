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
BLUE = (50, 120, 200)
BROWN = (165, 42, 42)  
YELLOW = (255, 255, 0)  
GREEN = (0, 255, 0)  

pygame.init()
clock = pygame.time.Clock()

# Definir la finestra
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Window Title')

mouse_pos = { "x": -1, "y": -1 }
heights = [0] * 22

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
    global mouse_pos
    mouse_inside = pygame.mouse.get_focused() # El ratolí està dins de la finestra?

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Botó tancar finestra
            return False
        elif event.type == pygame.MOUSEMOTION:
            if mouse_inside:
                mouse_pos["x"] = event.pos[0]
                mouse_pos["y"] = event.pos[1]
            else:
                mouse_pos["x"] = -1
                mouse_pos["y"] = -1
    return True

# Fer càlculs
def app_run():
    global heights

    cell_width = 25
    cell_height = 50

    inside_any_cell = False
    for cnt in range(len(heights)):

        cell_x = 50 + cnt * cell_width
        cell_y_top = 250 - heights[cnt]
        cell_y_bottom = 250

        if cell_x <= mouse_pos["x"] < (cell_x + cell_width) and cell_y_top <= mouse_pos["y"] < cell_y_bottom:
            inside_any_cell = True
            break

    for cnt in range(len(heights)):
        cell_x = 50 + cnt * cell_width + (cell_width / 2)

        if inside_any_cell:
            distance = abs(cell_x - mouse_pos["x"])

            max_distance = 200 
            heights[cnt] = max(5, 45 - min(distance, max_distance) * (40 / max_distance))
        else:

            heights[cnt] = 5

# Dibuixar
def app_draw():
    screen.fill(WHITE)
    utils.draw_grid(pygame, screen, 50)


    for cnt in range(len(heights)):
        x = 50 + cnt * 25
        height = 5 + heights[cnt]
        y = 250 - height
        pygame.draw.rect(screen, BLACK, (x, y, 25, height))

    pygame.display.update()

if __name__ == "__main__":
    main()