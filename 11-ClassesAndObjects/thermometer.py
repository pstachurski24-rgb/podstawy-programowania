import random

class Thermometer:
    def __init__(self):
        self.is_on = False
        self.temperature = None

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def measure(self):
        if not self.is_on:
            print('Thermometer is off')
            return
        self.temperature = random.randint(340, 420) / 10

    def show_temperature(self):
        if self.temperature is None:
            print('No measurement available')
            return
        text = f'Temperature: {self.temperature:.1f}C'
        if self.temperature >= 37:
            text += ' (fever)'
        print(text)
        if self.temperature >= 41:
            print('CRITICAL TEMPERATURE!!')
