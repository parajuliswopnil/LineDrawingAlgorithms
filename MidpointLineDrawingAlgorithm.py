import pygame
import sys
from pygame.locals import QUIT
import pygame.gfxdraw

pygame.init()
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

dx = x2 - x1
dy = y2 - y1

dInit = 2 * dy - dx
delD = 2 * (dy - dx)
for i in range(max(abs(dx), abs(dy))):
    if dInit < 0:
        x1 = x1 + 1
        y1 = y1
        dInit = dInit + 2 * dy
        coordinates = (x1, y1)
        coordinateList.append(coordinates)

    elif dInit >= 0:
        x1 = x1 + 1
        y1 = y1 + 1
        dInit = dInit + delD
        coordinates = (x1, y1)
        coordinateList.append(coordinates)

print(coordinateList)


drawingSurface = pygame.display.set_mode((900, 900))
drawingSurface.fill(colorWhite)
pygame.display.set_caption("Midpoint Line Drawing Algorithm")

for i in range(len(coordinateList) - 2):
    for j in range(len(coordinateList) - 1):
        pygame.draw.line(drawingSurface, colorBlack, coordinateList[i], coordinateList[j], 2)

# updates the drawing surface
pygame.display.update()

# explicitly ending the program
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()