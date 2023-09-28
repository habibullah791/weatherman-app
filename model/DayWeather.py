class DayWeatherData:
    def __init__(
        self,
        PKT,
        Max_TemperatureC,
        Mean_TemperatureC,
        Min_TemperatureC,
        Max_Humidity,   
        Mean_Humidity,
        Min_Humidity,
    ):
        self.PKT = PKT
        self.Max_TemperatureC = Max_TemperatureC
        self.Mean_TemperatureC = Mean_TemperatureC
        self.Min_TemperatureC = Min_TemperatureC
        self.Max_Humidity = Max_Humidity
        self.Mean_Humidity = Mean_Humidity
        self.Min_Humidity = Min_Humidity

    def get_PKT(self):
        return self.PKT

    def get_Max_TemperatureC(self):
        return self.Max_TemperatureC

    def get_Mean_TemperatureC(self):
        return self.Mean_TemperatureC

    def get_Min_TemperatureC(self):
        return self.Min_TemperatureC

    def get_Max_Humidity(self):
        return self.Max_Humidity

    def get_Mean_Humidity(self):
        return self.Mean_Humidity

    def get_Min_Humidity(self):
        return self.Min_Humidity