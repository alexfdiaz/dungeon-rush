import pygame

class Pointer:
	def __init__(self):
		self.img = pygame.image.load('resources/images/mouse_pointer.png')
		self.rect = self.img.get_rect()

	def render(self, surface):
		surface.blit(self.img, self.rect)

	def update(self, pos):
		self.rect.center = (pos[0] // 4, pos[1] // 4)