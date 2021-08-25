import pygame
from scripts.settings import Settings

class Map:
	def __init__(self, level=0):
		self.settings = Settings()

		file = open(f'resources/levels/level{level}/tiles.txt', 'r')
		self.tiles = file.read()
		file.close()
		self.tiles = self.tiles.split('\n')
		self.tiles = [list(row) for row in self.tiles]
		self.rects = [tile for row in self.tiles for tile in row]
		self.rects = [pygame.Rect(x * self.settings.TILE_SIZE, y * self.settings.TILE_SIZE, self.settings.TILE_SIZE, self.settings.TILE_SIZE) for y, row in enumerate(self.tiles) for x, tile in enumerate(row) if tile == '1']

	def render(self, surface, scroll=[0, 0]):
		for rect in self.rects:
			pygame.draw.rect(surface, (255, 0, 0), (rect.x - scroll[0], rect.y - scroll[1], rect.w, rect.h))