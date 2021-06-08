import pygame
import numpy as np
import time
pygame.init();

width, height = 1000, 1000
screen = pygame.display.set_mode((height, width));

#Color de fondo
bg = 25, 25, 25

screen.fill(bg);

nxC, nyC = 100, 100

dimCW = width / nxC
dimCH = height / nyC


gameState = np.zeros((nxC, nyC));
gameState[5, 3] = 1
gameState[5, 4] = 1
gameState[5, 5] = 1
gameState[5, 2] = 1
gameState[6, 2] = 1
gameState[6, 4] = 1

gameState[21, 21] = 1
gameState[22, 22] = 1
gameState[22, 23] = 1
gameState[21, 23] = 1
gameState[20, 21] = 1
gameState[20, 20] = 1
gameState[24, 24] = 1
gameState[24, 25] = 1
gameState[24, 26] = 1
gameState[24, 27] = 1

gameState[80, 80] = 1
gameState[80, 81] = 1
gameState[82, 81] = 1
gameState[83, 83] = 1
gameState[82, 82] = 1
gameState[81, 81] = 1
gameState[81, 81] = 1
gameState[81, 82] = 1
gameState[79, 83] = 1

#bucle
while True:

    newGameState = np.copy(gameState);

    screen.fill(bg)
    time.sleep(1)

    for y in range(0, nxC):
        for x in range(0, nyC):
            n_neigh = gameState[(x - 1) % nxC, (y - 1) % nyC] + gameState[(x)     % nxC, (y - 1) % nyC] + gameState[(x + 1) % nxC, (y - 1) % nyC] + gameState[(x - 1) % nxC, (y)     % nyC] + gameState[(x + 1) % nxC, (y)     % nyC] + gameState[(x - 1) % nxC, (y + 1) % nyC] + gameState[(x)     % nxC, (y + 1) % nyC] + gameState[(x + 1) % nxC, (y + 1) % nyC]
            
            if gameState[x, y] == 0 and (n_neigh == 3):
                newGameState[x, y] = 1
            elif gameState[x, y] == 1 and (n_neigh < 2 or n_neigh > 3):
                newGameState[x, y] = 0

            poly = [
                ((x)   * dimCW, y * dimCH),
                ((x+1) * dimCW, y * dimCH),
                ((x+1) * dimCW, (y+1) * dimCH),
                ((x)   * dimCW, (y+1) * dimCH),
            ]

            if newGameState[x, y] == 0:
                pygame.draw.polygon(screen, (128, 128, 128), poly, 1)
            else:
                pygame.draw.polygon(screen, (255, 255, 255), poly, 0)
    
    gameState = np.copy(newGameState)

    pygame.display.flip()