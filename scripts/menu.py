import pygame
from scripts.image import Image
from scripts.text import Text
from scripts.settings import Settings

class Main:
	def __init__(self):
		self.settings = Settings()

		self.bg = Image('resources/backgrounds/bg.png')

		self.logo = Image('resources/images/logo.png')
		self.logo.rect.center = (self.settings.DIS_WIDTH // 2, self.settings.DIS_HEIGHT // 2 - 2)

		self.text = Text('press SPACE to start', pygame.font.Font('resources/fonts/8bit.ttf', 5), (255, 255, 255), False)
		self.text.rect.center = (self.settings.DIS_WIDTH // 2, self.settings.DIS_HEIGHT // 2 + 20)

		self.frame = 0
		self.bg_shift = 0

		self.stage = 0

	def render(self, surface):
		self.bg.render(surface)
		self.logo.render(surface)
		self.text.render(surface)

	def check_mousedown(self, event, mouse_pos):
		pass

	def check_mouseup(self, event, mouse_pos):
		pass

	def run(self, events, mouse_pos):
		mouse_pos = (mouse_pos[0] // 4, mouse_pos[1] // 4)
		for event in events:
			self.check_mousedown(event, mouse_pos)
			self.check_mouseup(event, mouse_pos)

		self.frame += 1

		return self.stage