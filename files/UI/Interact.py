import pygame
from pygame.locals import *

import files.loop as b
import files.functions as f
from files.vars import win
from files.UI.square_border_line import *

class Interact:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.times_pressed = 0
		self.square_border_line = False
	
	def rect(self, dimentions, color, lock=None, square_border_line=False, border_width=2):

		self.square_border_line = square_border_line
		self.dimentions = dimentions
		self.lock = lock
		self.Lock_formula = 0
		self.border_width = border_width

		if lock == None:
			self.hitbox = pygame.Rect(self.x, self.y, dimentions[0], dimentions[1]) # Set hitbox
		else:
			self.Lock_formula = f.Lock_to(lock, self.x, self.y, width=dimentions[0], height=dimentions[1])

			self.hitbox = pygame.Rect(self.Lock_formula[0] + self.x,self.Lock_formula[1] + self.y, dimentions[0], dimentions[1]) # Set hitbox

		if color == None:
			self.color = (255,0,255)
		else:
			self.color = color
		

	def button(self, events, width, height, color, Action, 
			args=None, glow_c=None, lock=None):

		self.rect(width, height, color, lock=lock)

		self.__buttonColliderect__(events, self.hitbox, Action, args, glow_c)

	def draw(self, win):
		pygame.draw.rect(win, self.color, self.hitbox) # Draw the rect
		
		if self.square_border_line:
			square_border_line(
				win=win, x=self.x + self.Lock_formula[0], y=self.y + self.Lock_formula[1], width=self.dimentions[0], height=self.dimentions[1],
				color=(0,0,0), width_line=self.border_width
				)


	def __buttonColliderect__(self, events, hitbox, action, args, glow_c):
		if not (b.g_isInSign == True):  
			if b.mouse_hitbox.colliderect(hitbox): # Comprove if the cursor is touching the hitbox
				if not sprites == None:
					win.blit(sprites[1], (self.xy))

				if not glow_c == None:
					self.color = glow_c

				
				for b.event in events:  
					

					if b.event.type == pygame.MOUSEBUTTONDOWN:
						
						if b.event.button==1:
							self.times_pressed += 1
							if not action == None:
								if args == None:
									action() # Defined as a parameter
								else:
									action(*args) # Defined as a parameter


	def addToCoords(self, x=0, y=0):
		self.x += x
		self.y += y

		return self.x, self.y

	def getHitbox(self):
		return self.hitbox

	def getTimesPressed(self):
		return self.times_pressed

	def getLockFormula(self):
		return self.Lock_formula