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


CELL_SIZE = 50

pos_skater = { "row": 0, "column": 0}

img_tree = get_emoji(pygame, "🌲", size=CELL_SIZE)
img_snow = get_emoji(pygame, "❄️", size=CELL_SIZE)
img_sman = get_emoji(pygame, "☃️", size=CELL_SIZE)
img_skater = get_emoji(pygame, "🏂", size=CELL_SIZE)

board = []


#FUNCIONES DEL EJERCICIO

def place_random_letters(letter, count):
    global board

    for i in range(count):
        while True:
            ranIndex1 = random.randint(0, len(board) - 1)
            ranIndex2 = random.randint(0, len(board[0]) - 1)

            if (ranIndex1 == 0 and ranIndex2 == 0) or (board[ranIndex1][ranIndex2] != ""):
                continue
            break
        board[ranIndex1][ranIndex2] = letter


def init_board():
    rowInd = []
    for row in range(8):
        for col in range(10):
            rowInd.append("")
        board.append(rowInd)
        rowInd = []
    
    place_random_letters("T", 9)
    place_random_letters("S", 3)
    place_random_letters("M", 3)


def is_skiable_cell(row, col):

    if (len(board) -1 < row or len(board[0]) - 1 < col) or (0 > row or 0 > col): #Detecta si row o col está fuera de index
        return False
    
    if board[row][col] == "T" or board[row][col] == "M":
        return False
    
    
    return True

# Bucle de l'aplicació
def main():
    is_looping = True

    init_board()

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
    global pos_skater
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if is_skiable_cell(pos_skater["row"], pos_skater["column"] - 1):
                    pos_skater["column"] -= 1
            elif event.key == pygame.K_RIGHT:
                if is_skiable_cell(pos_skater["row"], pos_skater["column"] + 1):
                    pos_skater["column"] += 1
            elif event.key == pygame.K_UP:
                if is_skiable_cell(pos_skater["row"] - 1, pos_skater["column"]):
                    pos_skater["row"] -= 1
            elif event.key == pygame.K_DOWN:
                if is_skiable_cell(pos_skater["row"] + 1, pos_skater["column"]):
                    pos_skater["row"] += 1

    return True
# Fer càlculs
def app_run():
    pass

# Dibuixar
def app_draw():
    screen.fill(WHITE)
    utils.draw_grid(pygame, screen, 50)
    
    coordsX = 0
    coordsY = 0
    for row in board:
        for col in row:
            pygame.draw.rect(screen, (173, 216, 230), ((50 + coordsX, 50 + coordsY), (50, 50)))
            if col == "T":
                screen.blit(img_tree, (50 + coordsX, 50 + coordsY))
            elif col == "M":
                screen.blit(img_sman, (50 + coordsX, 50 + coordsY))
            elif col == "S":
                screen.blit(img_snow, (50 + coordsX, 50 + coordsY))
            coordsX += 50
        coordsY += 50
        coordsX = 0
    

    pos_x_skater = (50 * pos_skater["column"]) + 50
    pos_y_skater = (50 * pos_skater["row"]) + 50

    screen.blit(img_skater, ((pos_x_skater, pos_y_skater)))
    pygame.display.update()

if __name__ == "__main__":
    main()