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

moves_house = [{"direction": "right", "distance": 250}, {"direction": "up", "distance": 200}, {"direction": "left", "distance": 50}, {"direction": "up", "distance": 50}, {"direction": "left", "distance": 50}, {"direction": "up", "distance": 50}, {"direction": "left", "distance": 50}, {"direction": "down", "distance": 50}, {"direction": "left", "distance": 50}, {"direction": "down", "distance": 50}, {"direction": "left", "distance": 50}, {"direction": "down", "distance": 200}]
moves_sun = [{"direction": "right", "distance": 25}, {"direction": "up", "distance": 25}, {"direction": "right", "distance": 25}, {"direction": "up", "distance": 25}, {"direction": "right", "distance": 50}, {"direction": "down", "distance": 25}, {"direction": "right", "distance": 25}, {"direction": "down", "distance": 25}, {"direction": "right", "distance": 25}, {"direction": "down", "distance": 50}, {"direction": "left", "distance": 25}, {"direction": "down", "distance": 25}, {"direction": "left", "distance": 25}, {"direction": "down", "distance": 25}, {"direction": "left", "distance": 50}, {"direction": "up", "distance": 25}, {"direction": "left", "distance": 25}, {"direction": "up", "distance": 25}, {"direction": "left", "distance": 25} ]
moves_car = [{"direction": "up", "distance": 50}, {"direction": "right", "distance": 50}, {"direction": "up", "distance": 50}, {"direction": "right", "distance": 50}, {"direction": "down", "distance": 50}, {"direction": "right", "distance": 50}, {"direction": "down", "distance": 50} ]
moves_grass = [{"direction": "right", "distance": 650}, {"direction": "down", "distance": 100}, {"direction": "left", "distance": 650}]

def draw_moves(color, start_pos, moves):
    points = [start_pos]

    for move in moves:
        point1 = points[-1][0]
        point2 = points[-1][1]

        if move["direction"] == "right":
            point1 = points[-1][0] + move["distance"]
        elif move["direction"] == "left":
            point1 = points[-1][0] - move["distance"]
        elif move["direction"] == "up":
            point2 = points[-1][1] - move["distance"]
        elif move["direction"] == "down":
            point2 = points[-1][1] + move["distance"]
        
        points.append((point1, point2))
        
    pygame.draw.polygon(screen, color, points)

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

    draw_moves(BROWN, (350, 400), moves_house)
    draw_moves(YELLOW, (50, 100), moves_sun)
    draw_moves(BLUE, (100, 400), moves_car)
    draw_moves(GREEN, (0, 400), moves_grass)

    pygame.display.update()

if __name__ == "__main__":
    main()