#class file
import pygame
import random
from CONST import *


pygame.init()

class playerClass(pygame.Rect):
    def __init__(self, isEnemy):
        self.x = WINDOW_W / 2
        if isEnemy:
            self.y = WINDOW_H/10
        else:
            self.y = WINDOW_H - (WINDOW_H/8)
        self.width = 80
        self.height = 20
        self.velocity = playerSpeed
        self.color = (255,255,255)

    def move(self, keys):
        if keys[pygame.K_LEFT]: self.x -= self.velocity
        if keys[pygame.K_RIGHT]: self.x += self.velocity

        #print(self.x) # debug purposes

    def limit(self):
        if self.x >= WINDOW_W - self.width:
            self.x = WINDOW_W - self.width
        elif self.x <= 0:
            self.x = 0
        else:
            print("fudeu") # translate to "has fucked"

    def basic(self):
        return (self.x, self.y, self.width, self.height)





class ballClass(pygame.Rect):
    def __init__(self):
        self.x = WINDOW_W / 2
        self.y = WINDOW_H / 4
        self.lado = 15
        self.width, self.height = self.lado, self.lado # not necessary, just use lado
        self.velocity = ballSpeed
        self.color = (0,0,0)
        self.angulo = 0


    def basic(self):
        return (self.x, self.y, self.width, self.height)


    def move(self):
        self.y += self.velocity
        self.x += self.angulo
        self.color = cor_cor()


    def changeDir(self):
        self.velocity = -self.velocity
        self.angulo += random.randint(-3,3)

        #print("changed")

    def changeDirX(self):
        self.angulo = -self.angulo
        self.color = cor_cor()
