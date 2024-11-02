#!/usr/bin/env python3

import math
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import sys
import utils
import random

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
size = 35
sizeNum = 18
board = []
rows = 10
columns = 15


for row in range(rows):
    indArr = []
    for col in range(columns):
        indArr.append(random.randint(0,9))
    board.append(indArr)

def draw_board():
    fuenteNums = pygame.font.SysFont('Arial', sizeNum)
    for row in range(rows):
        for col in range(columns):
            celdaAfectada = mouseOnCelda()
            numeroCelda = numeroEnCelda(celdaAfectada, board)

            if celdaAfectada != [-1, -1] and numeroCelda != "":
                if row == celdaAfectada[0] and col == celdaAfectada[1]: #ESTO PINTA LA CELDA EN LA QUE ESTÁ EL RATÓN
                    pygame.draw.rect(screen, BLUE, (((50 + (size * col), (50 + (size * row)))), (size, size)))

                if numeroCelda == board[row][col]:  #ESTO PINTA TODAS LAS CELDAS CON COINCIDENCIAS EN EL NUMERO
                    pygame.draw.rect(screen, BLUE, (((50 + (size * col), (50 + (size * row)))), (size, size))) 

                if mouseClick == True: #ESTO ELIMINA LAS CELDAS CON LAS COINCIDENCIAS REEMPLAZANDO EL NUMERO POR UN HUECO VACÍO
                    for fila in range(rows):
                        for columna in range(columns):
                            if board[fila][columna] == numeroCelda:
                                board[fila][columna] = ""

            pygame.draw.rect(screen, BLACK, (((50 + (size * col), (50 + (size * row)))), (size, size)), 3)

            txtNum = fuenteNums.render(str(board[row][col]), True, BLACK)
            screen.blit(txtNum, (57 + (size * col), 57 + (size * row)))

def mouseOnCelda():
    if (mouse_pos["x"] > 50 and
        mouse_pos["x"] < (50 * len(board[0])) and #COMPROBANDO SI EL MOUSE ESTÁ DENTRO DE LA TABLA
        mouse_pos["y"] > 50 and
        mouse_pos["y"] < (50 * len(board))):
            
            for row in range(rows):
                startYCell = 50 + (size * row)
                endYCell = startYCell + size
                for col in range(columns):
                    startXCell = 50 + (size * col)
                    endXCell = startXCell + size
                    if (mouse_pos["x"] > startXCell and
                        mouse_pos["x"] < endXCell and
                        mouse_pos["y"] > startYCell and
                        mouse_pos["y"] < endYCell):
                        return [row, col]
                    
    return [-1, -1]

def numeroEnCelda(celda, tabla):
    return tabla[celda[0]][celda[1]]

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
    global mouse_pos, mouseClick
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
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouseClick = True
        else:
            mouseClick = False
    return True
# Fer càlculs
def app_run():
    pass

# Dibuixar
def app_draw():
    screen.fill(WHITE)
    #utils.draw_grid(pygame, screen, 50)

    draw_board()

    pygame.display.update()

if __name__ == "__main__":
    main()