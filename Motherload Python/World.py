# Imports
import pygame, Cell

# Constants
TILESIZE = 64
HEIGHT_OFFSET = 500

class World:
    def __init__(self, cols, rows):
        self.cols = cols
        self.rows = rows
        self.color = (250, 160, 90)
        self.backGround = pygame.Rect(0,0,320,320)
        self.groundGrid = [[Cell.Cell(i, j, TILESIZE, HEIGHT_OFFSET) for i in range(cols)] for j in range(rows)]
        #[[self.groundGrid[i][j].affiche() for i in range(cols)] for j in range(rows)]


    def draw(self, screen):
        for i in range(self.cols):
            for j in range(self.rows):
                pygame.draw.rect(screen, self.groundGrid[i][j].color, self.groundGrid[i][j].rect)

        #[[pygame.draw.rect(screen,self.groundGrid[i][j].color,self.groundGrid[i][j].rect) for i in range(10)] for j in range(10)]
