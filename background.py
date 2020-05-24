import pygame
class Background:
	def __init__(self, screen, path):
		self.screen = screen
		self.image = pygame.image.load(path).convert()
		self.rect = self.image.get_rect()
		self.rect.x = 0
		self.rect.y = 0
	def show(self):
		self.screen.blit(self.image, self.rect)