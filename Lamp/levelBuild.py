"""loads and renders the level blocks"""

import pygame
import numpy as np

class Platform(pygame.sprite.Sprite):
	
	# Sprite constructor, so that things actually exist
	# and x and y position

	def __init__(self,topLeft=(100,100),width=20,height=20,color=(200,120,120)):
		self.width = width
		self.height = height


		# Call the Sprite constructor from pygame
		pygame.sprite.Sprite.__init__(self)

		# creates a block image, this will later be replaced
		# with code that loads a block image
		self.image = pygame.Surface([self.width, self.height])
		self.image.fill(color)

		#gets the rectangle object with image dimensions
		self.rect = self.image.get_rect()
		self.rect.x = topLeft[0]
		self.rect.y = topLeft[1]

class Construct(object):	
	
	def __init__(self):

		def zero(n):
			temp = np.zeros(n).tolist()
			return temp
		def one(n):
			temp = np.ones(n).tolist()
			return temp

		self.grid = [zero(40),
				zero(40),
				zero(40),
				zero(40),
				zero(9) + one(2) + zero(18) + one(2) + zero(9),
				zero(40),
				zero(40),
				zero(40),
				zero(40),
				zero(4) + one(4) + zero(24) + one(4) + zero(4),
				zero(40),
				zero(40),
				zero(40),
				zero(40),
				zero(10) + one(5) + zero(10) + one(5) + zero(10),
				zero(40),
				zero(40),
				zero(40),
				zero(40),
				one(40/5) + zero(40/5) + one(40/5) + zero(40/5) + one(40/5),
				zero(40),
				zero(40),
				zero(40),
				zero(40),
				one(40/3) + zero(40/3) + one(40/3 + 1),
				zero(40),
				zero(40),
				zero(40),
				zero(40),
				one(40)]

		




