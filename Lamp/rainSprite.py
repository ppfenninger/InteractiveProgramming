import os, sys
import pygame
from pygame.locals import *
import LampMain
import time
import random

class Rain(pygame.sprite.Sprite):

	def __init__(self, width=2,height=5,color=(0,0,255)):

		self.width = width
		self.height = height
		self.color = color

		# Call the Sprite constructor from pygame
		pygame.sprite.Sprite.__init__(self)

		# creates a rain block
		self.image = pygame.Surface([self.width, self.height])
		self.image.fill(self.color)

		# gets the rect
		self.rect = self.image.get_rect()
		self.rect.center = (random.randint(0,800), 5)

		self.yMove = 3
		self.xMove = 0

	def update(self):
		self.rect.move_ip(self.xMove,self.yMove)

class Hail(pygame.sprite.Sprite):
	def __init__(self, width=5,height=10,color=(255,255,255)):

		self.width = width
		self.height = height
		self.color = color

		# Call the Sprite constructor from pygame
		pygame.sprite.Sprite.__init__(self)

		# creates a rain block
		self.image = pygame.Surface([self.width, self.height])
		self.image.fill(self.color)

		# gets the rect
		self.rect = self.image.get_rect()
		self.rect.center = (random.randint(0,800), 5)

		self.yMove = 3
		self.xMove = 0

	def update(self):
		self.rect.move_ip(self.xMove,self.yMove)
