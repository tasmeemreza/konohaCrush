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

def onKeyDown(player, key):
	if key == pygame.K_DOWN:
		player.offset(player.profile.playerSpeed)
	elif key == pygame.K_UP:
		player.offset(-player.profile.playerSpeed)
	elif key == pygame.K_SPACE:
		if len(player.weapons) < 3:
			player.attack()

def onKeyUp(player):
	player.offset(0)

def handleEvents(player, event):
	if event.type == pygame.QUIT:
		pygame.quit()
		sys.exit()
	elif event.type == pygame.KEYDOWN:
		onKeyDown(player, event.key)
	elif event.type == pygame.KEYUP:
		onKeyUp(player)

def run_game():
	profile = Settings()
	pygame.init()
	screen = pygame.display.set_mode((profile.screen_width, profile.screen_height))
	pygame.display.set_caption('Konoha Crush')
	
	forest = Background(screen)
	rasengans = Group()
	swords = Group()

	hero = Player(screen, 'images/naruto.png', rasengans, 'images/rasengan.png', True)
	villain = Player(screen, 'images/snake.png', swords, 'images/sword.png', False)

	heroChakra = Score(screen, (0, 138, 46), 10, 10)
	villainChakra = Score(screen, (204, 6, 13), profile.screen_width - 10 - profile.score_width, 10)

	while True:
		for event in pygame.event.get():
			handleEvents(hero, event)
		hero.update(villain, swords)
		villain.update(hero, rasengans)
		forest.show()
		hero.show()
		villain.show()
		heroChakra.show(villain.points / profile.total_points)
		villainChakra.show(hero.points / profile.total_points)
		pygame.display.flip()

run_game()