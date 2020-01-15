import pygame
import math
import random
from pygame import gfxdraw
pygame.init()
white = (255, 255, 255)
black = (0, 0, 0)
height = 800
dots = []
time = 0.0
radius = 100
gameloop = True
width = 600
window = pygame.display.set_mode((height, width))

while gameloop:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            gameloop = False

    x = radius * math.cos(time)
    y = radius * math.sin(time)

    r = 0+random.randint(5, 250)
    g = 0 + random.randint(5, 250)
    b = 0+random.randint(5, 250)
    dots.insert(0, y)
    window.fill(black)
    pygame.draw.circle(window, white, (150, 300), radius, 1)
    pygame.draw.circle(window, white, (150+int(x), 300+int(y)), 8)
    pygame.draw.line(window, white, (150, 300), (150+int(x), 300+int(y)))
    pygame.draw.line(window, (r, g, b), (150+x, 300 + y),
                     (350, 300+int(dots[0])))

    for i in range(len(dots)):
        gfxdraw.pixel(window, 350 + i, 300+int(dots[i]), (r, g, b))
    pygame.display.update()
    if len(dots) > 500:
        dots = dots[0:450]
    time += 0.01
