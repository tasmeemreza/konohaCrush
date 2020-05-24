import pygame
class Button:
	def __init__(self, screen, text, color, pos):
		self.screen = screen
		fontClass = pygame.font.Font('images/rubber.ttf', 40)
		self.image = fontClass.render(text, True, color)
		self.rect = self.image.get_rect()
		self.rect.centerx, self.rect.bottom = pos

	def show(self):
		self.screen.blit(self.image, self.rect)
	def check(self, pos):
		return self.rect.collidepoint(pos)