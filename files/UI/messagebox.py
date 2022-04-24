import pygame
from pygame.locals import *

from files.UI.Interact import Interact
from files.UI.label_text import TextLabel

running_message_boxes = {} # ID:MESSAGE_BOX
aveliable_ids = [n for n in range(100)]

class Messagebox:
    def __init__(
        self,
        x,
        y,
        lock_to = None # "x", "y" or "xy"
    ):

        self.x = x
        self.y = y
        self.lock_to = lock_to
        self.MINIMUM_BACKGROUND_SIZE = (350,250)

        # Background initialization
        self.background = Interact(x=self.x, y=self.y)
        self.background.rect(
            self.MINIMUM_BACKGROUND_SIZE, (255,255,255), lock=self.lock_to, square_border_line=True
            )

        self.T_LABEL = TextLabel(10, 20, self.lock_to)

    def __box_background(self, win):
        self.background.draw(win)

    def draw(self, win, events):
        #self.__box_background(win)
        self.T_LABEL.update(events, win)

# This function draws all the messageboxes
def messagebox_updater(win, events, calendar):
    for i in range(len(running_message_boxes)):
        running_message_boxes[i].draw(win, events)

    if running_message_boxes:
        calendar.set_UI_unlocked(False)
    else:
        calendar.set_UI_unlocked(True)

# Functions to add and remove message_box from running_message_boxes
def add_to_message_boxes(message_box):
    ID = aveliable_ids[0]
    running_message_boxes[ID] = message_box
    aveliable_ids.remove(ID)

    return ID

def remove_from_message_boxes(message_box_ID):
    running_message_boxes.pop(message_box_ID)
    aveliable_ids.append(message_box_ID)