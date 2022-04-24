import pygame
from pygame.locals import *


def square_border_line(win, x, y, width, height, color, width_line):

    a = True

    if a == True:
        red = (255,0,0)
        skyble = (0,255,0)
        blue = (0,0,255)
        green = (0,0,255)
    else:
        red = (0,0,0)
        skyble = (0,0,0)
        blue = (0,0,0)
        green = (0,0,0)

    initial_points = (x,y)

    width = x + width
    height = y + height

    # Corrections for corners
    width_line_correction = width_line

    # Horizontals
    pygame.draw.line(win, red, (x- (width_line), y), (width + (width_line/2), y ), width_line)
    pygame.draw.line(win, green, (x, height), (width, height), width_line)

    # Verticals
    pygame.draw.line(win, blue, (x , y), (x , height), width_line)
    pygame.draw.line(win, skyble, (width, y), (width , height), width_line)