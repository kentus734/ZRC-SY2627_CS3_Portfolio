
from abc import ABC, abstractmethod


# Abstract Base Class
class Sensor(ABC):

    @abstractmethod
    def get_reading(self):
        pass


# Child Class: pH Sensor
class PHSensor(Sensor):

    def get_reading(self):
        print("[pH Sensor] Reading: 7.2 pH (Neutral)")


# Child Class: Temperature Sensor
class TempSensor(Sensor):

    def get_reading(self):
        print("[Temperature Sensor] Reading: 24.5°C")

# Main Program
print("--- Lab Inventory System ---")

# Create sensor objects
ph_sensor = PHSensor()
temp_sensor = TempSensor()

# Display sensor readings
ph_sensor.get_reading()
temp_sensor.get_reading()

#my_sensor = Sensor()