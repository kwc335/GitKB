#!/usr/bin/python
import pygame, display
pygame.init()
clock = pygame.time.Clock()	# Clock to limit speed
screen = display.setup()

for n in range(100):
	clock.tick(45)
	colour = display.random_colour(100, 255)
	display.draw_circle(colour, screen)
	pygame.display.update()
	
raw_input("Press a key")
