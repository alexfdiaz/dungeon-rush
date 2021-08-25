import pygame
from scripts.settings import Settings

class MiniMap:
	def __init__(self, level):
		self.settings = Settings()

		file = open(f'resources/levels/level{level}/tiles.txt', 'r')
		self.tiles = file.read()
		file.close()

		self.tiles = self.tiles.split('\n')
		self.tiles = [list(row) for row in self.tiles]

		self.surface = pygame.Surface((len(self.tiles[0]), len(self.tiles)))
		self.surface.set_alpha(100)


	def render(self, surface, player_pos):
		self.surface.fill((0, 0, 0))

		for y, row in enumerate(self.tiles):
			for x, tile in enumerate(row):
				if tile != '0':
					pygame.draw.rect(self.surface, (150, 150, 150), (x, y, 1, 1))

		pygame.draw.rect(self.surface, (255, 255, 255), (player_pos[0] // 8, player_pos[1] // 8, 1, 1))

		pos = (self.settings.DIS_WIDTH - self.surface.get_width() - 1, 1)
		surface.blit(self.surface, pos)