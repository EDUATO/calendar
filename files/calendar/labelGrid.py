import pygame
from pygame.locals import *

from files.calendar.grid import Grid
from files.vars import *
import files.bucle as b
from files.UI.Text import Text
from files.fonts import Arial_60

class LabelGrid(Grid):
    def __init__(self, box_size, color, width_line, GRIDSIZE=[[0, b.modeX], [0, b.modeY]], squareNumber=None, labels_data=[(40,"Regular",5, (255,0,0), ["May", "June"], Arial_60)]):

        super().__init__(box_size, color, width_line, GRIDSIZE, squareNumber)

        self.labels_data = labels_data

    def update(self):

        super().update()
        self.height_amount = 0

        for i in range(len(self.labels_data)):
            self.position = (
                self.X_GRIDSIZE[0],
                self.Y_GRIDSIZE[0] - (self.labels_data[i][0] + self.height_amount),
                self.X_GRIDSIZE[1],
                self.labels_data[i][0]
            )


            # Color
            pygame.draw.rect(win, self.labels_data[i][3], (self.position[0], self.position[1], self.position[2], self.position[3]))
            # Shape
            super().square(self.position[0], self.position[1], self.position[2], self.position[3], self.color, self.width_line)
            self.height_amount += self.labels_data[i][0]

            if not self.labels_data[i][1] == None:
                # Check dividers
                if self.labels_data[i][1] == "Regular":

                    if self.labels_data[i][3] != 0:
                        self.chunks_sizes = self.position[2] / self.labels_data[i][2]
                        
                        for dividers in range(self.labels_data[i][2]):

                            pygame.draw.line(win, self.color, (self.position[0] + self.chunks_sizes * (dividers+1), self.position[1] + self.position[3]),
                            (self.position[0] + self.chunks_sizes * (dividers+1), self.position[1]), width=self.width_line)

                            try:
                                # Text
                                Text(self.position[0] + self.chunks_sizes * (dividers), self.position[1], self.labels_data[i][4][dividers], self.labels_data[i][5], (0,0,0), 
                                lock="xy", screen_areas=(self.position[0], self.position[1], self.chunks_sizes, self.labels_data[i][0])).draw()
                            except IndexError:
                                pass

                elif self.labels_data[i][1] == "Irregular":
                    # The tuple values are porcentages

                    self.chunks_sizes_tuple = self.labels_data[i][2]

                    for index in range(len(self.chunks_sizes_tuple)):

                        self.chunk_size = self.chunks_sizes_tuple[index] * self.position[2] / 100

                        pygame.draw.line(win, self.color, (self.position[0] + self.chunk_size, self.position[1] + self.position[3]),
                            (self.position[0] + self.chunk_size, self.position[1]), width=self.width_line)


                        if index == 0:
                            # Text
                            Text(self.position[0], self.position[1], self.labels_data[i][4][index], self.labels_data[i][5], (0,0,0)).draw()
                        else:
                            # Text
                            self.chunk_size = self.chunks_sizes_tuple[index-1] * self.position[2] / 100

                            Text(self.position[0] + self.chunk_size, self.position[1], self.labels_data[i][4][index], self.labels_data[i][5], (0,0,0)).draw()

            else:
                # Text
                Text(self.position[0], self.position[1], self.labels_data[i][4][0], self.labels_data[i][5], (0,0,0), lock="xy", screen_areas=self.position).draw()

