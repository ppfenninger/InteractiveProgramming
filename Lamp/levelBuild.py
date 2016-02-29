"""loads and renders the level blocks"""

import pygame


class Platform(pygame.sprite.Sprite):
	
	# Sprite constructor, so that things actually exist
	# and x and y position

	def __init__(self,centerpoint=(100,100),color=(200,120,120)
				,width=20,height=20):

		# Call the Sprite constructor from pygame
		pygame.sprite.Sprite.__init__(self)

		# creates a block image, this will later be replaced
		# with code that loads a block image
		self.image = pygame.Surface([width,height])
		self.image.fill(color)

		#gets the rectangle object with image dimensions
		self.rect = self.image.get_rect()
		self.rect.x = centerpoint[0]
		self.rect.y = centerpoint[1]