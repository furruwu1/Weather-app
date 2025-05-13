import customtkinter as ctk
from .main_frame import app
from ..json_functions import read_json
from ..api_requests import request_city_data
from datetime import datetime, timezone, timedelta
import time

CITIES_NAMES = read_json("config_app.json")["left_panel_frame"]

left_bg_colour = read_json("config_app.json")["left_panel_frame"]["left_bg_colour"]
left_city_colour = read_json("config_app.json")["left_panel_frame"]["left_city_colour"]
left_selected_colour = read_json("config_app.json")["left_panel_frame"]["left_selected_colour"]
text_colour = read_json("config_app.json")["main_frame"]["text_colour"]

scrollabel_frame = ctk.CTkScrollableFrame(master=app, height=700, width=275, fg_color=left_bg_colour)
scrollabel_frame.pack(side="left")

class City_frame(ctk.CTkFrame):
    def __init__(self, index, fg_color):
        ctk.CTkFrame.__init__(
            self,
            master=scrollabel_frame,
            width=260,
            height=100,
            fg_color=fg_color,
            border_width=2,
            border_color="#FFFFFF",
            corner_radius=16
        )
        self.pack(pady=15)
        self.city_index = index
        self.request_api()
        self.data_weather = read_json("config_weather")
        self.current_time = datetime.now(timezone(timedelta(seconds=self.data_weather["timezone"])))
        self.current_time = self.current_time.strftime("%H:%M")
        if self.city_index != 0:
            self.CITY_NAME = ctk.CTkLabel(
                master=self,
                text_color=text_colour,
                text=CITIES_NAMES["cities"][self.city_index],
                font=("Roboto Slab", 16, "bold")
            )
            self.CITY_NAME.place(x=14, y=7)
            self.TIME = ctk.CTkLabel(
                master=self,
                text_color=text_colour,
                text=self.current_time,
                font=("Roboto Slab", 12, "bold")
            )
            self.TIME.place(x=14, y=28)
        else:
            self.CURRENT_POSITION = ctk.CTkLabel(
                master=self,
                text_color=text_colour,
                text="Current position",
                font=("Roboto Slab", 16, "bold")
            )
            self.CURRENT_POSITION.place(x=14, y=7)
            self.CITY_NAME = ctk.CTkLabel(
                master=self,
                text_color=text_colour,
                text=CITIES_NAMES["cities"][self.city_index],
                font=("Roboto Slab", 12, "bold")
            )
            self.CITY_NAME.place(x=14, y=28)
        self.TEMPERATURE = ctk.CTkLabel(
            master=self,
            text_color=text_colour,
            text=str(round(self.data_weather["main"]["temp"])) + "°",
            font=("Inter", 50, "bold")
        )
        self.TEMPERATURE.place(x=180, y=7)
        self.WEATHER = ctk.CTkLabel(
            master=self,
            text_color=text_colour,
            text=self.data_weather["weather"][0]["description"].capitalize(),
            font=("Roboto Slab", 12, "bold")
        )
        self.WEATHER.place(x=14, y=65)
        self.MIN_MAX = ctk.CTkLabel(
            master=self,
            text_color=text_colour,
            text="max. " + str(round(self.data_weather["main"]["temp_max"])) + "° " + "min. " + str(round(self.data_weather["main"]["temp_min"])) + "°",
            font=("Roboto Slab", 12, "bold")
        )
        self.MIN_MAX.place(x=160, y=65)
        self.TIME = ctk.CTkLabel(
            master=self,
            text_color=text_colour,
            text="123"
        )
        #print("$", self.data_weather)


    def request_api(self):
        request_city_data(CITIES_NAMES["cities"][self.city_index], self.city_index)


for i in range(len(CITIES_NAMES["cities"])):
    if i != 0:
        city_frame = City_frame(index=i, fg_color=left_city_colour)
    else:
        city_frame = City_frame(index=i, fg_color=left_selected_colour)
