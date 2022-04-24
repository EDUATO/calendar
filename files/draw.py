import pygame
from datetime import date, datetime

########## LOCAL MODULES ##########
from files.vars import Scene, win
import files.loop as b
import files.import_imp
from files.fonts import *
from files.UI.Text import Text
import files.calendar.calendar_engine as c
from files.UI.messagebox import Messagebox, messagebox_updater, add_to_message_boxes, remove_from_message_boxes

def update_current_date():
	global cur_year, cur_month, cur_day
	current_date = date.today()

	# Keep updating current dates
	cur_year = int(current_date.strftime("%Y"))
	cur_month = int(current_date.strftime("%m"))
	cur_day = int(current_date.strftime("%d"))

update_current_date()

calendar_1 = c.Calendar(year=cur_year, month=cur_month, day=cur_day)

#ID = add_to_message_boxes(Messagebox(x=0, y=0, lock_to="xy"))

def Draw(events):
	
	update_current_date()

	# Update the current date
	calendar_1.set_real_date("Month", value=cur_month)
	calendar_1.set_real_date("Year", value=cur_year)
	calendar_1.set_real_date("Day", value=cur_day)

	calendar_1.update(events)

	# Draw time
	time = datetime.now()
	time_string = Text(0, 640, time.strftime("%H:%M:%S"), Arial_40, (255,255,255), lock="x")
	time_string.draw()


	for event in events:

		if event.type == KEYDOWN:
			# Change the months using the arrows keys
			if event.key == K_RIGHT:
				if calendar_1.get_UI_date("Month") == 12:
					calendar_1.add_UI_date("Year", +1)
					calendar_1.set_UI_date("Month", 1)

				else:
					calendar_1.add_UI_date("Month", +1)			
					
			elif event.key == K_LEFT:
				if calendar_1.get_UI_date("Month") == 1:
					calendar_1.add_UI_date("Year", -1)
					calendar_1.set_UI_date("Month", 12)

				else:
					calendar_1.add_UI_date("Month", -1)

	# MESSAGE BOX - DRAW

	messagebox_updater(win=win,events=events, calendar=calendar_1)
			