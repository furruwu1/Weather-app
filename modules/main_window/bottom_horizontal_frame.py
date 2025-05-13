import customtkinter as ctk
from .bottom_frame import bottom_frame
from .weather_picture import WeatherImage
from ..json_functions import read_json

background_colour = read_json("config_app.json")["main_frame"]["background_colour"]
text_colour = read_json("config_app.json")["main_frame"]["text_colour"]

bottom_border = ctk.CTkCanvas(master=bottom_frame, height=1)
bottom_border.pack(fill="x", padx=20)

bottom_horizontal_frame = ctk.CTkScrollableFrame(master=bottom_frame, height=150, width=778, fg_color=background_colour, orientation="horizontal")
bottom_horizontal_frame.pack(anchor="sw", padx=5, pady=5)

forecast_data = read_json("forecast_data.json")
cur_weather_data = read_json("current_city.json")

forecast_amount = read_json("config_app.json")["bottom_horizontal_frame"]["forecast_amount"]

class Forecast_frame(ctk.CTkFrame):
    def __init__(self, fg_color, index):
        ctk.CTkFrame.__init__(
            self,
            master=bottom_horizontal_frame,
            width=55,
            height=150,
            fg_color=fg_color
        )
        if index == 0:
            self.time_label = ctk.CTkLabel(
                master=self,
                text_color=text_colour,
                text="Now",
                font=("Roboto Slab", 18, "bold")
            )
            self.icon_image = WeatherImage(
                child_master=self,
                name_json="forecast_data.json",
                image_size=(50, 50)
            )
            self.temp_label = ctk.CTkLabel(
                master=self,
                text_color=text_colour,
                text=str(round(cur_weather_data["main"]["temp"])) + "°",
                font=("Inter", 30, "bold")
            )
        else:
            self.time_label = ctk.CTkLabel(
                master=self,
                text_color=text_colour,
                text=forecast_data["list"][index]["dt_txt"][11:16],
                font=("Roboto Slab", 18, "bold")
            )
            self.icon_image = WeatherImage(
                child_master=self,
                name_json="forecast_data.json",
                image_size=(50, 50),
                count=index
            )
            self.temp_label = ctk.CTkLabel(
                master=self,
                text_color=text_colour,
                text=str(round(forecast_data["list"][index]["main"]["temp"])) + "°",
                font=("Inter", 30, "bold")
            )

        self.time_label.pack()
        self.icon_image.pack(pady=16)
        self.temp_label.pack()
        self.pack_propagate(False)


for i in range(forecast_amount):
    forecast_frame = Forecast_frame(background_colour, i)
    forecast_frame.grid(row=0, column=i, padx=19)
