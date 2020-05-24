import pygame
import sys
from settings import Settings
from background import Background
from weapon import Weapon 
from score import Score 
from pygame.sprite import Group
from pygame.sprite import Sprite
from random import randint
class Player:
	def __init__(self, screen, playerPath, weapons, weaponPath, isLeft):
		self.profile = Settings()
		self.screen = screen
		self.image = pygame.image.load(playerPath).convert_alpha()
		self.rect = self.image.get_rect()
		if isLeft:
			self.x = 0
		else:
			self.x = self.screen.get_width() - self.image.get_width()
		self.y = self.screen.get_height() - self.image.get_height()
		self.rect.x, self.rect.y = self.x, self.y
		self.points = self.profile.total_points
		self.isLeft = isLeft
		self.direction = 0
		self.weapons = weapons
		self.weaponPath = weaponPath
		self.cnt = 0
		if not isLeft:
			self.profile.weaponSpeed *= -1
	
	def offset(self, direction):
		self.direction = direction		
	
	def within_screen(self, bottom):
		if bottom >= self.image.get_height() and bottom <= self.screen.get_rect().bottom:
			return True
		else:
			return False

	def attack(self):
		self.weapons.add(Weapon(self, self.weaponPath, (148, 148)))

	def attacked(self):
		self.points -= 10
		if self.points < 0:
			pygame.quit()
			sys.exit()

	def randomMovement(self):
		self.cnt = (self.cnt + 1) % self.profile.maxMove 
		if self.cnt == 0:
			self.direction = randint(0, 1)
			if self.direction == 0:
				self.direction = -1
		if self.within_screen(self.rect.bottom + self.direction):
			self.rect.bottom += self.direction
		else: 
			self.cnt = self.profile.maxMove - 1
		if randint(0, self.profile.attackMode - 1) % self.profile.attackMode == 0:
			self.attack()

	def update(self, opponent, opponentWeapons):
		self.weapons.update(opponent, opponentWeapons)
		for j in self.weapons.sprites():
			if j.rect.right < 0 or j.rect.left > self.screen.get_width():
				j.active = False
		for j in self.weapons.copy():
			if j.active == False:
				self.weapons.remove(j)
		if self.isLeft:
			if self.within_screen(self.rect.bottom + self.direction):
				self.y += self.direction
				self.rect.x, self.rect.y = self.x, self.y
		else:
			self.randomMovement()
	def show(self):
		self.screen.blit(self.image, self.rect)
		for j in self.weapons.sprites():
			j.show()