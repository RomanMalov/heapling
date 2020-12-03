import pygame
from model.scene import Scene
from utility.vector import Vector

pygame.init()
screen = pygame.display.set_mode((1500, 1000))
surface = pygame.Surface((1500, 1000))
FPS = 50

scene = Scene(Vector(0, 0), Vector(70,0), 1500, 1000)
scene.start()

clock = pygame.time.Clock()
finished = False
i = -1


while not finished:
    i += 1
    clock.tick(FPS)
    screen.blit(scene.step(0.001 * FPS), (scene.get_cords().x, scene.get_cords().y))
    pygame.display.update()
    if i==10:
        scene.heap_jump()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                scene.heap_jump() 
