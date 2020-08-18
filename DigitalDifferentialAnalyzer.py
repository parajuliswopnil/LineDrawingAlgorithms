import pygame
import sys
from pygame.locals import QUIT
import pygame.gfxdraw

# pygame initialization
pygame.init()

# color for the canvas and the line
colorBlack = (0, 0, 0)
colorWhite = (255, 255, 255)

# calculated coordinate is saved here
coordinateList = []

# end points input
x1 = int(input("Enter x coordinate of the starting position: "))
y1 = int(input("Enter y coordinate of the starting position: "))
x2 = int(input("Enter x coordinate of the ending position: "))
y2 = int(input("Enter y coordinate of the ending position: "))

# first point appending in the coordinate list
coordinateList.append((x1, y1))

# calculating the x difference and y difference
dx = x2 - x1
dy = y2 - y1

# calculating the next coordinates
for i in range(max(dx, dy)):
   if dx >= dy:
       x1 = x1 + 1
       y1 = y1 + dy / dx
       ypass = round(y1)
       coordinates = (x1, ypass)
       coordinateList.append(coordinates)

   elif dy>dx:
       y1 = y1 + 1
       x1 = x1 + dx / dy
       xpass = round(x1)
       coordinates = (xpass, y1)
       coordinateList.append(coordinates)


# defining drawing surface
drawingSurface = pygame.display.set_mode((900, 900))
drawingSurface.fill(colorWhite)
pygame.display.set_caption("Digital Differential Analyzer Line Drawing Algorithm")

# to get the two end points needed to draw the line using pygame.draw.line()
for i in range(len(coordinateList) - 2):
    for j in range(i+1, len(coordinateList) - 1):
        pygame.draw.line(drawingSurface, colorBlack, coordinateList[i], coordinateList[j], 2)

# updates the drawing surface
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()