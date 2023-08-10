class Temp:
    def __init__(self, temperature=0, unit="C"):
        self.__temperature=temperature
        self.__unit=unit

    def getTemperature(self):
        return self.__temperature

    @property
    def Temperature(self):
        return self.temperature

    def setTemperature(self,value):
        self.__temperature=value
    @temperature.setter
    def temperature(self):
            self.__temperature

    def to_celsius(self):
        if self.__unit=="F"
            return (self.__temperature - )