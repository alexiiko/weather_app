import requests
import pygame as pg
from settings import *
from api_key import api_key
from input_box import *

class InformationGetter:
    def __init__(self) -> None:
        pg.font.init()
        self.button_img = pg.image.load("button.png")
        self.button_rect = self.button_img.get_rect(center=(120, 130))

        self.clicked = False
        self.show_weather_info = False
        self.weather_data = None
        self.error_message = None

        self.font = pg.font.Font(None, 32)
        self.city_name = ""

    def get_city(self):
        self.city_name = input_box.return_text()
        return self.city_name

    def get_information(self, city) -> str:
        api_url = 'https://api.api-ninjas.com/v1/weather?city={}'.format(city)
        response = requests.get(api_url, headers={'X-Api-Key': f'{api_key}'})

        if response.status_code == requests.codes.ok:
            return response.json()
        else:
            self.error_message = f"Error: {response.status_code}"
            self.response_text = response.text
            return None

    def show_information(self, weather_data):
        if weather_data:
            temperature = str(weather_data['temp'])
            feels_like = str(weather_data['feels_like'])
            min_temperature = str(weather_data['min_temp'])
            max_temperature = str(weather_data['max_temp'])

            temperature_text = f"Temperature: {temperature}°C"
            feels_like_text = f"Feels like: {feels_like}°C"
            min_temperature_text = f"Minimal temperature: {min_temperature}°C"
            max_temperature_text = f"Maximal temperature: {max_temperature}°C"

            temperature_surf = self.font.render(temperature_text, True, "white")
            feels_like_surf = self.font.render(feels_like_text, True, "white")
            min_temperature_surf = self.font.render(min_temperature_text, True, "white")
            max_temperature_surf = self.font.render(max_temperature_text, True, "white")

            SCREEN.blit(temperature_surf, (300, 10))
            SCREEN.blit(feels_like_surf, (300, 60))
            SCREEN.blit(min_temperature_surf, (300, 110))
            SCREEN.blit(max_temperature_surf, (300, 160))

    def show_error_message(self):
        if self.error_message:
            error_text_surf = self.font.render(self.error_message, True, "white")
            response_text = self.font.render("An error occcured.", True, "white")
            again_text = self.font.render("Try with an another city.", True, "white")
            SCREEN.blit(error_text_surf, (300, 10))
            SCREEN.blit(response_text, (300, 60))
            SCREEN.blit(again_text, (300, 110))

    def check_for_click(self):
        x, y = pg.mouse.get_pos()
        if self.button_rect.collidepoint(x, y):
            if pg.mouse.get_pressed()[0] and not self.clicked:
                self.clicked = True
                city_name = self.get_city()
                if city_name:
                    self.weather_data = self.get_information(city_name)
                    self.show_weather_info = True 

        self.reset_click()

    def reset_click(self):
        if not pg.mouse.get_pressed()[0]:
            self.clicked = False

    def draw_self(self):
        SCREEN.blit(self.button_img, self.button_rect)

    def update(self):
        self.check_for_click()
        self.draw_self()

        if self.show_weather_info:
            if self.weather_data:
                self.show_information(self.weather_data)
            else:
                self.show_error_message()

information_getter = InformationGetter()