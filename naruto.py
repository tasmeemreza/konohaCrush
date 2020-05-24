import pygame
from settings import Settings 
import sys

class Naruto:
	def __init__(self, screen):
		self.profile = Settings()
		self.screen = screen
		self.image = pygame.image.load('trans_naruto.png').convert_alpha()
		self.rect = self.image.get_rect()
		self.screen_rect = self.screen.get_rect()
		self.rect.centerx = self.image.get_width() // 2
		self.rect.bottom = self.screen_rect.bottom
		self.direction = 0
		self.points = self.profile.total_points

	def offset(self, direction):
		self.direction = direction		
	def within_screen(self, bottom):
		if bottom >= self.image.get_height() and bottom <= self.screen_rect.bottom:
			return True
		else:
			return False

	def attacked(self):
		self.points -= 10
		if self.points < 0:
			pygame.quit()
			sys.exit()
	def update(self):
		if self.within_screen(self.rect.bottom + self.direction):
			self.rect.bottom += self.direction
	def show(self):
		self.screen.blit(self.image, self.rect)