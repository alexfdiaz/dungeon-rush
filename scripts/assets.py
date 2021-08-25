import pygame
from scripts.player import Player
from scripts.text import Text
from scripts.image import Image
from scripts.mouse import Pointer
from scripts.menu import Main
from scripts.settings import Settings

class Assets:
	def __init__(self):
		self.settings = Settings()

		self.main_menu = Main()

		self.pointer = Pointer()

		self.player = Player()
		self.player.rect.center = (self.settings.DIS_WIDTH // 2, self.settings.DIS_HEIGHT // 2 - 25)

		self.curtain = pygame.Surface((self.settings.DIS_WIDTH, self.settings.DIS_HEIGHT))
		self.curtain.fill((0, 0, 0))
		self.curtain.set_alpha(0)