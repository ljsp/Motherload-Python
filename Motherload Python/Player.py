import pygame,sys

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velX = 0
        self.velY = 0
        self.color = (250,120,60)
        self.rect = pygame.Rect(self.x,self.y,32,32)
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.speed = 6
        self.money = 20
        self.height = 0
        self.points = 0
        self.minerals = []
        self.reserveFuelTank = 0
        self.hullRepairNanoBots = 0
        self.dynamite = 0
        self.plasticExplosives = 0
        self.quantumTeleporter = 0
        self.matterTransmitter = 0

    def draw(self,screen):
        pygame.draw.rect(screen,self.color,self.rect)

    def update(self):
        self.velX = 0
        self.velY = 0
        if self.left_pressed and not self.right_pressed:
            self.velX = -self.speed
        if self.right_pressed and not self.left_pressed:
            self.velX = self.speed
        if self.up_pressed and not self.down_pressed:
            self.velY = -self.speed
        if self.down_pressed and not self.up_pressed:
            self.velY = self.speed

        self.x += self.velX
        self.y += self.velY

        self.rect = pygame.Rect(self.x, self.y,32,32)

    def dig(self):
        print("Digging !")