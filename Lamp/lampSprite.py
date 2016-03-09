import os, sys
import pygame
from pygame.locals import *
import LampMain
import time

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
		self.press = 0

		
	def MoveKeyDown(self):
		keys = pygame.key.get_pressed()
		if (keys[K_RIGHT]):
			self.xMove = self.xDist
		if (keys[K_LEFT]):
			self.xMove = -self.xDist
		if (keys[K_UP]):
			self.press += 1
			if self.press <= 6:
				self.yMove += -self.yDist
			else:
				self.yMove = 0
		if (keys[K_DOWN]):
			self.yMove = self.yDist

	def MoveKeyUp(self, key):
		if (key == K_RIGHT):
			self.xMove = 0
		if (key == K_LEFT):
			self.xMove = 0
		if (key == K_UP):
			self.yMove = 0
			self.press = 0
		if (key == K_DOWN):
			self.yMove = 0

	def update(self, other, platformGroup, width, height):
	
		if pygame.sprite.spritecollide(self, platformGroup, False):
			self.rect.move_ip(self.xMove, -self.yMove)
			self.yMove = 0
		else:
			if self.yMove == 0:
				self.yMove += 2
		# go off one edge, appear on the other
		x = self.rect.centerx
		if x > width:
			diff = x - width
			total = -(width + diff)
			self.rect.move_ip(total, 0)
		elif x < 0:
			diff = abs(x)
			total = width + diff
			self.rect.move_ip(total, 0)
		else:
			self.rect.move_ip(self.xMove,self.yMove)

		# if self.press:
		# 	self.yMove = 0
		# 	self.press = False
