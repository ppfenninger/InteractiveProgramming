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

		# a list of the keys that are currently down
		# 1, 2, 3, 4 represent right left up down respectively
		self.keyDown = []

	def MoveKeyDown(self, key):
		if self.keyDown == []:
			if (key == K_RIGHT):
				self.xMove += self.xDist
				self.keyDown.append(1)
			elif (key == K_LEFT):
				self.xMove += -self.xDist
				self.keyDown.append(2)
			elif (key == K_UP):
				self.yMove += -self.yDist
				self.keyDown.append(3)
			elif (key == K_DOWN):
				self.yMove += self.yDist
				self.keyDown.append(4)

	def MoveKeyUp(self, key):
		if self.keyDown != []:
			if (key == K_RIGHT) and self.keyDown[0] == 1:
				self.xMove += -self.xDist
				self.keyDown.pop()
			elif (key == K_LEFT) and self.keyDown[0] == 2:
				self.xMove += self.xDist
				self.keyDown.pop()
			elif (key == K_UP) and self.keyDown[0] == 3:
				self.yMove += self.yDist
				self.keyDown.pop()
			elif (key == K_DOWN) and self.keyDown[0] == 4:
				self.yMove += -self.yDist
				self.keyDown.pop()

	def update(self, platformGroup, width, height):


		if pygame.sprite.spritecollide(self, platformGroup, False):
			self.rect.move_ip(self.xMove, -3*self.yMove)

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
		return (self.xMove, self.yMove)
