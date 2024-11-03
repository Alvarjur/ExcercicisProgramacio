#!/usr/bin/env python3

import math
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import sys
import utils

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (50, 120, 200)
BROWN = (165, 42, 42)
YELLOW = (255, 255, 0)
GRAY = (169, 169, 169) 
ORANGE = (255, 165, 0)
GOLD = (255, 215, 0)
RED = (255, 69, 0) 

# Dades del sistema
sun = {
    "pos": (0, 0),
    "radius": 20
}

planets = {
    "Mercury": { "distance": 58,  "speed": 47.87, "radius": 3.80, "color": GRAY, "angle": 0, "pos": (0, 0) },
    "Venus":   { "distance": 108, "speed": 35.02, "radius": 9.50, "color": GOLD, "angle": 0, "pos": (0, 0) },
    "Earth":   { "distance": 150, "speed": 29.78, "radius": 10.0, "color": BLUE, "angle": 0, "pos": (0, 0) },
    "Mars":    { "distance": 228, "speed": 24.07, "radius": 5.30, "color": RED,  "angle": 0, "pos": (0, 0) },
}

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
    delta_time = clock.get_time() / 1000.0 

    sun["pos"] = (int(screen.get_width() / 2), int(screen.get_height() / 2))
    centro = {"x": int(screen.get_width() / 2), "y": int(screen.get_height() / 2)}

    
    for planet in planets:
        planets[planet]["angle"] = planets[planet]["angle"] + planets[planet]["speed"] * delta_time
        
        dicPoints = utils.point_on_circle(centro, planets[planet]["distance"], planets[planet]["angle"])
        planets[planet]["pos"] = tuple(dicPoints.values())

        

# Dibuixar
def app_draw():
    screen.fill(BLACK)
    utils.draw_grid(pygame, screen, 50)

    fuenteLabel = pygame.font.SysFont('Arial', 12)

    #DIBUJAR EL SOL
    pygame.draw.circle(screen, YELLOW, sun["pos"], sun["radius"])
    
    #DIBUJAR EL RESTO
    for planet in planets:
        pygame.draw.circle(screen, GRAY, sun["pos"], planets[planet]["distance"], 1) #ORBITAS

        pygame.draw.circle(screen, planets[planet]["color"], (planets[planet]["pos"]), planets[planet]["radius"]) #PLANETAS

        txtLabel = fuenteLabel.render(planet, True, WHITE)
        screen.blit(txtLabel, ((planets[planet]["pos"][0] + 14, planets[planet]["pos"][1] - 5))) #LABELS



    pygame.display.update()
if __name__ == "__main__":
    main()