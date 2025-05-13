from .main_frame import app
from ..json_functions import read_json
import customtkinter as ctk
import time
import datetime

CURRENT_CITY = read_json("current_city.json")

background_colour = read_json("config_app.json")["main_frame"]["background_colour"]
text_colour = read_json("config_app.json")["main_frame"]["text_colour"]

bottom_frame = ctk.CTkFrame(master=app, width=800, height=240, fg_color=background_colour, border_width=5, border_color="#FFFFFF", corner_radius=20)
bottom_frame.place(x=350, y=400)
bottom_frame.pack_propagate(False)

current_time = time.time()
if current_time < CURRENT_CITY["sys"]["sunrise"]:
    sunrise_sunset = datetime.timedelta(seconds=CURRENT_CITY["sys"]["sunrise"]+3600)
    sunrise_sunset = str(sunrise_sunset)[11:17]
    sunrise_sunset = "Sunrise will be at" + sunrise_sunset
elif current_time < CURRENT_CITY["sys"]["sunset"] and current_time >= CURRENT_CITY["sys"]["sunrise"]:
    #sunrise_sunset = CURRENT_CITY["sys"]["sunset"].strftime("%H:%M")
    sunrise_sunset = datetime.timedelta(seconds=CURRENT_CITY["sys"]["sunset"]+3600)
    sunrise_sunset = str(sunrise_sunset)[11:17]
    sunrise_sunset = "Sunset will be at" + sunrise_sunset
elif current_time >= CURRENT_CITY["sys"]["sunset"]:
    sunrise_sunset = datetime.timedelta(seconds=CURRENT_CITY["sys"]["sunset"]+3600)
    sunrise_sunset = str(sunrise_sunset)[11:17]
    sunrise_sunset = "Sunset was at" + sunrise_sunset
else:
    sunrise_sunset = "No data"
sunrise_sunset_label = ctk.CTkLabel(master=bottom_frame, text_color=text_colour, text=sunrise_sunset, font=("Roboto Slab", 14, "bold"))
sunrise_sunset_label.pack(anchor="nw", padx=20, pady=7)
