import pygame
from pygame.locals import *

from files.vars import *
import files.loop as b
from files.UI.square_border_line import *

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

                square_border_line(win=win, x=self.position[0], y=self.position[1], width=self.position[2], height=self.position[3],
                color=self.color, width_line=self.width_line)

                self.gridPositions[(x, y)] = {"Pos":self.position} # Give the x0, y0, width and height

                # Detect collition
                if self.colliderecting == None:
                    if b.mouse_hitbox.colliderect(self.position):
                        self.colliderecting = (x, y)

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