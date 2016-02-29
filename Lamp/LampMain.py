"""Our Lamp adventure game.

@author: Paige and Jonathan
"""
import os, sys
import pygame
from pygame.locals import *
import levelBuild

class LampMain():
	"""This class initializes the game and contains the main loops of the game
	"""

	def __init__(self, width=800,height=600):
		"""Makes the window and displays it"""

		# initializes pygame
		pygame.init()
		pygame.display.init()

		# sets window size
		self.width = width
		self.height = height

		#creates the window
		self.window = pygame.display.set_mode((self.width, self.height))

	def MainLoop(self):
		"""The main loop of the game"""

		# creates the backgorund
		self.background = pygame.Surface(self.window.get_size())
		self.background = self.background.convert()
		self.background.fill((200,0,0))

		self.platformGroup = pygame.sprite.Group()
		tempPlat = levelBuild.Platform((0,0))
		self.platformGroup.add(tempPlat)


		while 1:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()

			self.window.blit(self.background, (0,0))
			self.platformGroup.draw(self.window)
			pygame.display.flip()


if __name__ == "__main__":
	newGame = LampMain()
	newGame.MainLoop()

