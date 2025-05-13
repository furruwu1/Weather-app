import customtkinter as ctk
from .main_frame import app
from ..json_functions import read_json
from .weather_picture import WeatherImage

CURRENT_CITY = read_json("current_city.json")

background_colour = read_json("config_app.json")["main_frame"]["background_colour"]
text_colour = read_json("config_app.json")["main_frame"]["text_colour"]

current_center_frame = ctk.CTkFrame(master=app, width=315, height=275, fg_color=background_colour)
current_center_frame.place(x=576, y=100)

current_position_label = ctk.CTkLabel(master=current_center_frame, text_color=text_colour, text="Current position", font=("Roboto Slab", 35, "bold"))
current_position_label.pack()
current_city_label = ctk.CTkLabel(master=current_center_frame, text_color=text_colour, text=CURRENT_CITY["name"], font=("Roboto Slab", 22, "bold"))
current_city_label.pack()
current_temp_label = ctk.CTkLabel(master=current_center_frame, text_color=text_colour, text=str(round(CURRENT_CITY["main"]["temp"])) + "°", font=("Inter", 80))
current_temp_label.pack()

curr_weather = CURRENT_CITY["weather"][0]["description"]
current_weather_label = ctk.CTkLabel(master=current_center_frame, text_color=text_colour, text=curr_weather.capitalize().split(" ")[0], font=("Roboto Slab", 30, "bold"))
current_weather_label.pack()

weather_extra_text = curr_weather.split(" ")
weather_extra_text.pop(0)
weather_extra_label = ctk.CTkLabel(master=current_center_frame, text_color=text_colour, text=weather_extra_text, font=("Roboto Slab", 24, "bold"))
weather_extra_label.pack()

min_max_temp_frame = ctk.CTkFrame(master=current_center_frame, width=120, height=30, fg_color=background_colour)
min_max_temp_frame.pack()

arrow_down = WeatherImage(child_master=min_max_temp_frame, name_json="arrow_down.png", image_size=(18, 25))
arrow_down.grid(column=0, row=0)

min_temp_label = ctk.CTkLabel(master=min_max_temp_frame, text_color=text_colour, text=" " + str(round(CURRENT_CITY["main"]["temp_min"])) + "°  ", font=("Inter", 30, "bold"))
min_temp_label.grid(column=1, row=0)

arrow_up = WeatherImage(child_master=min_max_temp_frame, name_json="arrow_up.png", image_size=(18, 25))
arrow_up.grid(column=2, row=0)

max_temp_label = ctk.CTkLabel(master=min_max_temp_frame, text_color=text_colour, text=" " + str(round(CURRENT_CITY["main"]["temp_max"])) + "°  ", font=("Inter", 30, "bold"))
max_temp_label.grid(column=3, row=0)
