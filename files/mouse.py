import pygame

from files.vars import mouse_hitbox

# pygame.mouse.get_pos()

class Mouse:
	def __init__(self):
		self.mouse_button = pygame.mouse.get_pressed()

	def mouse_update(self):
		global mouse_hitbox
		# Update Mouse's hitbox
		mouse_hitbox.left, mouse_hitbox.top = pygame.mouse.get_pos()

		# Update mouse button
		self.mouse_button = pygame.mouse.get_pressed()

	def mouse_press_action(self, index, action, args=None):
		if self.mouse_button[index] == 1: # Is being pressed
			if args != None:
				action(*args)
			else:
				action()

	def mouse_press_while_colliderecting(self, index, rect_to_colli, action, args=None):
		if mouse_hitbox.colliderect(rect_to_colli):
			self.mouse_press_action(index, action, args)