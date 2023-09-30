from utils.Utils import Utils
from DB.FileHandler import FileHandler


file_handler = FileHandler()
utils = Utils()


class WeatherDataControler:
    def __init__(self) -> None:
        pass

    def getTemperatureHumidityStats(self, year, month):
        '''
            @param year: The year for which to retrieve statistics (int).
            @param month: The month for which to retrieve statistics (int).
            @desc: This method retrieves temperature and humidity statistics for a specific
                month and year and returns the data in JSON format.
            @return: JSON-formatted data containing temperature and humidity statistics.
        '''
        data = utils.cal_HighestLowestTemperatureHumidity(year, month)
        data = utils.convertToJSON(data)

        return data

    def getHighestTemperatureStats(self, year, month):
        '''
            @param year: The year for which to retrieve statistics (int).
            @param month: The month for which to retrieve statistics (int).
            @desc: This method retrieves the highest temperature statistics for a specific
                month and year and returns the data in JSON format.
            @return: JSON-formatted data containing highest temperature statistics.
        '''
        category = 'highestTemp'
        data = utils.cal_TemperatureStat(year, month, category)
        data = utils.convertToJSON(data)

        return data

    def getLowestTemperatureStats(self, year, month):
        '''
            @param year: The year for which to retrieve statistics (int).
            @param month: The month for which to retrieve statistics (int).
            @desc: This method retrieves the lowest temperature statistics for a specific
                month and year and returns the data in JSON format.
            @return: JSON-formatted data containing lowest temperature statistics.
        '''
        category = 'lowestTemp'
        data = utils.cal_TemperatureStat(year, month, category)
        data = utils.convertToJSON(data)

        return data

    def getMeanTemperatureStats(self, year, month):
        '''
            @param year: The year for which to retrieve statistics (int).
            @param month: The month for which to retrieve statistics (int).
            @desc: This method retrieves the mean temperature statistics for a specific
                month and year and returns the data in JSON format.
            @return: JSON-formatted data containing mean temperature statistics.
        '''
        category = 'meanTemp'
        data = utils.cal_TemperatureStat(year, month, category)
        data = utils.convertToJSON(data)

        return data
    
    
    def getHighestHumidityStats(self, year, month):
        '''
            @param year: The year for which to retrieve statistics (int).
            @param month: The month for which to retrieve statistics (int).
            @desc: This method retrieves the highest humidity statistics for a specific
                month and year and returns the data in JSON format.
            @return: JSON-formatted data containing highest humidity statistics.
        '''
        category = 'highestHumid'
        data = utils.cal_HumidStat(year, month, category)
        data = utils.convertToJSON(data)

        return data
    
    def getLowestHumidityStats(self, year, month):
        '''
            @param year: The year for which to retrieve statistics (int).
            @param month: The month for which to retrieve statistics (int).
            @desc: This method retrieves the lowest humidity statistics for a specific
                month and year and returns the data in JSON format.
            @return: JSON-formatted data containing lowest humidity statistics.
        '''
        category = 'lowestHumid'
        data = utils.cal_HumidStat(year, month, category)
        data = utils.convertToJSON(data)

        return data
    
    def getMeanHumidityStats(self, year, month):
        '''
            @param year: The year for which to retrieve statistics (int).
            @param month: The month for which to retrieve statistics (int).
            @desc: This method retrieves the mean humidity statistics for a specific
                month and year and returns the data in JSON format.
            @return: JSON-formatted data containing mean humidity statistics.
        '''
        category = 'meanHumid'
        data = utils.cal_HumidStat(year, month, category)
        data = utils.convertToJSON(data)

        return data

    def getAvgTemperatureHumidityStats(self, year, month):
        '''
            @param year: The year for which to retrieve statistics (int).
            @param month: The month for which to retrieve statistics (int).
            @desc: This method retrieves the average temperature and humidity statistics for a specific
                month and year and returns the data in JSON format.
            @return: JSON-formatted data containing average temperature and humidity statistics.
        '''
        data = utils.cal_AvgHighestLowestTemperatureHumidity(year, month)
        data = utils.convertToJSON(data)
        
        return data
    
    def getAvgHighestTemperatureStats(self, year, month):
        '''
            @param year: The year for which to retrieve statistics (int).
            @param month: The month for which to retrieve statistics (int).
            @desc: This method retrieves the average highest temperature statistics for a specific
                month and year and returns the data in JSON format.
            @return: JSON-formatted data containing average highest temperature statistics.
        '''
        category = 'highestTemp'
        data = utils.cal_AvgTemperatureHumidStat(year, month, category)
        data = utils.convertToJSON(data)
        
        return data
    
    def getAvgMeanTemperatureStats(self, year, month):
        '''
            @param year: The year for which to retrieve statistics (int).
            @param month: The month for which to retrieve statistics (int).
            @desc: This method retrieves the average mean temperature statistics for a specific
                month and year and returns the data in JSON format.
            @return: JSON-formatted data containing average mean temperature statistics.
        '''
        category = 'meanTemp'
        data = utils.cal_AvgTemperatureHumidStat(year, month, category)
        data = utils.convertToJSON(data)
        
        return data
    
    def getAvgLowestTemperatureStats(self, year, month):
        '''
            @param year: The year for which to retrieve statistics (int).
            @param month: The month for which to retrieve statistics (int).
            @desc: This method retrieves the average lowest temperature statistics for a specific
                month and year and returns the data in JSON format.
            @return: JSON-formatted data containing average lowest temperature statistics.
        '''
        category = 'lowestTemp'
        data = utils.cal_AvgTemperatureHumidStat(year, month, category)
        data = utils.convertToJSON(data)
        
        return data
    
    def getAvgHighestHumidityStats(self, year, month):
        '''
            @param year: The year for which to retrieve statistics (int).
            @param month: The month for which to retrieve statistics (int).
            @desc: This method retrieves the average highest humidity statistics for a specific
                    month and year and returns the data in JSON format.
            @return: JSON-formatted data containing average highest humidity statistics.
        '''
        category = 'highestHumid'
        data = utils.cal_AvgTemperatureHumidStat(year, month, category)
        data = utils.convertToJSON(data)
        
        return data
    def getAvgLowestHumidityStats(self, year, month):
        '''
            @param year: The year for which to retrieve statistics (int).
            @param month: The month for which to retrieve statistics (int).
            @desc: This method retrieves the average lowest humidity statistics for a specific
                month and year and returns the data in JSON format.
            @return: JSON-formatted data containing average lowest humidity statistics.
        '''
        category = 'lowestHumid'
        data = utils.cal_AvgTemperatureHumidStat(year, month, category)
        data = utils.convertToJSON(data)
        
        return data
    
    def getAvgMeanHumidityStats(self, year, month):
        '''
            @param year: The year for which to retrieve statistics (int).
            @param month: The month for which to retrieve statistics (int).
            @desc: This method retrieves the average mean humidity statistics for a specific
                month and year and returns the data in JSON format.
            @return: JSON-formatted data containing average mean humidity statistics.
        '''
        category = 'meanHumid'
        data = utils.cal_AvgTemperatureHumidStat(year, month, category)
        data = utils.convertToJSON(data)
        
        return data
