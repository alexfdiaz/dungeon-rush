import pygame
import sys
import math
from scripts.settings import Settings
from scripts.player import Player
from scripts.mouse import Pointer
from scripts.image import Image
from scripts.text import Text
from scripts.map import Map
from scripts.minimap import MiniMap

class MainScene:
	def __init__(self):
		self.scene_id = 0

		self.next_scene = Level1()

		self.settings = Settings()

		self.pointer = Pointer()
		self.pointer.rect.center = (0, 0)

		self.player = Player()
		self.player.rect.center = (self.settings.DIS_WIDTH // 2, self.settings.DIS_HEIGHT // 2 - 25)

		self.bg = Image('resources/backgrounds/bg.png')

		self.logo = Image('resources/images/logo.png')
		self.logo.rect.center = (self.settings.DIS_WIDTH // 2, self.settings.DIS_HEIGHT // 2 - 2)

		self.text = Text('press SPACE to start', pygame.font.Font('resources/fonts/8bit.ttf', 5), (255, 255, 255), False)
		self.text.rect.center = (self.settings.DIS_WIDTH // 2, self.settings.DIS_HEIGHT // 2 + 20)

		self.rects = [
			pygame.Rect(0, -10, self.settings.DIS_WIDTH, 10),
			pygame.Rect(self.settings.DIS_WIDTH, 0, 10, self.settings.DIS_HEIGHT),
			pygame.Rect(0, self.settings.DIS_HEIGHT, self.settings.DIS_WIDTH, 10),
			pygame.Rect(-10, 0, 10, self.settings.DIS_HEIGHT)
		]

		self.frame = 0

	def render(self, surface):
		self.bg.render(surface)
		self.logo.render(surface)
		self.text.render(surface)
		self.player.render(surface, self.frame)
		self.pointer.render(surface)

	def __check_keydown(self, event):
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_w:
				self.player.moving_up = True
			if event.key == pygame.K_s:
				self.player.moving_down = True
			if event.key == pygame.K_a:
				self.player.moving_left = True
			if event.key == pygame.K_d:
				self.player.moving_right = True

	def __check_keyup(self, event):
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_ESCAPE:
				pygame.quit()
				sys.exit()
			if event.key == pygame.K_w:
				self.player.moving_up = False
			if event.key == pygame.K_s:
				self.player.moving_down = False
			if event.key == pygame.K_a:
				self.player.moving_left = False
			if event.key == pygame.K_d:
				self.player.moving_right = False

	def run(self, events, mouse_pos):
		for event in events:
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

			self.__check_keydown(event)
			self.__check_keyup(event)

		self.player.update(self.rects, mouse_pos)
		self.pointer.update(mouse_pos)

		self.frame += 1


class LevelScene:
	def __init__(self):
		pass


class Level1(LevelScene):
	def __init__(self):
		super().__init__()
		self.scene_id = 1

		self.next_scene = Level2()

		self.settings = Settings()

		self.player = Player()
		self.player.rect.center = (self.settings.DIS_WIDTH // 2, self.settings.DIS_HEIGHT // 2)

		self.health_bar = [Image('resources/images/healthbar1.png'), Image('resources/images/healthbar2.png')]
		for image in self.health_bar:
			image.rect.topleft = (2, 2)

		self.stamina_bar = [Image('resources/images/staminabar1.png'), Image('resources/images/staminabar2.png')]
		for image in self.stamina_bar:
			image.rect.topleft = (38, 1)

		self.pointer = Pointer()
		self.pointer.rect.center = (0, 0)

		self.map = Map(1)
		self.minimap = MiniMap(1)

		self.scroll = [0, 0]

		self.frame = 0

		self.black_out = pygame.Surface((self.settings.DIS_WIDTH, self.settings.DIS_HEIGHT))
		self.black_out.fill((0, 0, 0))
		self.black_out.set_alpha(0)

		self.pause = False

	def render(self, surface):
		self.map.render(surface, self.scroll)

		self.player.render(surface, self.frame, self.scroll)

		self.health_bar[1].render(surface)
		pygame.draw.rect(surface, (255, 0, 0), (12, 6, self.player.health, 4))
		self.health_bar[0].render(surface)

		self.stamina_bar[1].render(surface)
		pygame.draw.rect(surface, (255, 255, 0), (47, 6, self.player.health, 4))
		self.stamina_bar[0].render(surface)

		self.minimap.render(surface, self.player.rect.center)

		surface.blit(self.black_out, (0, 0))

		self.pointer.render(surface)

	def __check_keydown(self, event):
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_w:
				self.player.moving_up = True
			if event.key == pygame.K_s:
				self.player.moving_down = True
			if event.key == pygame.K_a:
				self.player.moving_left = True
			if event.key == pygame.K_d:
				self.player.moving_right = True

			if event.key == pygame.K_UP:
				if self.player.health < 20:
					self.player.health += 1
			if event.key == pygame.K_DOWN:
				if self.player.health > 0:
					self.player.health -= 1

	def __check_keyup(self, event):
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_ESCAPE:
				pygame.quit()
				sys.exit()

			if event.key == pygame.K_w:
				self.player.moving_up = False
			if event.key == pygame.K_s:
				self.player.moving_down = False
			if event.key == pygame.K_a:
				self.player.moving_left = False
			if event.key == pygame.K_d:
				self.player.moving_right = False

	def run(self, events, mouse_pos):
		for event in events:
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

			self.__check_keydown(event)
			self.__check_keyup(event)

		self.player.update(self.map.rects, mouse_pos)
		self.pointer.update(mouse_pos)


		self.scroll[0] += (self.player.rect.centerx - self.scroll[0] - self.settings.DIS_WIDTH // 2) / 8
		self.scroll[1] += (self.player.rect.centery - self.scroll[1] - self.settings.DIS_HEIGHT // 2) / 8

		self.frame += 1

class Level2(LevelScene):
	def __init__(self):
		super().__init__()
		self.scene_id = 2

		self.next_scene = None

	def render(self, surface):
		pass

	def run(self, events, mouse_pos):
		pass