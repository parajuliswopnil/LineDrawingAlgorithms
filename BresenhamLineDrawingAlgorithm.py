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
slope = dy / dx
print(abs(slope))
if abs(slope) <= 1:
    p = 2 * dy - dx
    for i in range(abs(dx)):
        if p <= 0:
            x1 = x1 + 1
            y1 = y1
            p = p + 2 * dy
            coordinates = (x1, y1)
            coordinateList.append(coordinates)
        elif p > 0:
            x1 = x1 + 1
            y1 = y1 + 1
            p = p + 2 * dy - 2 * dx
            coordinates = (x1, y1)
            coordinateList.append(coordinates)

elif abs(slope) > 1:
    p = 2 * dx - dy
    print(p)
    for i in range(abs(dy)):
        if p <= 0:
            x1 = x1
            y1 = y1 + 1
            p = p + 2 * dx
            coordinates = (x1, y1)
            coordinateList.append(coordinates)
        elif p > 0:
            x1 = x1 + 1
            y1 = y1 + 1
            p = p + 2 * dx - 2 * dy
            coordinates = (x1, y1)
            coordinateList.append(coordinates)

print(coordinateList)
drawingSurface = pygame.display.set_mode((900, 900))
drawingSurface.fill(colorWhite)
pygame.display.set_caption("Bresenham's Line Drawing Algorithm")

for i in range(len(coordinateList) - 2):
    for j in range(len(coordinateList) - 1):
        pygame.draw.line(drawingSurface, colorBlack, coordinateList[i], coordinateList[j], 2)

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
