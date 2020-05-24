import pygame
import sys
from settings import Settings
from naruto import Naruto 
from background import Background 
from rasengan import Rasengan 
from pygame.sprite import Group
from orochimaru import Orochimaru
from sword import Sword 
from score import Score 
def run_game():
	profile = Settings()
	pygame.init()
	screen = pygame.display.set_mode((profile.screen_width, profile.screen_height))
	pygame.display.set_caption('My Game')
	hero = Naruto(screen)
	forest = Background(screen)
	villain = Orochimaru(screen)
	rasengans = Group()
	swords = Group()

	naruto_chakra = Score(screen, (0, 138, 46), 10, 10)
	orochimaru_chakra = Score(screen, (204, 6, 13), profile.screen_width - 10 - profile.score_width, 10)
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					hero.offset(-profile.naruto_speed)		
				elif event.key == pygame.K_DOWN:
					hero.offset(profile.naruto_speed) 
				elif event.key == pygame.K_SPACE:
					if len(rasengans) < 3: 
						rasengans.add(Rasengan(screen, hero))
			elif event.type == pygame.KEYUP:
				hero.offset(0)
		hero.update()
		villain.update(swords)
		rasengans.update(villain, swords)
		swords.update(hero, rasengans)
		for j in rasengans.copy():
			if j.rect.x > profile.screen_width or j.active == False:
				rasengans.remove(j)
		for j in swords.copy():
			if j.rect.x < 0 or j.active == False:
				swords.remove(j)
		forest.show()
		hero.show()
		villain.show()
		for j in rasengans.sprites():
			j.show()
		for j in swords.sprites():
			j.show()
		orochimaru_chakra.show(villain.points / profile.total_points)
		naruto_chakra.show(hero.points / profile.total_points)
		pygame.display.flip()
run_game()