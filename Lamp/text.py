"""Generates all of the text for the game. Methods return rendered text to 
be added """
import pygame
from pygame.locals import *

if not pygame.font: print "You don't have any fonts"
from LampMain import LampMain

class Title():

	def __init__(self, background, window):
		self.background = background
		self.window = window
	
	def titleScreen(self):
		# Makes the title page and waits for user to continue
		going = False
		while not going:
			if pygame.font and not going:
				font = pygame.font.Font(None,36)
				text = font.render("Press Enter To Begin!", 0, (255,255,255))

				bigTitle = pygame.font.Font(None,48)
				bigText = bigTitle.render("LAMP GAME", 0, (0,0,255))

				smallTextpos = text.get_rect(centerx=self.background.get_width()/2,
											centery=self.background.get_height()/2 +20)

				bigTextpos = bigText.get_rect(centerx=self.background.get_width()/2,
											centery=self.background.get_height()/2-20)

				self.window.blit(bigText, bigTextpos)
				self.window.blit(text, smallTextpos)
				pygame.display.flip()
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						sys.exit()
					elif event.type == KEYUP:
						if event.key == K_RETURN:
							going = True

class GameOver():
	def __init__(self, background, window):
		self.background = background
		self.window = window
	
	def gameover(self):
		# Makes the gameover page and waits for user to continue
		self.background.fill((0,0,0))
		going = False
		while not going:
			if pygame.font and not going:
				font = pygame.font.Font(None,36)
				text = font.render("press enter to restart", 0, (255,255,255))

				bigTitle = pygame.font.Font(None,48)
				bigText = bigTitle.render("GAME OVER", 0, (255,0,0))

				smallTextpos = text.get_rect(centerx=self.background.get_width()/2,
											centery=self.background.get_height()/2 +20)

				bigTextpos = bigText.get_rect(centerx=self.background.get_width()/2,
											centery=self.background.get_height()/2-20)

				self.window.blit(bigText, bigTextpos)
				self.window.blit(text, smallTextpos)
				pygame.display.flip()
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						sys.exit()
					elif event.type == KEYUP:
						if event.key == K_RETURN:
							going = True
							newGame = LampMain()
							newGame.MainLoop()
