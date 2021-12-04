import pygame
import calendar
import json

from files.calendar.grid import Grid
from files.calendar.labelGrid import LabelGrid
from files.vars import *
import files.bucle as b
from files.fonts import Arial_40, Arial_60
from files.UI.Text import Text
from files.functions import jsontxt_to_list

AlertNoJsonFile = True # Change it, eventually

class Calendar:
    def __init__(self, year, month, day):

        self.cal = calendar.Calendar()

        self.date = {} # The real date
        self.in_date = {} # The month/year the user is

        self.set_UI_date("Year", year)
        self.set_UI_date("Month", month)

        self.set_real_date("Year", year)
        self.set_real_date("Month", month)
        self.set_real_date("Day", day)

        self.days_labels = [ "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

        self.months_labels = ["January", "February", "March", "April", "May", "June", "July", "August", "Setember", "October", "November", "December"]

        self.short_days_labels = []
        for i in range(len(self.days_labels)):
            self.short_days_labels.append(self.days_labels[i][0:3])

        self.box_size = (90, 90)

        self.intialize_grid()

        self.events_data = {} # Here goes the days where there is an event
        self.loaded_events_data_id = []
        
    def update(self, events):

        self.grid_place = self.grid.get_hitbox()

        # Callendar white background
        pygame.draw.rect(win, (255,255,255), (self.grid_place[0], self.grid_place[2], self.grid_place[1], self.grid_place[3]))

        self.grid.update()

        # Update callendar data
        self.set_callendar_data()
        
        self.write_text_in_calendar(events)
    
    def intialize_grid(self):
        if self.date["Month"] ==  self.in_date["Month"] and self.date["Year"] ==  self.in_date["Year"]:
            self.yearText = f'- {self.date["Day"]} of {self.months_labels[int(self.date["Month"])-1]}, {self.date["Year"]} -'
        else:
            self.yearText = f'- {self.months_labels[int(self.in_date["Month"])-1]}, {self.in_date["Year"]} -'

        # Make the grid
        self.grid = LabelGrid(
            box_size=self.box_size, 
            color=(0,0,0), 
            width_line=3, 
            squareNumber=[7,6], 
            labels_data=[(40, "Regular", 7, (230,0,0), self.short_days_labels, Arial_40), (40, None, 0, (0, 0,230), [self.yearText], Arial_40)]
        )

        self.grid_place = self.grid.get_hitbox()

        self.grid.set_place(b.modeX/2 - self.grid_place[1]/2, b.modeY/2 - self.grid_place[3]/2)

    def write_text_in_calendar(self, events):
        self.isColliderecting = self.grid.is_colliderecting_box()
        
        
        for i in range(len(self.calendar_data)):
            # Read json files
            try:
                pass
                self.read_json_data(year=self.calendar_data[i]["Year"])
            except AttributeError:
                pass

            if not self.calendar_data[i]["Day"][0] == 0: # Write only the valid dates

                # Write dates
                Text(self.calendar_data[i]["Pos"][0], self.calendar_data[i]["Pos"][1], str(self.calendar_data[i]["Day"][0]), Arial_60, (0,0,0), "xy", screen_areas=(self.calendar_data[i]["Pos"][0], self.calendar_data[i]["Pos"][1], self.box_size[0], self.box_size[1])).draw()

                # Select Actual Day
                if self.calendar_data[i]["Day"][0] == self.date["Day"] and self.calendar_data[i]["Month"] == self.date["Month"] and self.calendar_data[i]["Year"] == self.date["Year"]:

                    self.grid.square( self.calendar_data[i]["Pos"][0],  self.calendar_data[i]["Pos"][1],  self.calendar_data[i]["Pos"][2], self.calendar_data[i]["Pos"][3], (255,0,0), 5)

                # Find events
                if bool(self.events_data): # If there's data
                    try:
                        for mon in range(len(self.events_data[self.in_date["Year"]][self.months_labels[self.in_date["Month"]-1]])):
                            
                            if self.events_data[self.in_date["Year"]][self.months_labels[self.in_date["Month"]-1]][mon]["Day"] == self.calendar_data[i]["Day"][0]:
                                self.grid.square( self.calendar_data[i]["Pos"][0],  self.calendar_data[i]["Pos"][1],  self.calendar_data[i]["Pos"][2], 
                                self.calendar_data[i]["Pos"][3], (102,0,204), 5)
                    except KeyError:
                        pass

                    
                # Day colliderecting with mouse 
                if self.isColliderecting != None:
                    # Rect
                    self.day_square_hitbox = pygame.Rect(self.calendar_data[i]["Pos"][0],  self.calendar_data[i]["Pos"][1],  self.calendar_data[i]["Pos"][2], 
                        self.calendar_data[i]["Pos"][3])

                    # Mouse colliderect
                    if b.mouse_hitbox.colliderect(self.day_square_hitbox):
                        self.grid.square( self.calendar_data[i]["Pos"][0],  self.calendar_data[i]["Pos"][1],  self.calendar_data[i]["Pos"][2], 
                        self.calendar_data[i]["Pos"][3], (255,255,0), 5) # Color when the mouse colliderects a day

                        # Detect mouse click
                        for event in events:
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if event.button == 1:
                                    # Add an event to the calendar
                                    self.add_new_event(day=self.calendar_data[i]["Day"][0], year=self.calendar_data[i]["Year"], monthID=self.calendar_data[i]["Month"], data="")

    def add_events_data(self, year, monthID):

        # MAKE THE EVENTS_DATA YEAR
        if not year in self.loaded_events_data_id:
            # Add an empty year dict to the events list
            self.events_data[year] = {}

            self.loaded_events_data_id.append(year) # Years loaded
        
        # Check if the month exist in the year's keys
        if not (self.months_labels[monthID-1] in self.events_data[year].keys()):
            self.events_data[year][self.months_labels[monthID-1]] = []
        
           
    def add_new_event(self, day, year, monthID, data):
        # Check if the year and month is in events_data 
        self.add_events_data(year, monthID)

        canAdd = True
        # Check if there is already an event in the date
        for i in range(len(self.events_data[year][self.months_labels[monthID-1]])):
            if self.events_data[year][self.months_labels[monthID-1]][i]["Day"] == int(day):
                canAdd = False
                break

        if canAdd:
            print(day)
            self.events_data[year][self.months_labels[monthID-1]].append({"Day" : int(day), "Data":data})
            print("Adding new event")
            self.save_json_data(year=year, event=self.events_data[year])

    def save_json_data(self, year, event):
        global AlertNoJsonFile
        # Save the data to a json file 
        try:
            # Try to open the file, if it can't, it creates a new one
            self.year_file = open(f"Years/.{year}.json", "w+")

            self.year_file.writelines(json.dumps(event, indent=4))

            print(f"The file {year}.json was saved.")

            AlertNoJsonFile = True # To print an alert if there is no json file

            self.year_file.close()
            if not year in self.loaded_events_data_id:
                self.loaded_events_data_id.append(year)
        except Exception:
            pass
        finally:
            self.year_file.close()


    def read_json_data(self, year):
        # Read the data from the json file and save it
        if not year in self.loaded_events_data_id:
            try:
                # Try reading the data
                self.year_file = open(f"Years/.{year}.json", "r")

                self.year_read_file = self.year_file.readlines()

                self.year_file.close()

                self.events_data[year] = jsontxt_to_list(self.year_read_file)

                self.loaded_events_data_id.append(year)

            except FileNotFoundError:
                global AlertNoJsonFile
                if AlertNoJsonFile:
                    print(f"It does not exist a file named {year}.json")
                    AlertNoJsonFile = False
            finally:
                self.year_file.close()


    def set_callendar_data(self):
        self.calendar_data = []

        for day in self.cal.itermonthdays2(self.in_date["Year"], self.in_date["Month"]):

            self.calendar_data.append({
                "Day":day, # (0 #date ,0 #Calendar order) 
                "Month":int(self.in_date["Month"]),
                "Year":int(self.in_date["Year"]),
                "Pos":None}) # Position in grid

        # Set position in callendar collumns (y)
        self.y_position = -1
        for i in range(len(self.calendar_data)):
            if self.calendar_data[i]["Day"][1] == 0:
                self.y_position += 1

            # Get grid position and append it in the callendar data
            self.grid_pos = self.grid.get_square_position_in((self.calendar_data[i]["Day"][1], self.y_position))
            self.calendar_data[i]["Pos"] = self.grid_pos

    def open_data_UI(self):
        print("Opened")

    # Real date setter
    def set_real_date(self, id, value, init=False):
        self.date[id] = value
        
        if init:
            self.intialize_grid()

    # Setter of the month/year the user is
    def set_UI_date(self, id, value, init=False):
        self.in_date[id] = value
        
        if init:
            self.intialize_grid()