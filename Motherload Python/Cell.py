
# Imports
import pygame
import Mineral

class Cell:
    def __init__(self, x, y, size, heightOffset):
        self.contains = Mineral.Mineral
        self.x = x * (size + 2)
        self.y = y * (size + 2) + heightOffset
        self.rect = pygame.Rect(self.x, self.y, size, size)
        self.color = (250, 160, 90)

    def affiche(self):
        print("Cell pos is : ", self.x, self.y)