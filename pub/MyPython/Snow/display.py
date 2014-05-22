import pygame, random
WIDTH = 600; HEIGHT = 600

def setup():
	BLACK = (0, 0, 0)
	screen = pygame.display.set_mode([WIDTH, HEIGHT])
	screen.fill(BLACK)
	return screen

def draw_circle(colour, screen):
	x = random.randint(1, WIDTH)
	y = random.randint(1, HEIGHT);
	size = random.randint(1, 5)
	pygame.draw.circle(screen, colour, (x, y), size)

def random_colour(minimum, maximum):
	red = random.randint(minimum, maximum)
	green = random.randint(minimum, maximum)
	blue = random.randint(minimum, maximum)
	colour = [red, green, blue]
	return colour
