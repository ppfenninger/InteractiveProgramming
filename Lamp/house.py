import os, sys
import pygame
from pygame.locals import *
import LampMain

class House(pygame.sprite.Sprite):

	def __init__(self, centerPoint, name):
		pygame.sprite.Sprite.__init__(self)
		self.houseLocation = os.path.join('images', name)
		self.image = pygame.image.load(self.houseLocation)
		self.image = pygame.transform.scale(self.image, (100, 40))
		self.rect = self.image.get_rect()
		self.rect.center = centerPoint