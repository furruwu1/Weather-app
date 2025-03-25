import os
from .main_frame import app
import customtkinter as ctk
import PIL.Image as pil
from ..json_functions import read_json


class WeatherImage(ctk.CTkLabel):
    def __init__(self, child_master: object, name_json: str, image_size: tuple):
        self.SIZE = image_size
        self.name_json = name_json
        ctk.CTkLabel.__init__(
            self,
            master=child_master,
            image=self.load_image()
        )

    def load_image(self):
        icon_id = read_json("current_city.json")["weather"][0]["icon"]
        image_path = os.path.abspath(__file__ + f"../../../images/{icon_id}.png")

        my_image = ctk.CTkImage(light_image=pil.open(image_path),
                                size=self.SIZE
                                )
        return my_image

current_weather_image = WeatherImage(child_master=app, name_json="current_city.json", image_size=(170, 160))
current_weather_image.place(x=380, y=169)
