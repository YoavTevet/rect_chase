import pygame as pg
import math

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)


class Enemy:

    def __init__(self, x, y, height=20, width=20, color=red, vel=4, damage=1):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.color = color
        self.vel = vel
        self.damage = damage
        self.rect = pg.Rect(self.x, self.y, self.width, self.height)
        self.timer = 0

    def chase(self, x, y):
        dx = self.x - x
        dy = self.y - y

        distance = math.sqrt(dx**2 + dy**2)
        steps = distance / self.vel

        self.x -= dx/steps
        self.y -= dy/steps

        self.rect.x = self.x
        self.rect.y = self.y

        self.timer += 1
