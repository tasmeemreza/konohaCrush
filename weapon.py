import pygame
import sys
from settings import Settings
from background import Background
from score import Score 
from pygame.sprite import Group
from pygame.sprite import Sprite
from random import randint

class Weapon(Sprite):
	def __init__(self, player, path, position):
		super().__init__()
		self.profile = player.profile
		self.screen = player.screen
		self.image = pygame.image.load(path).convert_alpha()
		self.rect = self.image.get_rect()
		self.x = player.rect.x + position[0]
		self.y = player.rect.y + position[1]
		self.rect.centerx, self.rect.centery = self.x, self.y
		self.active = True
		self.path = path
		self.xDir = randint(-1, 1)
		self.isLeft = player.isLeft

	def update(self, opponent, opponentWeapons):
		for i in opponentWeapons.sprites():
			if self.rect.collidepoint((i.rect.centerx, i.rect.centery)) or i.rect.collidepoint((self.x, self.y)):
				self.active = False
				i.active = False
		if opponent.rect.collidepoint((self.rect.centerx, self.rect.centery)):
			self.active = False
			opponent.attacked()
		if self.isLeft:
			self.x += self.profile.weaponSpeed
		else:
			self.x -= self.profile.weaponSpeed
			self.y += self.xDir
		self.rect.centerx, self.rect.centery = self.x, self.y
	def show(self):
		self.screen.blit(self.image, self.rect)
