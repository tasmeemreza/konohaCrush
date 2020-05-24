import pygame
from settings import Settings 
class Score:
	def __init__(self, screen, color, x, y):
		self.profile = Settings()
		self.screen = screen
		self.x, self.y = x, y
		self.color = color
	def show(self, val):
		offsetX = val * self.profile.scoreWidth
		pygame.draw.rect(self.screen, self.color, pygame.Rect(self.x, self.y, offsetX, self.profile.scoreHeight))
		pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(self.x, self.y, self.profile.scoreWidth, self.profile.scoreHeight), 5)
