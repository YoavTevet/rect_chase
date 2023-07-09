import pygame as pg

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)


class Character:

    def __init__(self, x, y, height=20, width=20, color=green, vel=5, health=1):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.rect = pg.Rect(self.x, self.y, self.width, self.height)
        self.color = color
        self.vel = vel
        self.health = health
        self.movement = {"Up": False, "Down": False, "Left": False, "Right": False}

    def reset_movement(self):
        self.movement = {"Up": False, "Down": False, "Left": False, "Right": False}

    def move_down(self):
        self.y += self.vel
        self.rect.y += self.vel

    def move_up(self):
        self.y -= self.vel
        self.rect.y -= self.vel

    def move_left(self):
        self.x -= self.vel
        self.rect.x -= self.vel

    def move_right(self):
        self.x += self.vel
        self.rect.x += self.vel

    def move(self):
        if self.movement["Up"]:
            self.move_up()
        if self.movement["Down"]:
            self.move_down()
        if self.movement["Left"]:
            self.move_left()
        if self.movement["Right"]:
            self.move_right()
