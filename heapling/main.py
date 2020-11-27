import pygame
from model import dot, heap, wall
from view import view
from pygame.draw import *

pygame.init()
screen = pygame.display.set_mode((794, 1123))
surface = pygame.Surface((794, 1123))
view = view.View(screen)
FPS = 30
WHITE = (255, 255, 255)

dots = [dot.Dot(400, 600, 10), dot.Dot(450, 450, 20), dot.Dot(550, 450, 30), dot.Dot(500, 550, 25)]

player = heap.Heap([], 500, 500, 30, 0.5, 0.8)
wall = wall.Wall([dot.Dot(200, 600, 0), dot.Dot(300, 500, 0)])

clock = pygame.time.Clock()
finished = False
i = 0

while not finished:
    i += 1
    clock.tick(FPS)
    player.step(0.00001 * FPS)
    rect(screen, WHITE, (0, 0, 794, 1123))
    player.append(dots[(i // 100) % 4])
    wall.display(view)
    for dot in dots:
        dot.display(view)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
