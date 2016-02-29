"""Generates all of the text for the game. Methods return rendered text to 
be added """
import pygame
from pygame.locals import *

if not pygame.font: print "You don't have any fonts"

class Title():
	
	def __init__(self):
		"""Creats the title screen"""

		if pygame.font:
			font = pygame.font.Font(None,36)
			text = font.render("Press Enter To Begin!")
			bigTitle = pygame.font.Font(none,48)
			bigText = bigTitle.render
			return [text, bigText]
		
		# if pygame.font:
		# 		bigTitle = pygame.font.Font(none,48)
		# 		bigText = bigTitle.render
  #             font = pygame.font.Font(None, 36)
  #             text = font.render("Pellets %s" % self.snake.pellets
  #                                   , 1, (255, 0, 0))
  #               textpos = text.get_rect(centerx=self.background.get_width()/2)
  #               self.screen.blit(text, textpos)