import pygame

class Image:
	def __init__(self, path):
		self.image = pygame.image.load(path)
		self.rect = self.image.get_rect()

	def render(self, surface, scroll=[0, 0]):
		surface.blit(self.image, self.rect)