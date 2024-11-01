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
    dades = [ 
        {'nom': 'Pelut', 'any': 2018, 'pes': 6.5, 'especie': 'Gos'},
        {'nom': 'Pelat', 'any': 2020, 'pes': 5.0, 'especie': 'Gos'},
        {'nom': 'Mia', 'any': 2022, 'pes': 3.0, 'especie': 'Gat'},
        {'nom': 'Nemo', 'any': 2003, 'pes': 0.1, 'especie': 'Peix'},
        {'nom': 'Mickey', 'any': 1928, 'pes': 0.5, 'especie': 'Ratolí'},
        {'nom': 'Donald', 'any': 1934, 'pes': 0.5, 'especie': 'Ànec'} 
        ]
    
    pygame.draw.rect(screen, WHITE, ((150, 100), (50 * len(dades[0]), 25 * len(dades))))

    #DIBUJAR LAS LINEAS NEGRAS DE LA TABLA
    coordsY = 0
    for i in range(len(dades) + 1):
        pygame.draw.line(screen, BLACK, (150, 100 + coordsY), (150 + (50 * len(dades[0])), 100 + coordsY), 3)
        coordsY += 25
    
    #PONER EL TEXTO
    fuenteNom = pygame.font.SysFont('Arial', 18)
    fuenteDatos = pygame.font.SysFont('Arial', 16)
    coordsY = 0

    for dic in dades:
        txtNom = fuenteNom.render(dic["nom"], True, BLACK)
        screen.blit(txtNom, (155, 103 + coordsY))

        txtDato1 = fuenteDatos.render(str(dic['any']), True, (50, 120, 200))
        screen.blit(txtDato1, (255, 104 + coordsY))

        txtDato2 = fuenteDatos.render(dic["especie"], True, (50, 120, 200))
        screen.blit(txtDato2, (305, 104 + coordsY))

        coordsY += 25


    pygame.display.update()

if __name__ == "__main__":
    main()