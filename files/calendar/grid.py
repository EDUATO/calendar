import pygame
from pygame.locals import *

from files.vars import *
import files.bucle as b

class Grid:
    def __init__(
                self, box_size, color, width_line, 
                squareNumber=None, # squareNumber, can be None or a tuple with the amount of cells for y and x. Each cell will have the size of box_size
                _manualGRIDSIZE=[[0, b.modeX], [0, b.modeY]],  # If squareNumber is false, you can add the columns and rows manually.
                ):

        self.box_size = box_size
        self.color = color
        self.width_line = width_line
        self.squareNumber = squareNumber

        if squareNumber == None:
            self.X_GRIDSIZE = _manualGRIDSIZE[0] # 0:Coords, 1:Width
            self.Y_GRIDSIZE = _manualGRIDSIZE[1]

        else:
            self.X_GRIDSIZE = [0, box_size[0] * self.squareNumber[0]]
            self.Y_GRIDSIZE = [0 , box_size[1] * self.squareNumber[1]]

        self.gridPositions = {}

        self.colliderecting = ()

    def update(self):
        self.colliderecting = None
        for y in range( int(self.Y_GRIDSIZE[1] // self.box_size[1] )):

            for x in range( int(self.X_GRIDSIZE[1] //  self.box_size[0] ) ):
                
                self.position = (
                    self.X_GRIDSIZE[0] + (self.box_size[0]*(x)),
                    self.Y_GRIDSIZE[0] + (self.box_size[1]*(y)),
                    self.box_size[0],
                    self.box_size[1]
                   )

                self.square(x=self.position[0], y=self.position[1], width=self.position[2], height=self.position[3],
                color=self.color, width_line=self.width_line)

                self.gridPositions[(x, y)] = {"Pos":self.position} # Give the x0, y0, width and height

                # Detect collition
                if self.colliderecting == None:
                    if b.mouse_hitbox.colliderect(self.position):
                        self.colliderecting = (x, y)


    def square(self, x, y, width, height, color, width_line, correction=True):

        self.initial_points = (x,y)

        self.width = x + width
        self.height = y + height

        # Corrections for corners
        if correction:
            self.width_line_correction = (width_line-1)/2
        else:
            self.width_line_correction = 0

        # Horizontals
        pygame.draw.line(win, color, (x , y), (self.width, y), width_line)
        pygame.draw.line(win, color, (x - self.width_line_correction, self.height - self.width_line_correction), (self.width + self.width_line_correction, self.height - self.width_line_correction), width_line)

        # Verticals
        pygame.draw.line(win, color, (x, y - self.width_line_correction), (x, self.height), width_line)
        pygame.draw.line(win, color, (self.width, y - self.width_line_correction), (self.width, self.height), width_line)

    def get_hitbox(self):
        return [self.X_GRIDSIZE[0], self.X_GRIDSIZE[1], self.Y_GRIDSIZE[0], self.Y_GRIDSIZE[1]]

    def set_place(self, x, y):
        self.X_GRIDSIZE[0] = x
        self.Y_GRIDSIZE[0] = y

    def get_square_position_in(self, id):
        # For example you want to get the id (0, 1), so you will get where is the position of that square and its size
        try:
            return self.gridPositions[id]["Pos"]
        except:
            return (0,0)

    def is_colliderecting_box(self):
        return self.colliderecting