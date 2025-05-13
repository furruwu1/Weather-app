import time
import customtkinter as ctk
from .main_frame import app
from ..json_functions import read_json

background_colour = read_json("config_app.json")["main_frame"]["background_colour"]
text_colour = read_json("config_app.json")["main_frame"]["text_colour"]

right_frame = ctk.CTkFrame(master=app, width=146, height=130, fg_color=background_colour)
right_frame.place(x=940, y=190)

current_weekday = time.strftime("%A")
current_weekday_label = ctk.CTkLabel(master=right_frame, text_color=text_colour, text=current_weekday, font=("Roboto Slab", 18, "bold"))
current_weekday_label.pack()

current_date = time.strftime("%d.%m.%Y")
current_date_label = ctk.CTkLabel(master=right_frame, text_color=text_colour, text=current_date, font=("Roboto Slab", 35, "bold"))
current_date_label.pack()

current_time = time.strftime("%H:%M")
current_time_label = ctk.CTkLabel(master=right_frame, text_color=text_colour, text=current_time, font=("Roboto Slab", 30, "bold"))
current_time_label.pack()
