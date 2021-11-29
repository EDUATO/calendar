import pygame
from pygame.locals import *

from files.vars import win, modeX, modeY
import files.functions as f

class Text:
	def __init__(self, x, y, txt, FUENTE, COLOR, lock=None, screen_areas=(0, 0, modeX, modeY)):

		self.x = x
		self.y = y
		
		self.Text = FUENTE.render(txt,1,(COLOR))

		self.w = self.Text.get_rect().width
		self.h = self.Text.get_rect().height
		self.Lock_formula = (0,0)

		if not lock == None:
			self.Lock_formula = f.Lock_to(lock,0,0, width=self.w, height=self.h, screen_areas=screen_areas )

	def draw(self):
		win.blit(self.Text,(self.Lock_formula[0] + self.x,self.Lock_formula[1] + self.y))

	def getHitbox(self):
		return pygame.Rect(self.Lock_formula[0] + self.x, self.Lock_formula[1] + self.y, self.w, self.h)

	def getWidth(self):
		return self.w

	def setCoords(self, x, y):
		self.x = x
		self.y = y