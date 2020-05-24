import pygame
class Background:
	def __init__(self, screen):
		self.screen = screen
		self.image = pygame.image.load('background.jpg').convert()
		# self.image.set_colorkey(self.image.get_at((0, 0)))
		self.rect = self.image.get_rect()
		self.rect.x = 0
		self.rect.y = 0
	def show(self):
		self.screen.blit(self.image, self.rect)