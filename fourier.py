import pygame
import math
import random
from pygame import gfxdraw
pygame.init()
white = (255, 255, 255)
black = (0, 0, 0)
height = 800
n = 1
dots = []
time = 0
radius = 100
gameloop = True
clock = pygame.time.Clock()
x = 0
y = 0
width = 600
window = pygame.display.set_mode((height, width))

while gameloop:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            gameloop = False

    x = y = 0

    window.fill(black)
    for i in range(50):
        prevx = x
        prevy = y
        n = i*2 + 1
        radius = 100 * (4/(n*math.pi))
        x += radius * math.cos(n*time)
        y += radius * math.sin(n*time)

        r = 0+random.randint(5, 250)
        g = 0 + random.randint(5, 250)
        b = 0+random.randint(5, 250)

        pygame.draw.circle(window, white, (150+int(prevx),
                                           300+int(prevy)), int(radius), 1)
        pygame.draw.circle(window, white, (150+int(x), 300+int(y)), 8)
        pygame.draw.line(window, white, (150+int(prevx), 300+int(prevy)),
                         (150+int(x), 300+int(y)))

    #clock.tick(300)

    dots.insert(0, y)
    pygame.draw.line(window, (r, g, b), (150+x, 300 + y),
                     (350, 300+int(dots[0])))
    for i in range(len(dots)-2):
        #gfxdraw.pixel(window, 350 + i, 300+int(dots[i]), (r, g, b))
        pygame.draw.polygon(window,(r,g,b),((350+i,300+dots[i]),(350+i+1,300+dots[i+1]),(350+i+2,300+dots[i+2])),5)
    pygame.display.update()
    if len(dots) > 500:
        dots = dots[0:450]

    time += 0.01
