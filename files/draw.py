import pygame
from datetime import date, datetime

########## LOCAL MODULES ##########
from files.vars import Scene
import files.bucle as b
import files.import_imp
from files.fonts import *
from files.UI.Text import Text
import files.calendar.calendar_engine as c

def update_current_date():
	global cur_year, cur_month, cur_day
	current_date = date.today()

	# Keep updating current dates
	cur_year = int(current_date.strftime("%Y"))
	cur_month = int(current_date.strftime("%m"))
	cur_day = int(current_date.strftime("%d"))

update_current_date()

# Month/Year where the user is
calendar_year = cur_year
calendar_month = cur_month

calendar_1 = c.Calendar(year=cur_year, month=cur_month, day=cur_day)

def Draw(events):
	global calendar_year, calendar_month, calendar_day
	
	update_current_date()

	calendar_1.set_UI_date("Month", value=calendar_month, init=True)
	calendar_1.set_UI_date("Year", value=calendar_year, init=True)
	
	calendar_1.update(events)

	# Draw time
	time = datetime.now()
	time_string = Text(0, 640, time.strftime("%H:%M:%S"), Arial_40, (255,255,255), lock="x")
	time_string.draw()


	for event in events:

		if event.type == KEYDOWN:
			if event.key == K_RIGHT:
				if calendar_month == 12:
					calendar_year += 1
					calendar_month = 1

				else:
					calendar_month += 1				
					
			elif event.key == K_LEFT:
				if calendar_month == 1:
					calendar_year -= 1
					calendar_month = 12

				else:
					calendar_month -= 1

			