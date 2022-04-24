import pygame 
from pygame.locals import QUIT

########## LOCAL MODULES ##########
from files.vars import mouse_hitbox, fps, Frames_per_second, Playing, win, modeX, modeY
import files.draw as dr
from files.mouse import Mouse


def loop():
	global deltaTime, FPS, mouse_control

	mouse_control = Mouse()

	while Playing == True:
		
		events = pygame.event.get()

		# Update mouse's hitbox and pressed buttons
		mouse_control.mouse_update()

		# Frames per second
		FPS = fps.tick(Frames_per_second)

		#DeltaTime
		deltaTime = FPS/15

		Events(events)

		update(events)

def Events(events):
	global Playing, modeY, modeX

	modeX = modeX
	modeY = modeY

	for event in events:

		if event.type == QUIT:
			Playing = False

		
			
def update(events):
	win.fill((50,50,50))

	# Draw on screen
	dr.Draw(events)

	# Update each frame
	pygame.display.update()