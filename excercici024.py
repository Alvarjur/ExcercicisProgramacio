#!/usr/bin/env python3

import math
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import sys
import utils
from datetime import datetime

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (50, 120, 200)
RED = (255, 69, 0) 

time = { 
    "hours": 0, 
    "minutes": 0, 
    "seconds": 0
}

offset = -90

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
    global time, hour_tuple, secondsTuple, minutes_tuple

    now = datetime.now()
    current_time_ms = now.timestamp() * 1000
    
    # Hores amb fracció de minuts (format 12 hores)
    time["hours"] = (current_time_ms / 3600000) % 12

    # Minuts amb fracció de segons    
    time["minutes"] = (current_time_ms / 60000) % 60

    # Segons amb fracció de mil·lisegons
    time["seconds"] = (current_time_ms / 1000) % 60

    degrees_per_hour = (360 / 12) #aguja de horas
    degrees_per_second = (360 / 60) #aguja de segundos
    degrees_per_minute = (360 / 60) #aguja de minutos

    hour_angle = (degrees_per_hour * time["hours"]) + offset
    seconds_angle = (degrees_per_second * time["seconds"]) + offset
    minutes_angle = (degrees_per_minute * time["minutes"]) + offset

    seconds = utils.point_on_circle({"x": 325, "y": 250}, 200 * 0.9, seconds_angle)
    secondsTuple = (seconds["x"], seconds["y"])
    
    hour = utils.point_on_circle({"x": 325, "y": 250}, 200 * 0.4, hour_angle)
    hour_tuple = (hour["x"], hour["y"])
        
    minutes = utils.point_on_circle({"x": 325, "y": 250}, 200 * 0.7, minutes_angle)
    minutes_tuple = (minutes["x"], minutes["y"])

# Dibuixar
def app_draw():
    screen.fill(BLACK)
    utils.draw_grid(pygame, screen, 50)
    fuenteNum = pygame.font.SysFont('Arial', 16)

    #DIBUJANDO LOS NÚMEROS
    for num in range(1,13):
        coordsNum = utils.point_on_circle({"x": 325, "y": 250}, 200, (360/12) * num + offset)
        coordsNumTuple = tuple(coordsNum.values())
        txtNum = fuenteNum.render(str(num), True, WHITE)
        txtNum_rect = txtNum.get_rect(center=coordsNumTuple)
        screen.blit(txtNum, txtNum_rect)

    pygame.draw.line(screen, RED, (325, 250), secondsTuple, 2)
    pygame.draw.line(screen, BLUE, (325, 250), minutes_tuple, 4)
    pygame.draw.line(screen, WHITE, (325, 250), hour_tuple, 7)

    pygame.display.update()
if __name__ == "__main__":
    main()