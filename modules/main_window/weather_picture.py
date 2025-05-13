import os
from .main_frame import app
import customtkinter as ctk
import PIL.Image as pil
from ..json_functions import read_json

class WeatherImage(ctk.CTkLabel):
    def __init__(self, child_master: object, name_json: str, image_size: tuple, count=0):
        self.SIZE = image_size
        self.name_json = name_json
        self.count = count
        ctk.CTkLabel.__init__(
            self,
            master=child_master,
            text="",
            image=self.load_image()
        )

    def load_image(self):
        if self.name_json == "arrow_down.png":
            image_path = os.path.abspath(__file__ + "../../../../images/arrow_down.png")
        elif self.name_json == "arrow_up.png":
            image_path = os.path.abspath(__file__ + "../../../../images/arrow_up.png")
        elif self.name_json == "forecast_data.json":
            icon_id = read_json(self.name_json)["list"][self.count]["weather"][0]["icon"]
            image_path = os.path.abspath(__file__ + f"../../../../images/{icon_id}.png")
        else:
            icon_id = read_json(self.name_json)["weather"][0]["icon"]
            image_path = os.path.abspath(__file__ + f"../../../../images/{icon_id}.png")

        my_image = ctk.CTkImage(light_image=pil.open(image_path),
                                size=self.SIZE
                                )
        return my_image

current_weather_image = WeatherImage(child_master=app, name_json="current_city.json", image_size=(170, 160))
current_weather_image.place(x=380, y=169)
