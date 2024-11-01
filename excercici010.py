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
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0) 
GOLD = (255, 215, 0)
NAVY = (0, 0, 128)

mouse_pos = {"x": -1, "y": -1}
#Rectangulos
rectangles = [
        { "rect": { "x": 50, "y": 100, "width": 250, "height": 50 }, "color": RED },
        { "rect": { "x": 50, "y": 200, "width": 100, "height": 200 }, "color": GOLD },
        { "rect": { "x": 200, "y": 200, "width": 100, "height": 100 }, "color": BLUE },
        { "rect": { "x": 200, "y": 350, "width": 400, "height": 50 }, "color": PURPLE },
        { "rect": { "x": 350, "y": 100, "width": 50, "height": 200 }, "color": ORANGE },
        { "rect": { "x": 450, "y": 100, "width": 150, "height": 100 }, "color": GREEN },
        { "rect": { "x": 450, "y": 250, "width": 150, "height": 50 }, "color": NAVY }
    ]

rects = []

for dic in rectangles:
    rectsBruto = list(dic["rect"].values())
    rects.append([[rectsBruto[0], rectsBruto[1]], [rectsBruto[2], rectsBruto[3]], [rectangles.index(dic), dic["color"]]])

print(rects)
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
    global mouseInRect, rectAfectado

    mouseInRect = False

    for valor in rects:
        if (mouse_pos["x"] > valor[0][0] and mouse_pos["x"] < (valor[0][0] + valor[1][0]) and #Le sumo a x el valor de width (x es 0 y width es [1][0])
            mouse_pos["y"] > valor[0][1] and mouse_pos["y"] < (valor[0][1] + valor[1][1])): 
            mouseInRect = True
            rectAfectado = valor[2][0]

# Dibuixar
def app_draw():
    screen.fill(WHITE)
    utils.draw_grid(pygame, screen, 50)
    
    #Dibuando los rectangulos
    for rectan in rects:
        if mouseInRect:
            if rectAfectado == rects.index(rectan):
                pygame.draw.rect(screen, rectan[2][1], ((rectan[0][0], rectan[0][1]), (rectan[1][0], rectan[1][1])))
        pygame.draw.rect(screen, BLACK, ((rectan[0][0], rectan[0][1]), (rectan[1][0], rectan[1][1])), 5)

    pygame.display.update()

if __name__ == "__main__":
    main()