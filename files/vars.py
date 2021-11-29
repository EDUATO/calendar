import pygame
import pygame.locals

Version = ""

Playing = True

########### WINDOW ###########
modeX = 1080
modeY = 720

flags = None

win = pygame.display.set_mode( (modeX,modeY) )

pygame.display.set_caption("Calendar") # Win's name

fps = pygame.time.Clock()

Frames_per_second = 60

# Mouse hitbox
mouse_hitbox = pygame.Rect((0,0), (1,1))

########## SCENE ############
Scene = 0

######### ANIMATION #########


