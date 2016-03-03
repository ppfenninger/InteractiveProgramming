import os, sys
import pygame
from pygame.locals import *

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
		#sets the number of pixels we are going to move each time
		self.xDist = 3
		self.yDist = 30
		#initializes how much we are moving
		self.xMove = 0
		self.yMove = 0

	def MoveKeyDown(self, key):
		if (key == K_RIGHT):
			self.xMove += self.xDist
		elif (key == K_LEFT):
			self.xMove += -self.xDist
		elif (key == K_UP):
			self.yMove += -self.yDist
		elif (key == K_DOWN):
			self.yMove += self.yDist

	def MoveKeyUp(self, key):
		if (key == K_RIGHT):
			self.xMove += -self.xDist
		elif (key == K_LEFT):
			self.xMove += self.xDist
		elif (key == K_UP):
			self.yMove += self.yDist
		elif (key == K_DOWN):
			self.yMove += -self.yDist

	def update(self):
		self.rect.move_ip(self.xMove,self.yMove)