import pygame
from datetime import date, datetime

########## LOCAL MODULES ##########
from files.vars import Scene
import files.bucle as b
import files.import_imp
from files.fonts import *
from files.UI.Text import Text
import files.calendar.calendar_engine as c

def update_current_day():
	global current_date, cur_year, cur_month, cur_day, calendar_1, calendar_year, calendar_month, calendar_day
	current_date = date.today()

	# Keep updating current dates
	cur_year = int(current_date.strftime("%Y"))
	cur_month = int(current_date.strftime("%m"))
	cur_day = int(current_date.strftime("%d"))

update_current_day()

calendar_year = cur_year
calendar_month = cur_month
calendar_day = cur_day

calendar_1 = c.Calendar(year=calendar_year, month=calendar_month, day=calendar_day)

def Draw(events):
	global calendar_year, calendar_month, calendar_day, calendar_1, cur_day, cur_month, cur_year, current_date
	
	update_current_day()

	calendar_1.set_day(calendar_day, init=True)
	calendar_1.set_month(calendar_month, init=True)
	calendar_1.set_year(calendar_year, init=True)
	
	calendar_1.update(events)

	# Show time
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

	# See if the day/month/year has changed
	calendar_day = 0
	if int(calendar_month) == int(cur_month):
		if int(calendar_year) == int(cur_year):
			calendar_day = cur_day

	calendar_1.set_day(calendar_day, init=True)
	calendar_1.set_month(calendar_month, init=True)
	calendar_1.set_year(calendar_year, init=True)

			