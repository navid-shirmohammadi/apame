"""
moified code
github user:6220679
skrx
link:https://stackoverflow.com/questions/15098900/how-to-set-the-pivot-point-center-of-rotation-for-pygame-transform-rotate
"""

import pygame as pg


def rotate(surface, angle, pivot, offset):
    rotated_image = pg.transform.rotozoom(surface, -angle, 1)
    rotated_offset = offset.rotate(angle)
    rect = rotated_image.get_rect(center=pivot+rotated_offset)
    return rotated_image, rect


pg.init()
screen = pg.display.set_mode((640, 480))
clock = pg.time.Clock()
BG_COLOR = pg.Color('gray12')

IMAGE = pg.image.load('1.jpg').convert_alpha()
pivot = [200, 250]
offset = pg.math.Vector2(100, 0)
angle = 0

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    keys = pg.key.get_pressed()
    if keys[pg.K_d] or keys[pg.K_RIGHT]:
        angle += 1
    elif keys[pg.K_a] or keys[pg.K_LEFT]:
        angle -= 1
    if keys[pg.K_f]:
        pivot[0] += 2

    rotated_image, rect = rotate(IMAGE, angle, pivot, offset)

    screen.fill(BG_COLOR)
    screen.blit(rotated_image, rect)
    pg.draw.circle(screen, (30, 250, 70), pivot, 3)
    pg.display.set_caption('Angle: {}'.format(angle))
    pg.display.flip()
    clock.tick(30)

pg.quit()
