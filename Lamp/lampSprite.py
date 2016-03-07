import os, sys
import pygame
from pygame.locals import *
import LampMain

class Lamp(pygame.sprite.Sprite):
	
	def __init__(self, centerPoint, name):
		# creates Sprite
		pygame.sprite.Sprite.__init__(self)

		fullname = os.path.join('images')
		fullname = os.path.join(fullname, name)
		image = pygame.image.load(fullname)
		image = pygame.transform.scale(image, (40, 40))
		self.image = image
		#moves sprite into correct location
		self.rect = image.get_rect()
		self.rect.center = centerPoint
		#sets the number of pixels we are going to mossve each time
		self.xDist = 1
		self.yDist = 1
		#initializes how much we are moving
		self.xMove = 0
		self.yMove = 0
		self.canJump = True

	def MoveKeyDown(self, key):
		
		if (key == K_RIGHT):
			self.xMove += self.xDist
			self.yMove = 0
		elif (key == K_LEFT):
			self.xMove += -self.xDist
			self.yMove = 0
		elif (key == K_UP):
			self.yMove += -self.yDist
			self.xMove = 0
		elif (key == K_DOWN):
			self.yMove += self.yDist
			self.xMove = 0

	def MoveKeyUp(self, key):
		if (key == K_RIGHT):
			if self.xMove != 0:
				self.xMove += -self.xDist
		elif (key == K_LEFT):
			if self.xMove != 0:
				self.xMove += self.xDist
		elif (key == K_UP):
			if self.yMove != 0:
				self.yMove += self.yDist
		elif (key == K_DOWN):
			if self.yMove != 0:	
				self.yMove += -self.yDist

	def update(self, platformGroup):
		if pygame.sprite.spritecollide(self, platformGroup, False):
			self.canJump = True
		else:
			self.canJump = False

		if pygame.sprite.spritecollide(self, platformGroup, False):
			self.rect.move_ip(-3*self.xMove, -3*self.yMove)

		else:
			self.rect.move_ip(self.xMove,self.yMove)
		return (self.xMove, self.yMove)
