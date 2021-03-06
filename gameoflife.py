import pygame
import sys
from random import randint
from time import sleep
from pygame.constants import SCALED


def genRandomPairs(m, n):
    seen = set()

    x, y = randint(m, n), randint(m, n)

    while True:
        seen.add((x, y))
        yield (x, y)
        x, y = randint(m, n), randint(m, n)
        while (x, y) in seen:
            x, y = randint(m, n), randint(m, n)


def updatePixels(pixelarr):
    temp_pixelarr = []
    for x in range(DIM_SIZE):
        temp = []
        for y in range(DIM_SIZE):
            temp.append(None)
        temp_pixelarr.append(temp)
    for x in range(DIM_SIZE):
        if x == 0 or x == DIM_SIZE-1:
            for z in range(DIM_SIZE):
                temp_pixelarr[x][z] = 0
            continue
        for y in range(DIM_SIZE):
            friends = 0
            if y == 0 or y == DIM_SIZE-1:
                temp_pixelarr[x][y] = 0
                continue
            for a in range(x-1, x+2):
                for b in range(y-1, y+2):
                    if not (a == x and b == y):
                        if pixelarr[a][b] == 1:
                            friends += 1
            if pixelarr[x][y] == 0 and friends == 3:
                temp_pixelarr[x][y] = 1
            elif pixelarr[x][y] == 1 and (friends in [2, 3]):
                temp_pixelarr[x][y] = 1
            elif pixelarr[x][y] == 1 and (friends not in [2, 3]):
                temp_pixelarr[x][y] = 0
            elif pixelarr[x][y] == 1:
                temp_pixelarr[x][y] = 0
            else:
                temp_pixelarr[x][y] = 0
    return temp_pixelarr


DIM_SIZE = 100
SCALE = 4
DIM = [DIM_SIZE*SCALE, DIM_SIZE*SCALE]


def main():
    pygame.init()
    screen = pygame.display.set_mode(DIM)
    pygame.display.set_caption("Game of Life")
    surface = pygame.display.get_surface()

    pixelarr = []
    for x in range(DIM_SIZE):
        temp = []
        for y in range(DIM_SIZE):
            temp.append(0)
        pixelarr.append(temp)

    g = genRandomPairs(0, DIM_SIZE-1)

    for _ in range(4000):
        x, y = next(g)
        pixelarr[x][y] = 1

    for v in range(0, DIM_SIZE, 20):
        for w in range(0, DIM_SIZE, 20):
            for x in range(10):
                for y in range(10):
                    pixelarr[v+x][w+y] = 1

    screen.fill((0, 0, 0))

    for x in range(DIM_SIZE):
        for y in range(DIM_SIZE):
            if pixelarr[x][y] == 1:
                pygame.draw.circle(surface, (255, 255, 255), (x, y), 1)
            else:
                pygame.draw.circle(surface, (0, 0, 0), (x, y), 1)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        for x in range(DIM_SIZE):
            for y in range(DIM_SIZE):
                if pixelarr[x][y] == 1:
                    pygame.draw.rect(surface, (255, 255, 255),
                                     pygame.Rect(x*SCALE+1, y*SCALE+1, SCALE, SCALE))
                else:
                    pygame.draw.rect(surface, (0, 0, 0),
                                     pygame.Rect(x*SCALE+1, y*SCALE+1, SCALE, SCALE))
        pygame.display.flip()
        pixelarr = updatePixels(pixelarr)
        sleep(0.1)


if __name__ == '__main__':
    main()
