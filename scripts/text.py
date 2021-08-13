import pygame

class Text:
	def __init__(self, text, font, color, antialias = True, background = None):
		self.text = font.render(text, antialias, color, background)
		self.rect = self.text.get_rect()

	def render(self, surface):
		surface.blit(self.text, self.rect)
