# WRITE YOUR SOLUTION HERE:
import pygame
from datetime import datetime as dt
from math import pi, sin, cos


pygame.init()
res = (640, 480)
display = pygame.display.set_mode(res)
center = tuple(x // 2 for x in res)
ratio = pi / 1800
color = "green"

def draw(length, angle, size):
    x = center[0] + sin(angle) * length
    y = center[1] - cos(angle) * length
    pygame.draw.line(display, color, center, (x, y), size)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    time = dt.now().strftime("%I:%M:%S")
    hr, min, sec = [int(x) for x in time.split(":")]
    angle_h = (hr * 3600 + min * 60 + sec) * ratio / 12
    angle_m = (min * 60 + sec) * ratio
    angle_s = sec * ratio * 60
    
    display.fill((0, 0, 40))
    pygame.display.set_caption(time)
    pygame.draw.circle(display, color, center, 200, 5)
    pygame.draw.circle(display, color, center, 5)
    
    draw(180, angle_s, 1)
    draw(160, angle_m, 3)
    draw(120, angle_h, 5)
    
    pygame.display.flip()
