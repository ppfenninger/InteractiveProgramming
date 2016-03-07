"""Our Lamp adventure game.

@author: Paige and Jonathan
"""
import os, sys
import pygame
from pygame.locals import *
import lampSprite
import levelBuild
import text
import lampSprite
import time
import numpy


class LampMain():
	"""This class initializes the game and contains the main loops of the game
	"""

	def __init__(self, width=800,height=600):
		"""Makes the window and displays it"""
		# creates our lamp object
		self.lamp = lampSprite.Lamp((400, 550), 'lamp.png')

		# initializes pygame
		pygame.init()
		pygame.display.init()

		# sets window size
		self.width = width
		self.height = height

		#creates the window
		self.window = pygame.display.set_mode((self.width, self.height))

		self.oneAgo = (0,0)
		self.twoAgo = (0,0)


	def MainLoop(self):
		"""The main loop of the game"""

		# creates the backgorund
		self.background = pygame.Surface(self.window.get_size())
		self.background = self.background.convert()
		self.background.fill((200,0,0))

		keyPressed = False
		# add the platforms to the stage
		self.constructStage()

		# makes the title page and waits for user to continue
		# background and window are passed to it so they can alter the window
		# and use background dimensions
		waitScreen = text.Title(self.background, self.window)
		waitScreen.titleScreen()
		# continuously updates the game state
		pygame.key.set_repeat(3, 50)

		while 1:
			time.sleep(.005)
			if not pygame.sprite.spritecollide(self.lamp, self.platformGroup, False):
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						sys.exit()
					elif event.type == KEYDOWN:
						if ((event.key == K_RIGHT)
						or (event.key == K_LEFT)
						or (event.key == K_UP)
						or (event.key == K_DOWN)):
							self.lamp.MoveKeyDown(event.key)		
					elif event.type == KEYUP:
						if ((event.key == K_RIGHT)
						or (event.key == K_LEFT)
						or (event.key == K_UP)
						or (event.key == K_DOWN)):
							self.lamp.MoveKeyUp(event.key)
						
												
			self.lamp.update(self.platformGroup, self.width, self.height)
			# updates the Surface that everything is displaying on
			self.window.blit(self.background, (0,0))
			self.platformGroup.draw(self.window)
			self.window.blit(self.lamp.image, self.lamp.rect)

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

		constructor = levelBuild.Construct()
		newGrid = constructor.grid


		for y in xrange(len(newGrid)):
			for x in xrange(len(newGrid[y])):
				if newGrid[y][x] == 1:
					tempPlat = levelBuild.Platform((x*BLOCK_WIDTH,y*BLOCK_WIDTH),BLOCK_WIDTH,BLOCK_WIDTH)
					self.platformGroup.add(tempPlat)




if __name__ == "__main__":
	newGame = LampMain()
	newGame.MainLoop()

