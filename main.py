import pygame as pg
import sys
import os
from player import Character
from enemy import Enemy


red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)

DISPLAY_SIZE = (1200, 800)
screen = pg.display.set_mode(DISPLAY_SIZE)

pg.init()
current_path = os.path.dirname(__file__)
clock = pg.time.Clock()

player = Character(600, 400)
enemies = [Enemy(250, 250)]


def move_player():
    keys = pg.key.get_pressed()
    if keys[pg.K_UP] or keys[pg.K_w]:
        player.movement["Up"] = True
    if keys[pg.K_DOWN] or keys[pg.K_s]:
        player.movement["Down"] = True
    if keys[pg.K_LEFT] or keys[pg.K_a]:
        player.movement["Left"] = True
    if keys[pg.K_RIGHT] or keys[pg.K_d]:
        player.movement["Right"] = True

    player.move()  # Hello
    player.reset_movement()


def redraw_game_window():  # draws everything that needs to be on the screen
    screen.fill(black)

    pg.draw.rect(screen, player.color, player.rect)  # draw player rect

    for e in enemies:
        pg.draw.rect(screen, e.color, e.rect)


while True:
    clock.tick(60)

    # loop that checks all the events and updates states according to user input
    for event in pg.event.get():
        if event.type == pg.QUIT:  # if 'X' button is pressed
            pg.quit()
            sys.exit()

    move_player()
    for e in enemies:
        e.chase(player.x, player.y)
        if e.rect.colliderect(player.rect):
            # timer prevents enemy from hitting player multiple times per second
            if e.timer > 25:
                print("Hit")
                player.health -= e.damage
                e.timer = 0

    redraw_game_window()
    pg.display.update()
