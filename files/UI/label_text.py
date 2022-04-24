import pygame
from pygame.locals import *

from files.UI.text_input.pygame_textinput import TextInput
from files.UI.Interact import Interact

class TextLabel:
    def __init__(self, x, y, lock_to):
        self.x = x
        self.y = y
        self.lock_to = lock_to

        # Background initialization
        self.background = Interact(x=self.x, y=self.y)
        self.background.rect(
            (100,200), (255,255,255), lock=self.lock_to, square_border_line=True,border_width=30
            )

        self.LockFormula = self.background.getLockFormula()

        # TextInput variables
        self.TextInput = TextInput(
            initial_string="", font_family="Arial",
            font_size=16
        )
        self.TextMargin = 10

    def _background(self, win):
        self.background.draw(win)

    def update(self, events, win):
        self.TextInput.update(events)

        self._background(win)
        win.blit(self.TextInput.get_surface(), (self.x + self.LockFormula[0] + self.TextMargin, self.y + self.LockFormula[1] + self.TextMargin))