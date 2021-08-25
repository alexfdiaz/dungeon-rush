import pygame
from scripts.settings import Settings
from scripts.assets import Assets
from scripts.scene import MainScene

class Game:
	def __init__(self):
		pygame.init()

		self.settings = Settings()
		self.assets = Assets()

		self.window = pygame.display.set_mode((self.settings.WIN_WIDTH, self.settings.WIN_HEIGHT))
		self.display = pygame.Surface((self.settings.DIS_WIDTH, self.settings.DIS_HEIGHT))
		pygame.display.set_caption(self.settings.CAPTION)
		pygame.display.set_icon(pygame.image.load('icons/icon.png'))
		pygame.mouse.set_visible(False)
		pygame.mixer.music.load('resources/audio/bgsong.wav')
		pygame.mixer.music.set_volume(0.1)
		pygame.mixer.music.play(-1)

		self.clock = pygame.time.Clock()
		self.frames = 0

		self.current_stage = 0

		self.current_scene = MainScene()

	def render(self):
		self.display.fill(self.settings.BG_COLOR)

		self.current_scene.render(self.display)

		self.window.blit(pygame.transform.scale(self.display, (self.settings.WIN_WIDTH, self.settings.WIN_HEIGHT)), (0, 0))
		pygame.display.flip()

	def run(self):
		self.frame = 0
		self.alpha = 1
		
		while True:
			self.clock.tick(self.settings.FRAME_RATE)
			self.events = pygame.event.get()
			self.mouse_pos = pygame.mouse.get_pos()

			for event in self.events:
				if self.current_scene.scene_id == 0:
					if event.type == pygame.KEYUP:
						if event.key == pygame.K_SPACE:
							self.current_scene = self.current_scene.next_scene

			self.current_scene.run(self.events, self.mouse_pos)


			self.render()
			self.frame += 1


if __name__ == '__main__':
	dunrush = Game()
	dunrush.run()