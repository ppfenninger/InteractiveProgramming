"""loads and renders the level blocks"""

import pygame


class Platform(pygame.sprite.Sprite):
	
	# Sprite constructor, so that things actually exist
	# and x and y position

	def __init__(self,topLeft=(100,100),width=20,height=20,color=(200,120,120)):

		# Call the Sprite constructor from pygame
		pygame.sprite.Sprite.__init__(self)

		# creates a block image, this will later be replaced
		# with code that loads a block image
		self.image = pygame.Surface([width,height])
		self.image.fill(color)

		#gets the rectangle object with image dimensions
		self.rect = self.image.get_rect()
		self.rect.x = topLeft[0]
		self.rect.y = topLeft[1]

