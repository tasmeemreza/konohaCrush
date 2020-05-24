import pygame
from settings import Settings 
from pygame.sprite import Sprite

class Rasengan(Sprite):
	def __init__(self, screen, naruto):
		super().__init__()
		self.profile = Settings()
		self.screen = screen
		self.image = pygame.image.load('rasengan.png').convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.centerx = naruto.rect.x + 148
		self.rect.centery = naruto.rect.y + 148
		self.active = True

	def intersect(self, p, x, y):
		if p.left <= x and x <= p.right and p.top <= y and y <= p.bottom:
			return True
		else:
			return False
	def update(self, villain, swords):
		for i in swords.sprites():
			if self.intersect(self.rect, i.rect.centerx, i.rect.centery) or self.intersect(i.rect, self.rect.centerx, self.rect.centery):
				self.active = False
		if self.intersect(villain.rect, self.rect.centerx, self.rect.centery):
			self.active = False
			villain.attacked()
		self.rect.centerx += self.profile.rasengan_speed
	def show(self):
		self.screen.blit(self.image, self.rect)
