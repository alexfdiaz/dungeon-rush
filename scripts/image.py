import pygame

class Image:
	def __init__(self, path):
		self.image = pygame.image.load(path)
		self.rect = self.image.get_rect()

	def render(self, surface):
		surface.blit(self.image, self.rect)