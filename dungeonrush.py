import pygame, sys
from scripts.settings import Settings
from scripts.assets import Assets

class Game:
	def __init__(self):
		pygame.init()

		self.settings = Settings()
		self.assets = Assets()

		self.window = pygame.display.set_mode((self.settings.WIN_WIDTH, self.settings.WIN_HEIGHT))
		self.display = pygame.Surface((self.settings.DIS_WIDTH, self.settings.DIS_HEIGHT))
		pygame.display.set_caption(self.settings.CAPTION)
		pygame.display.set_icon(pygame.image.load('icons/icon.png'))
		self.clock = pygame.time.Clock()
		self.frames = 0

	def render(self):
		self.display.fill(self.settings.BG_COLOR)
		self.assets.bg.render(self.display)

		for rect in self.assets.world.rects:
				#pygame.draw.rect(self.display, (255, 0, 0), rect)
				pass

		self.assets.logo.render(self.display)

		self.assets.play.render(self.display)
		self.assets.options.render(self.display)

		self.assets.player.render(self.display, self.frame)

		self.window.blit(pygame.transform.scale(self.display, (self.settings.WIN_WIDTH, self.settings.WIN_HEIGHT)), (0, 0))
		pygame.display.flip()

	def check_keydown(self, event):
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_w:
				self.assets.player.moving_up = True
			if event.key == pygame.K_s:
				self.assets.player.moving_down = True
			if event.key == pygame.K_a:
				self.assets.player.moving_left = True
				self.assets.player.facing_right = False
				self.assets.player.facing_left = True
			if event.key == pygame.K_d:
				self.assets.player.moving_right = True
				self.assets.player.facing_right = True
				self.assets.player.facing_left = False

	def check_keyup(self, event):
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_ESCAPE:
				sys.exit()
			if event.key == pygame.K_w:
				self.assets.player.moving_up = False
			if event.key == pygame.K_s:
				self.assets.player.moving_down = False
			if event.key == pygame.K_a:
				self.assets.player.moving_left = False
			if event.key == pygame.K_d:
				self.assets.player.moving_right = False

	def check_mousedown(self, event):
		if event.type == pygame.MOUSEBUTTONDOWN:
			x, y = pygame.mouse.get_pos()
			mouse_pos = (x // 4, y // 4)
			if self.assets.play.rect.collidepoint(mouse_pos):
				self.assets.play.pressed = True
			if self.assets.options.rect.collidepoint(mouse_pos):
				self.assets.options.pressed = True

	def check_mouseup(self, event):
		if event.type == pygame.MOUSEBUTTONUP:
			self.assets.play.pressed = False
			self.assets.options.pressed = False

	def run(self):
		self.frame = 0
		bg_shift = 0
		while True:
			self.clock.tick(self.settings.FRAME_RATE)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()

				self.check_keydown(event)
				self.check_keyup(event)
				self.check_mousedown(event)
				self.check_mouseup(event)

			self.assets.player.update_pos(self.assets.world.rects)

			if self.frame % 5 == 0:
				self.assets.bg.rect.y = (-self.settings.DIS_HEIGHT + bg_shift % 40)
				bg_shift += 1

			self.render()
			self.frame += 1


if __name__ == '__main__':
	dunrush = Game()
	dunrush.run()