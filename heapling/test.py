from model.gui.button import Button, font
from utility.vector import Vector
import pygame
import os


pygame.init()
screen  = pygame.display.set_mode((1500, 1000))

buttons = []
surfaces = []

buttons.append(Button("Play the game", Vector(0,0), {"font-family": "SpaceInvaders","font-size": 20}))
buttons.append(Button("Change the way", Vector(0,0), {"font-family": "SpaceInvaders","font-size": 20}))
buttons.append(Button("Quit your hopeless actions", Vector(0,0), {"font-family": "SpaceInvaders","font-size": 20}))

for (i,button) in enumerate(buttons):
	surfaces.append(button.display()[0])

for (i,surface) in enumerate(surfaces):
	screen.blit(surface, (750-surface.get_width()//2, 300+i*200))

pygame.display.update()

clock = pygame.time.Clock()

running = True
while (running):
	clock.tick(60)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False