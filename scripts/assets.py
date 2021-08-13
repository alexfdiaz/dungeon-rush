import pygame
from scripts.player import Player
from scripts.world import World
from scripts.button import Button
from scripts.image import Image
from scripts.settings import Settings

class Assets:
	def __init__(self):
		self.settings = Settings()

		self.large_font = pygame.font.Font(self.settings.FONT, 18)
		self.small_font = pygame.font.Font(self.settings.FONT, 10)

		self.player = Player()
		self.player.rect.center = (self.settings.DIS_WIDTH // 2, self.settings.DIS_HEIGHT // 2 - 40)

		self.world = World()

		self.bg = Image('resources/backgrounds/bg.png')

		self.logo = Image('resources/images/logo.png')
		self.logo.rect.midbottom = (self.settings.DIS_WIDTH // 2, self.settings.DIS_HEIGHT // 2 - 2)

		self.play = Button('resources/images/unpressed_play.png', 'resources/images/pressed_play.png')
		self.play.rect.topleft = (self.logo.rect.x, self.settings.DIS_HEIGHT // 2 + 2)

		self.options = Button('resources/images/unpressed_options.png', 'resources/images/pressed_options.png')
		self.options.rect.topleft = (self.settings.DIS_WIDTH // 2 + 2, self.settings.DIS_HEIGHT // 2 + 2)