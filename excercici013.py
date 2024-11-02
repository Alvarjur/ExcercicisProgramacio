#!/usr/bin/env python3

import math
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import sys
import utils
from svgmoji.emojis import get_emoji
import random

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

posCar = [450, 300]

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


dirLeft = False
dirRight = False
dirUp = False
dirDown = False
angle = 180
# Gestionar events
def app_events():
    global dirLeft, dirRight, dirUp, dirDown

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dirLeft = True
            elif event.key == pygame.K_RIGHT:
                dirRight = True
            elif event.key == pygame.K_UP:
                dirUp = True
            elif event.key == pygame.K_DOWN:
                dirDown = True
        else:
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    dirLeft = False
                elif event.key == pygame.K_RIGHT:
                    dirRight = False
                elif event.key == pygame.K_UP:
                    dirUp = False
                elif event.key == pygame.K_DOWN:
                    dirDown = False

    return True

# Fer càlculs
def app_run():
    global angle
    delta_time = clock.get_time() / 1000.0  # Convertir a segons
    
    speed = 100
    displacement = speed * delta_time

    if dirLeft:
        posCar[0] -= displacement
        if dirUp:
            angle = 45
        elif dirDown:
            angle = 140
        else:
            angle = 90
    if dirRight:
        posCar[0] += displacement
        if dirUp:
            angle = 320
        elif dirDown:
            angle = 220
        else:
            angle = 270
            
    if dirUp:
        posCar[1] -= displacement
        if not dirLeft and not dirRight:
            angle = 0

    if dirDown:
        posCar[1] += displacement

        if not dirLeft and not dirRight:
            angle = 180



    

# Dibuixar
def app_draw():
    screen.fill(WHITE)
    utils.draw_grid(pygame, screen, 50)
    
    #dibujar el circuito
    pathTrack = os.path.join(os.path.dirname(__file__), "./circuit.png")
    ImagenTrack = pygame.image.load(pathTrack).convert_alpha()
    ImagenTrack = utils.scale_image(pygame, ImagenTrack, target_height=480)

    screen.blit(ImagenTrack, (0,0))

    #dibujar coche
    pathCar = os.path.join(os.path.dirname(__file__), "./car.png")
    imagenCar = pygame.image.load(pathCar).convert_alpha()
    imagenCar = utils.scale_image(pygame, imagenCar, target_width= 15)
    rotated_img = pygame.transform.rotate(imagenCar, angle)
    
    screen.blit(rotated_img, posCar)

    pygame.display.update()

if __name__ == "__main__":
    main()