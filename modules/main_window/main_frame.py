import customtkinter as ctk
from ..json_functions import read_json

def click():
    print("На мене натиснуто")

config = read_json(file_name="config_app.json")
WIDTH = config["main_frame"]["width"]
HEIGHT = config["main_frame"]["height"]
TITLE = config["main_frame"]["title"]
MAIN_BG_COLOUR = config["main_frame"]["background_colour"]
TITLE_BAR_HEIGHT = config["main_frame"]["title_bar_height"]

app = ctk.CTk(fg_color=MAIN_BG_COLOUR)
app.title(TITLE)

scale_factor = app._get_window_scaling()
X = int((int(app.winfo_screenwidth()) - int(WIDTH))/2*scale_factor)
Y = int((int(app.winfo_screenheight())/2 - (int(HEIGHT)+int(TITLE_BAR_HEIGHT))/2)*scale_factor)
app.geometry(f"{WIDTH}x{HEIGHT}+{X}+{Y}")

#first_button = ctk.CTkButton(app, text="Натисни на мене", command=click)
#first_button.place(x=200, y=200)
#first_button.grid(row=0,column=0)
#first_button.pack(pady=(0,20), padx=185)

#second_button = ctk.CTkButton(app, text="Натисни на мене", command=click)
#second_button.pack()

