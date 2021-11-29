import pygame
import json

########## LOCAL MODULES ##########
from files.vars import win, modeX, modeY

def Lock_to(lock, x, y, width, height, screen_areas=(0, 0, modeX, modeY)):

	if lock == "x":
		return ( x + screen_areas[2]/2 - width/2 , y)

	elif lock == "y":
		return (x, y + screen_areas[3]/2 - height/2 )

	elif lock == "xy":
		return (x + screen_areas[2]/2 - width/2, y + screen_areas[3]/2 - height/2 )

	return 0

def jsontxt_to_list(jsonFile):
	# Read the file from json

	jsonstr = ""
	for i in range(len(jsonFile)):
		jsonstr += jsonFile[i].replace("\n", "")

	List = json.loads(jsonstr)

	return List