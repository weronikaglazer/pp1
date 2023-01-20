import random
class Thermometer():
    def __init__(self):
        self.temperature = 0
        self.is_on = False

    def check_temperature(self):
        if self.is_on:
            self.temperature = round(random.uniform(34.0,42.0),1)
            print("The temperature is " + str(self.temperature) + "C")
            if (37.0 <= self.temperature < 41.0):
                print("Fever")
            elif (self.temperature >= 41.0):
                print("Fever")
                print("CRITICAL TEMPERATURE!!")
        else:
            print("Turn on the thermometer first.")
        
    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False