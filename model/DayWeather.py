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
        '''
        Initialize Weather Data Object

        @param PKT: Date and time of the weather data (str).
        @param Max_TemperatureC: Maximum temperature in degrees Celsius (float).
        @param Mean_TemperatureC: Mean temperature in degrees Celsius (float).
        @param Min_TemperatureC: Minimum temperature in degrees Celsius (float).
        @param Max_Humidity: Maximum relative humidity in percentage (float).
        @param Mean_Humidity: Mean relative humidity in percentage (float).
        @param Min_Humidity: Minimum relative humidity in percentage (float).

        @desc: This constructor initializes a WeatherData object with the provided weather data.

        @return: None.
        '''
        self.PKT = PKT
        self.Max_TemperatureC = Max_TemperatureC
        self.Mean_TemperatureC = Mean_TemperatureC
        self.Min_TemperatureC = Min_TemperatureC
        self.Max_Humidity = Max_Humidity
        self.Mean_Humidity = Mean_Humidity
        self.Min_Humidity = Min_Humidity

    def get_PKT(self):
        '''
            @desc: This method returns the date and time of the weather data.
            @return: Date and time of the weather data (str).
        '''
        return self.PKT

    def get_Max_TemperatureC(self):
        '''
            @desc: This method returns the maximum temperature in degrees Celsius.
            @return: Maximum temperature in degrees Celsius (float).
        '''
        return self.Max_TemperatureC

    def get_Mean_TemperatureC(self):
        '''
            @desc: This method returns the mean temperature in degrees Celsius.
            @return: Mean temperature in degrees Celsius (float).
        '''
        return self.Mean_TemperatureC

    def get_Min_TemperatureC(self):
        '''
            @desc: This method returns the minimum temperature in degrees Celsius.
            @return: Minimum temperature in degrees Celsius (float).
        '''
        return self.Min_TemperatureC

    def get_Max_Humidity(self):
        '''
            @desc: This method returns the maximum relative humidity in percentage.
            @return: Maximum relative humidity in percentage (float).
        '''
        return self.Max_Humidity

    def get_Mean_Humidity(self):
        '''
            @desc: This method returns the mean relative humidity in percentage.
            @return: Mean relative humidity in percentage (float).
        '''
        return self.Mean_Humidity

    def get_Min_Humidity(self):
        '''
            @desc: This method returns the minimum relative humidity in percentage.
            @return: Minimum relative humidity in percentage (float).
        '''
        return self.Min_Humidity
