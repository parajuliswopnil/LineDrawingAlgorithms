import pygame
import sys
from pygame.locals import QUIT
import pygame.gfxdraw

pygame.init()
colorBlack = (0, 0, 0)
colorWhite = (255, 255, 255)



drawingSurface = pygame.display.set_mode((900, 900))
drawingSurface.fill(colorWhite)
pygame.display.set_caption("Bresenham's Line Drawing Algorithm")
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
