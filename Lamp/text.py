"""Generates all of the text for the game. Methods return rendered text to 
be added """
import pygame
from pygame.locals import *

if not pygame.font: print "You don't have any fonts"

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

	def endScreen(self):
		#makes the death screen and waits for the user to continue
		going = False
		while not going:
			if pygame.font and not going:
				font = pygame.font.Font(None,36)
				text = font.render("Press Enter to Begin Again", 0, (255,255,255))

				bigTitle = pygame.font.Font(None,48)
				bigText = bigTitle.render("You Arrived Home Safely!", 0, (0,0,255))

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