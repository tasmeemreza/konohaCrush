import pygame
from settings import Settings 
from random import randint
from sword import Sword 
import sys

class Orochimaru:
	def __init__(self, screen):
		self.profile = Settings()
		self.screen = screen
		self.image = pygame.image.load('trans_snake.png').convert_alpha()
		# self.image.set_colorkey(self.image.get_at((0, 0)))
		self.rect = self.image.get_rect()
		self.rect.bottom = self.screen.get_rect().bottom
		self.rect.centerx = self.screen.get_width() - self.image.get_width() // 2
		self.cnt = 0
		self.direction = 1
		self.points = self.profile.total_points

	def within_screen(self, bottom):
		if bottom >= self.image.get_height() and bottom <= self.screen.get_rect().bottom:
			return True
		else:
			return False
	def update(self, swords):
		self.cnt = (self.cnt + 1) % self.profile.orochimaru_move
		if self.cnt == 0:
			self.direction = randint(0, 1)
			if self.direction == 0:
				self.direction = -1
		if self.within_screen(self.rect.bottom + self.direction):
			self.rect.bottom += self.direction
		else: 
			self.cnt = self.profile.orochimaru_move - 1
		if randint(0, self.profile.attack_mode - 1) % self.profile.attack_mode == 0:
			swords.add(Sword(self.screen, self))

	def attacked(self):
		self.points -= 10
		if self.points < 0:
			pygame.quit()
			sys.exit()
	def show(self):
		self.screen.blit(self.image, self.rect)