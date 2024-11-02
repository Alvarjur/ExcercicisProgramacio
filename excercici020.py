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

board = {
    "position": { 
        "x": 50, 
        "y": 50 
    },
    "size": { 
        "rows": 15, 
        "cols": 10 
    },
    "cell_size": 25
}

def draw_board():
    for row in range(1, board["size"]["rows"]):
        for column in range(1, board["size"]["cols"]):
            dictCell = cell_from_point(mouse_pos, board)
            if dictCell != {"row": -1, "col": -1}:
                cellRowOnPoint = dictCell["row"]
                cellColOnPoint = dictCell["col"]
                if row == cellRowOnPoint and column == cellColOnPoint:
                    pygame.draw.rect(screen, BLUE, ((board["position"]["x"] + (column * board["cell_size"]), board["position"]["y"]+ (row * board["cell_size"])),(board["cell_size"], board["cell_size"])))
            pygame.draw.rect(screen, BLACK, ((board["position"]["x"] + (column * board["cell_size"]), board["position"]["y"]+ (row * board["cell_size"])),(board["cell_size"], board["cell_size"])), 1)
            

    return True

def cell_from_point(point, board):
    endTablaX = board["position"]["x"] + (board["size"]["cols"] * board["cell_size"])
    endTablaY = board["position"]["y"] + (board["size"]["rows"] * board["cell_size"])

    if (point["x"] > board["position"]["x"] and #COMPROBAR SI EL RATÓN (PUNTO) ESTÁ DENTRO DE LA TABLA
            point["x"] < endTablaX and
            point["y"] > board["position"]["y"] and
            point["y"] < endTablaY):
        
        for row in range(1, board["size"]["rows"]): #COMPROBAR CON UN BUCLE ANIDADO QUE CELDA ES EN LA QUE ESTÁ ENCIMA EL RATON
            posYstartCell = board["position"]["y"] + (board["cell_size"] * row)
            posYendCell = posYstartCell + board["cell_size"]

            for col in range(1, board["size"]["cols"]):
                posXstartCell = board["position"]["x"] + (board["cell_size"] * col)
                posXendCell = posXstartCell + board["cell_size"]

                if (point["x"] > posXstartCell and
                    point["x"] < posXendCell and
                    point["y"] > posYstartCell and
                    point["y"] < posYendCell):
                    return {"row": row, "col": col}
                
    return {"row": -1, "col": -1}

def point_from_cell(cell, board): #ESTA FUNCIÓN NO LA HE USADO, NO SÉ EN QUE ERA NECESARIA

    x = board["position"]["x"] + (cell["col"] * board["cell_size"])
    y = board["position"]["y"] + (cell["row"] * board["cell_size"])

    return x, y

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
    mouse_inside = pygame.mouse.get_focused() # El ratolí està dins de la finestra?

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
    pass

# Dibuixar
def app_draw():
    screen.fill(WHITE)
    utils.draw_grid(pygame, screen, 50)

    draw_board()

    pygame.display.update()

if __name__ == "__main__":
    main()