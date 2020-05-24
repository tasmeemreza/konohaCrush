import pygame
import sys
from settings import Settings
from background import Background
from player import Player 
from weapon import Weapon 
from score import Score 
from pygame.sprite import Group
from pygame.sprite import Sprite
from random import randint
from button import Button
isGirl = False

def onKeyDown(screen, player, key, running):
	if running == False and key == pygame.K_TAB:
		return True
	if player == None:
		return 
	if key == pygame.K_DOWN:
		player.offset(player.profile.playerSpeed)
	elif key == pygame.K_UP:
		player.offset(-player.profile.playerSpeed)
	elif key == pygame.K_SPACE:
		if len(player.weapons) < 3:
			player.attack()
	elif key == pygame.K_h:
		global isGirl 
		if isGirl:
			isGirl = False
		else:
			isGirl = True

def onKeyUp(player, running):
	if running:
		player.offset(0)

def handleEvents(screen, player, event, playButton, running):
	if event.type == pygame.QUIT:
		pygame.quit()
		sys.exit()
	elif event.type == pygame.KEYDOWN:
		return onKeyDown(screen, player, event.key, running)
	elif event.type == pygame.KEYUP:
		onKeyUp(player, running)
	elif event.type == pygame.MOUSEBUTTONDOWN:
		return playButton.check(pygame.mouse.get_pos())

running = False
profile = Settings()
pygame.init()
screen = pygame.display.set_mode((profile.screen_width, profile.screen_height))
pygame.display.set_caption('Konoha Crush')

wall = Background(screen, 'images/konohaCrush.jpg')
forest = Background(screen, 'images/background.jpg')
playButton = Button(screen, 'Play', (0, 0, 0), (screen.get_rect().centerx, screen.get_rect().centery))
message = Button(screen, 'Click TAB to play', (255, 255, 255), (screen.get_rect().centerx, screen.get_rect().bottom))
openingImage = True

reqInit = True
villain, hero = None, None

while True:
	for event in pygame.event.get():
		if handleEvents(screen, hero, event, playButton, running) == True:
			running = True
			openingImage = False

	if running == False:
		if openingImage: 
			wall.show()
		else: 
			forest.show()
			hero.show()
			villain.show()
		playButton.show()
		message.show()
	else:
		if reqInit:
			hero = Player(screen, 'images/naruto.png', 'images/rasengan.png', True, 'images/girl.png', 'images/love.png')
			villain = Player(screen, 'images/snake.png', 'images/sword.png', False)
			reqInit = False
		if isGirl:
			hero.changeGirl()
		else:
			hero.changeBoy()

		forest.show()
		hero.update(villain)
		villain.update(hero)
		hero.show()			
		villain.show()
		if hero.get_points() <= 0 or villain.get_points() <= 0: 
			running = False
			reqInit = True
			isGirl = False
			if hero.get_points() > 0:
				status = 'won'
			else:
				status = 'lost'
			playButton = Button(screen, 'Naruto ' + status, (255, 255, 255), (screen.get_rect().centerx, screen.get_rect().centery))
	pygame.display.flip()

