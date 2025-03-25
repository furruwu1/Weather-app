#Імпортуємо бібліотеку Requests для створення запитів=
import requests
import json
from ..json_functions import write_json
from ..json_functions import read_json

data_api = read_json(file_name="config_api.json")

API_KEY = data_api['API_KEY']

def request_city_data(CITY_NAME, index):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY_NAME}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    # 200, 201
    # 404, 403

    if response.status_code == 200:
        data_dict = json.loads(response.content)
        #print(data_dict)
        write_json("config_weather", data_dict)
        if index == 0:
            write_json("current_city.json", data_dict)
    else:
        print(f"Error, {response.status_code}")
