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

    #LAS IMAGENES NO SON LAS MISMAS QUE EN EL EJERCICIO
    
    path_shinnosuke = os.path.join(os.path.dirname(__file__), "./shinnosuke.png")
    imagen_shinnosuke = pygame.image.load(path_shinnosuke).convert_alpha()
    imagen_shinnosuke = utils.scale_image(pygame, imagen_shinnosuke, target_width=100)

    path_shiro = os.path.join(os.path.dirname(__file__), "./shiro.png")
    imagen_shiro = pygame.image.load(path_shiro).convert_alpha()
    imagen_shiro = utils.scale_image(pygame, imagen_shiro, target_width=75)

    screen.blit(imagen_shinnosuke, (320, 185))
    screen.blit(imagen_shiro, (225, 233))

    pygame.display.update()

if __name__ == "__main__":
    main()