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
	def __init__(self, screen, playerPath, weaponPath, isLeft, alternate=None, alternateWeapon=None):
		# print('init', playerPath)
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
		self.points = self.profile.totalPoints
		self.isLeft = isLeft
		self.direction = 0
		self.weapons = Group()
		self.weaponPath = weaponPath
		self.cnt = 0
		if isLeft:
			xCoord = 10
			bgColor = (0, 138, 46)
		else:
			xCoord = self.screen.get_width() - 10 - self.profile.scoreWidth
			bgColor = (204, 6, 13)
		self.chakra = Score(screen, bgColor, xCoord, 10)
		self.alternate = alternate
		self.alternateWeapon = alternateWeapon
		self.playerPath = playerPath
		self.isMale = True

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

	def changeBoy(self):
		if self.isMale:
			return 
		self.weaponPath, self.alternateWeapon = self.alternateWeapon, self.weaponPath
		self.image = pygame.image.load(self.playerPath)
		self.rect = self.image.get_rect()
		self.rect.x, self.rect.y = self.x, self.y
		self.isMale = True

	def changeGirl(self):
		if not self.isMale:
			return 
		self.weaponPath, self.alternateWeapon = self.alternateWeapon, self.weaponPath
		self.image = pygame.image.load(self.alternate)
		self.rect = self.image.get_rect()
		self.rect.x, self.rect.y = self.x, self.y
		self.isMale = False

	def get_points(self):
		return self.points

	def randomMovement(self, opponent):
		self.cnt = (self.cnt + 1) % self.profile.maxMove 
		if self.cnt == 0:
			self.direction = randint(0, 1)
			if self.direction == 0:
				self.direction = -1
		if self.within_screen(self.rect.bottom + self.direction):
			self.rect.bottom += self.direction
		else: 
			self.cnt = self.profile.maxMove - 1
		mult = 1
		if not opponent.isMale:
			mult *= 2
		if randint(0, self.profile.attackMode * mult - 1) % (mult * self.profile.attackMode) == 0:
			self.attack()

	def update(self, opponent):
		opponentWeapons = opponent.weapons
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
			self.randomMovement(opponent)
	
	def show(self):
		self.screen.blit(self.image, self.rect)
		for j in self.weapons.sprites():
			j.show()
		self.chakra.show(self.points / self.profile.totalPoints)