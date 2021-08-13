import pygame
from scripts.settings import Settings

class World:
	def __init__(self, level = 0):
		self.settings = Settings()

		self.file = open(f'resources/levels/level{level}/tiles.txt', 'r')
		self.tiles = self.file.read()
		self.file.close()
		self.tiles = self.tiles.split('\n')
		self.tiles = [list(row) for row in self.tiles]
		self.rects = [tile for row in self.tiles for tile in row]
		self.rects = [pygame.Rect(x * self.settings.TILE_SIZE, y * self.settings.TILE_SIZE, self.settings.TILE_SIZE, self.settings.TILE_SIZE) for y, row in enumerate(self.tiles) for x, tile in enumerate(row) if tile == '1']