"""Our Lamp adventure game.

@author: Paige and Jonathan
"""
import os, sys
import pygame
from pygame.locals import *
import levelBuild
import text



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

		
		# add the platforms to the stage
		self.constructStage()

		# makes the title page and waits for user to continue
		# background and window are passed to it so they can alter the window
		# and use background dimensions
		waitScreen = text.Title(self.background, self.window)
		waitScreen.titleScreen()

		# continuously updates the game state
		while 1:
			
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()

			# updates the Surface that everything is displaying on
			self.window.blit(self.background, (0,0))
			self.platformGroup.draw(self.window)

			# refreshes the display and makes all of the changes visisble
			pygame.display.flip()

	def constructStage(self):
		# set the width of the platform blocks. BlockHeight is the same, so I just left it as one variable
		BLOCK_WIDTH = 20

		#easy way to see numner of blocks that make up x and y
		blocknumX = self.width/BLOCK_WIDTH
		blocknumY = self.height/BLOCK_WIDTH

		# creates the Group of platform Sprites. Group is like a list of Sprites
		self.platformGroup = pygame.sprite.Group()

		for x in xrange(blocknumX):
			for y in xrange(blocknumY):
				if x ==1 or y==1 or x==blocknumX-2 or y==blocknumY-2:
					tempPlat = levelBuild.Platform((x*BLOCK_WIDTH,y*BLOCK_WIDTH))
					self.platformGroup.add(tempPlat)




if __name__ == "__main__":
	newGame = LampMain()
	newGame.MainLoop()

