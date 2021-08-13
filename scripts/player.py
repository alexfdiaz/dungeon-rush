import pygame
import numpy as np
from scripts.settings import Settings

class Player:
	def __init__(self):
		self.settings = Settings()

		self.facing_right = True
		self.facing_left = False

		self.moving_up = False
		self.moving_down = False
		self.moving_left = False
		self.moving_right = False

		self.idle = [pygame.image.load('resources/images/player/idle1.png'), pygame.image.load('resources/images/player/idle2.png')]
		self.running = [pygame.image.load('resources/images/player/running1.png'), pygame.image.load('resources/images/player/running2.png')]
		self.rect = self.idle[0].get_rect()

	def render(self, surface, frame):
		if self.moving_up == self.moving_down == self.moving_left == self.moving_right == False:
			if self.facing_right:
				if frame % self.settings.FRAME_RATE < (self.settings.FRAME_RATE // 2):
					surface.blit(self.idle[0], self.rect)
				else:
					surface.blit(self.idle[1], self.rect)
			if self.facing_left:
				if frame % self.settings.FRAME_RATE < (self.settings.FRAME_RATE // 2):
					surface.blit(pygame.transform.flip(self.idle[0], True, False), self.rect)
				else:
					surface.blit(pygame.transform.flip(self.idle[1], True, False), self.rect)
		else:
			if self.facing_right:
				if frame % (self.settings.FRAME_RATE // 4) < (self.settings.FRAME_RATE // 8):
					surface.blit(self.running[0], self.rect)
				else:
					surface.blit(self.running[1], self.rect)
			if self.facing_left:
				if frame % (self.settings.FRAME_RATE // 4) < (self.settings.FRAME_RATE // 8):
					surface.blit(pygame.transform.flip(self.running[0], True, False), self.rect)
				else:
					surface.blit(pygame.transform.flip(self.running[1], True, False), self.rect)

	def update_pos(self, rects):
		step = 2
		rect_copy = self.rect.copy()

		if self.moving_up and not self.moving_left and not self.moving_right:
			rect_copy.y -= step
			collision_tiles = [rect for rect in rects if rect_copy.colliderect(rect)]
			if len(collision_tiles) == 0:
				self.rect = rect_copy
			else:
				self.rect.top = collision_tiles[0].bottom

		if self.moving_down and not self.moving_left and not self.moving_right:
			rect_copy.y += step
			collision_tiles = [rect for rect in rects if rect_copy.colliderect(rect)]
			if len(collision_tiles) == 0:
				self.rect = rect_copy
			else:
				self.rect.bottom = collision_tiles[0].top

		if self.moving_left and not self.moving_up and not self.moving_down:
			rect_copy.x -= step
			collision_tiles = [rect for rect in rects if rect_copy.colliderect(rect)]
			if len(collision_tiles) == 0:
				self.rect = rect_copy
			else:
				self.rect.left = collision_tiles[0].right

		if self.moving_right and not self.moving_up and not self.moving_down:
			rect_copy.x += step
			collision_tiles = [rect for rect in rects if rect_copy.colliderect(rect)]
			if len(collision_tiles) == 0:
				self.rect = rect_copy
			else:
				self.rect.right = collision_tiles[0].left

		if self.moving_up and self.moving_left:
			rect_copy.y -= int(np.sqrt(step))
			rect_copy.x -= int(np.sqrt(step))
			collision_tiles = [rect for rect in rects if rect_copy.colliderect(rect)]
			if len(collision_tiles) == 0:
				self.rect = rect_copy
			else:
				rect_copy2 = self.rect.copy()
				rect_copy2.y -= int(np.sqrt(step))
				collision_tiles = [rect for rect in rects if rect_copy2.colliderect(rect)]
				if len(collision_tiles) == 0:
					self.rect = rect_copy2
				else:
					rect_copy3 = self.rect.copy()
					rect_copy3.x -= int(np.sqrt(step))
					collision_tiles = [rect for rect in rects if rect_copy3.colliderect(rect)]
					if len(collision_tiles) == 0:
						self.rect = rect_copy3

		if self.moving_up and self.moving_right:
			rect_copy.y -= int(np.sqrt(step))
			rect_copy.x += int(np.sqrt(step))
			collision_tiles = [rect for rect in rects if rect_copy.colliderect(rect)]
			if len(collision_tiles) == 0:
				self.rect = rect_copy
			else:
				rect_copy2 = self.rect.copy()
				rect_copy2.y -= int(np.sqrt(step))
				collision_tiles = [rect for rect in rects if rect_copy2.colliderect(rect)]
				if len(collision_tiles) == 0:
					self.rect = rect_copy2
				else:
					rect_copy3 = self.rect.copy()
					rect_copy3.x += int(np.sqrt(step))
					collision_tiles = [rect for rect in rects if rect_copy3.colliderect(rect)]
					if len(collision_tiles) == 0:
						self.rect = rect_copy3

		if self.moving_down and self.moving_left:
			rect_copy.y += int(np.sqrt(step))
			rect_copy.x -= int(np.sqrt(step))
			collision_tiles = [rect for rect in rects if rect_copy.colliderect(rect)]
			if len(collision_tiles) == 0:
				self.rect = rect_copy
			else:
				rect_copy2 = self.rect.copy()
				rect_copy2.y += int(np.sqrt(step))
				collision_tiles = [rect for rect in rects if rect_copy2.colliderect(rect)]
				if len(collision_tiles) == 0:
					self.rect = rect_copy2
				else:
					rect_copy3 = self.rect.copy()
					rect_copy3.x -= int(np.sqrt(step))
					collision_tiles = [rect for rect in rects if rect_copy3.colliderect(rect)]
					if len(collision_tiles) == 0:
						self.rect = rect_copy3

		if self.moving_down and self.moving_right:
			rect_copy.y += int(np.sqrt(step))
			rect_copy.x += int(np.sqrt(step))
			collision_tiles = [rect for rect in rects if rect_copy.colliderect(rect)]
			if len(collision_tiles) == 0:
				self.rect = rect_copy
			else:
				rect_copy2 = self.rect.copy()
				rect_copy2.y += int(np.sqrt(step))
				collision_tiles = [rect for rect in rects if rect_copy2.colliderect(rect)]
				if len(collision_tiles) == 0:
					self.rect = rect_copy2
				else:
					rect_copy3 = self.rect.copy()
					rect_copy3.x += int(np.sqrt(step))
					collision_tiles = [rect for rect in rects if rect_copy3.colliderect(rect)]
					if len(collision_tiles) == 0:
						self.rect = rect_copy3