from scripts.image import Image
import pygame

class Button:
	def __init__(self, *paths):
		self.images = [pygame.image.load(path) for path in paths]
		self.rect = self.images[0].get_rect()
		self.pressed = False

	def render(self, surface):
		if not self.pressed:
			surface.blit(self.images[0], self.rect)
		else:
			surface.blit(self.images[1], self.rect)